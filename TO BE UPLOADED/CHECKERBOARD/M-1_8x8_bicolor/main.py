'''
20 X 20
bi-color
destorted -- illusion
'''

from random import randint
from PIL import Image , ImageDraw
for dd in range(100):
    img = Image.new('RGBA',(5000,5000),color=(150,150,150,0))
    draw = ImageDraw.Draw(img)

    # number of boxes
    boxes = 8
    x = 5000/boxes

    w = (randint(0,255),randint(0,255),randint(0,255))
    b = (randint(0,255),randint(0,255),randint(0,255))
    # w = "white" #  (255,255,255)
    # b = "black" #  (0,0,0)
    for j in range(0,boxes,1):
        for i in range(0,boxes,1):
            if (i+j)%2==0:
                draw.rounded_rectangle([(j*x,i*x),((j+1)*x,(i+1)*x)], fill=w, outline=None,radius=0)
            else:
                draw.rounded_rectangle([(j*x,i*x),((j+1)*x,(i+1)*x)], fill=b, outline=None,radius=0)
    # img.save("dlete"+str(dd)+".png","PNG")
    # print("HO GYA"+str(dd))
    img.save("dlete"+str(dd)+".png","PNG")
    print("HO GYA"+str(dd))
