from PIL import Image
from pix2tex.cli import LatexOCR

img = Image.open('222.png')
model = LatexOCR()
print(model(img))