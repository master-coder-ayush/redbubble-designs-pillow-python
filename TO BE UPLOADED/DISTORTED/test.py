from random import randint
from PIL import Image , ImageDraw
for dd in range(100):
    img = Image.new('RGBA',(5000,5000),color=(150,150,150,0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(0,0),(2500,5000)], fill=(randint(0,255),randint(0,255),randint(0,255),180), outline=None,radius=0)
    draw.rounded_rectangle([(2500,0),(5000,5000)], fill=(randint(0,255),randint(0,255),randint(0,255),180), outline=None,radius=0)
    rgb_img = img.convert('RGBA')
    for j in range(2000):
        for i in range(1,1000):
            x = (2500-i,1500+j)   # left side ka pehla - red
            y = (2499+i,1500+j)   # right - violet
            rx,gx,bx,ox = rgb_img.getpixel(x)    # red
            ry,gy,by,oy = rgb_img.getpixel(y)    # violet
            draw.point(y,fill=(rx,gx,bx,ox))     # violet ki jagah red
            draw.point(x,fill=(ry,gy,by,oy))     # red ki jagah violet
    img.save("s"+str(dd)+".png","PNG")
    print("HO GYA "+str(dd))