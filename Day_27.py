from PIL import Image

image = Image.open('3.jpg')
image_resize = image.resize((512, 512))
image_resize.save('conversao.webp', format='WEBP')