from pyocr import tesseract
from PIL import Image
imagefile = Image.open('code.jpg')
val = tesseract.image_to_string(imagefile)
print(val)
