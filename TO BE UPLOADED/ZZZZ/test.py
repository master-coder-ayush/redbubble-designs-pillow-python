from random import randint
from PIL import Image , ImageDraw
for dd in range(150):
    img = Image.new('RGBA',(5000,5000),color=(0,0,55,180))
    draw = ImageDraw.Draw(img)
    for mmmm in range(15):
        draw.polygon([(randint(0,5000),randint(0,5000)),(randint(0,5000),randint(0,5000)),(randint(0,5000),randint(0,5000)),(randint(0,5000),randint(0,5000)),(randint(0,5000),randint(0,5000)),(randint(0,5000),randint(0,5000))], fill=(randint(0,255),randint(0,255),randint(0,255),180))

    rgb_img = img.convert('RGBA')
    img.save("s"+str(dd)+".png","PNG")
    print("HO GYA "+str(dd))
    