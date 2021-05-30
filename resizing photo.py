#resizing the photo

from PIL import Image
imgPath ='\\Users\RCZS\Downloads\R33d02c67b4a6e90abe2d7a58f764edd8.jpg'
img = Image.open(imgPath)
size=(500,500)
out=img.resize(size)
out.show()

