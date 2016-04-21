import sys, os
import textwrap
try:
    from urllib.parse import urljoin
except ImportError:
    # Python 2.7
    from urlparse import urljoin
import json
from collections import namedtuple
from functools import wraps
import requests
from tldextract import extract
import datetime
from datetime import timedelta
import random
import string


DEFAULT_URL = 'https://test.httpapi.com/api/'
# DEFAULT_URL = 'http://cn.resellerclub.com/'

MAX_RECORDS = 50  # 50 is the current max

class Address(namedtuple('Address', 'line_1 line_2 line_3 city state country zipcode')):
    def to_params(self):
        return {
            'address-line-1': self.line_1,
            'self-line-2': self.line_2,
            'self-line-3': self.line_3,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'zipcode': self.zipcode
        }

class ResellerError(RuntimeError):
    pass

def check_error(res):
    if isinstance(res, dict):
        status = res.get('status')
        if status and status.lower() == 'error':
            if 'message' in res:
                raise ResellerError(res['message'])
            elif 'error' in res:
                raise ResellerError(res['error'])
            else:
                raise ResellerError(res)
    return res

def append_slash(url):
    if not url.endswith('/'):
        return url + '/'
    return url

class ApiClient(object):

    def __init__(self, user_id, api_key, customer_id=0, contact_id=0, url=None, proxies=None):
        self.customer_id = customer_id
        self.contact_id = contact_id
        self.url = url or DEFAULT_URL
        self.session = requests.session()
        self.proxies = proxies
        self.session.params = {
            'auth-userid': user_id,
            'api-key': api_key
        }

    def request(self, http_method, api_method, params):
        path = '{}.json'.format(api_method)
        response = self.session.request(
            http_method, urljoin(append_slash(self.url), path), params=params, proxies=self.proxies, timeout=60)
        return response.json

    def domains_get_details(self, name):
        return self.request('GET', 'domains/details-by-name', {
            'domain-name': name,
            'options': 'All'
        })

    def domains_register(self, domain, years, ns, customer=None, reg_contact=None,
        admin_contact=None, tech_contact=None, billing_contact=None, invoice_option='NoInvoice', purchase_privacy=False,
        protect_privacy=False):
        """
        :param str domain: domain name to register
        :param int years: number of years to register for
        :param list[str] ns: list of nameservers
        :param int customer: customer to register on behalf of
        :param int reg_contact:
        :param int admin_contact:
        :param int tech_contact:
        :param int billing_contact:
        :param str invoice_option: one of NoInvoice, PayInvoice, or KeepInvoice
        :param bool purchase_privacy: optional
        :param bool protect_privacy: optional
        """
        if self.contact_id:
            reg_contact = admin_contact = tech_contact = billing_contact = self.contact_id
        elif not reg_contact:
            contact = self.contacts_default(customer)
            reg_contact = int(contact['Contact']['registrant'])

        if not admin_contact:
            admin_contact = reg_contact
        if not tech_contact:
            tech_contact = reg_contact
        if not billing_contact:
            billing_contact = reg_contact
        if not customer and self.customer_id:
            customer = self.customer_id

        return check_error(self.request('POST', 'domains/register', {
            'domain-name': domain,
            'years': years,
            'ns': ns,
            'customer-id': customer,
            'reg-contact-id': reg_contact,
            'admin-contact-id': admin_contact,
            'tech-contact-id': tech_contact,
            'billing-contact-id': billing_contact,
            'invoice-option': invoice_option,
            'purchase-privacy': purchase_privacy,
            'protect-privacy': protect_privacy
        }))

    def create_domain(self, domain, ns1=None, ns2=None):
        """默认注册域名"""
        # 获得域名后缀
        subdomain, maindomain, tld = extract(domain)
        if not tld:
            return {
                "status": 'error',
                "data": '不支持的域名后缀。',
                "domain": domain
            }

        check_result = self.domains_check_availability(maindomain, tld)
        if check_result[domain]['status'] == 'available':
            if not ns1 and not ns2:
                ns = ['comin.mercury.orderbox-dns.com', 'comin.venus.orderbox-dns.com',
                      'comin.earth.orderbox-dns.com', 'comin.mars.orderbox-dns.com']
            else:
                ns = [ns1, ns2]
            result = self.domains_register(domain, 1, ns, self.customer_id, self.contact_id)
            if 'actionstatus' in result and result['actionstatus'] == 'Success':
                password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
                return {
                    'status': 'success',
                    'domain': domain,
                    'data': {
                        '控制面板用户名': domain,
                        '开通时间': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        '到期时间': (datetime.datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d %H:%M:%S"),
                        '控制面板密码': password,
                        '控制面板': 'http://domain.shibangsoft.com'
                    },
                    'datetime': datetime.datetime.now()
                }
            else:
                return {
                    'domain': domain,
                    'status': 'error',
                    'data': '注册域名时发生错误，返回结果: {0}'.format(result),
                    'type': 'create',
                    'datetime': datetime.datetime.now()
                }
        elif check_result[domain]['status'] == 'regthroughus':
            return {
                'status': 'error',
                'data': '在resellerclub.com上域名{}查询为已被该平台注册。'.format(domain),
                'type': 'check',
                'datetime': datetime.datetime.now()
            }
        elif check_result[domain]['status'] == 'regthroughothers':
            return {
                'status': 'error',
                'data': '在resellerclub.com上域名{}查询为已被其它平台注册。'.format(domain),
                'type': 'check',
                'datetime': datetime.datetime.now()
            }
        else:
            return {
                'status': 'error',
                'data': '域名{0}查询可用性时出现意外错误：{1}'.format(domain, check_result),
                'type': 'check',
                'datetime': datetime.datetime.now()
            }

    def domains_default_ns(self, customer_id):
        """Return default name servers for a customer
        :param customer_id:
        """
        return check_error(self.request('GET', 'domains/customer-default-ns', {
            'customer-id': customer_id
        }))

    def contacts_add(self, type, name, company, email, address, phone_cc, phone, customer_id):
        """
        :param type:
        :param name: name of the contact
        :param company: name of company
        :param email:
        :param address:
        :param phone_cc:
        :param phone:
        :param customer_id:
        """
        params = {
            'type': type,
            'name': name,
            'company': company,
            'email': email,
            'phone-cc': phone_cc,
            'phone': phone,
            'customer-id': customer_id
        }
        params.update(address.to_params())
        return check_error(self.request('POST', 'contacts/add', params))

    def contacts_default(self, customer_id, type='Contact'):
        return self.request('POST', 'contacts/default', {
            'customer-id': customer_id,
            'type': type
        })

    def customers_add(self, username, password, name, company, address, phone_cc,
        phone, lang_pref):
        """
        :param username: email address
        :param password:
        :param name:
        :param company:
        :param address:
        :param phone_cc:
        :param phone:
        :param lang_pref:
        """
        params = {
            'username': username,
            'passwd': password,
            'name': name,
            'company': company,
            'phone-cc': phone_cc,
            'phone': phone,
            'lang-pref': lang_pref
        }
        params.update(address.to_params())
        return check_error(self.request('POST', 'customers/signup', params))


    def domains_check_availability(self, domain, tlds, suggest_alternative=False):
        """
        :param domain: domain to check availability for
        :param tlds: tlds of the domains to check
        :param suggest_alternative: True to return a list of alternative domain names
        """
        return check_error(self.request('GET', 'domains/available', {
            'domain-name': domain,
            'tlds': tlds,
            'suggest-alternative': suggest_alternative
        }))

    def dns_activate(self, domain_name):
        order_id = self.domains_get_details(domain_name)['entityid']
        return self.request('POST', 'dns/activate', {
            'order-id': order_id,
        })

    def dns_search(self, domain, type, no_of_records=10, host=None):
        return self.request('GET', 'dns/manage/search-records', {
            'domain-name': domain,
            'type': type,
            'no-of-records': no_of_records,
            'page-no': 1,
            'host': host
        })

    def dns_add_record(self, record_type, domain, value, host=None, ttl=None):
        return self.request('POST', 'dns/manage/add-{}-record'.format(record_type), {
            'domain-name': domain,
            'value': value,
            'host': host,
            'ttl': ttl or None
        })

    def dns_delete_record(self, record_type, domain, value, host=None):
        return self.request('POST', 'dns/manage/delete-{}-record'.format(record_type), {
            'domain-name': domain,
            'value': value,
            'host': host,
        })

if __name__ == '__main__':
    client = ApiClient('527221', 'api_key', 'customer_id')
    domain = 'sbmzhcn.in'
    result = client.create_domain(domain)
    print(result)