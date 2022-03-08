from PIL import Image

image = Image.open("mur.png")
# image = image.convert('L')
image.show()
# image.save('gray-pillow.jpeg', 'jpeg')
