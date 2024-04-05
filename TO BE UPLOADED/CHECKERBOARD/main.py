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
    
    b = (randint(0,255),randint(0,255),randint(0,255),100)
    rainbow = [(148,0,211),(75,0,130),(0,0,255),(0,255,0),(255,255,0),(255,127,0),(255,0,0)]
    # number of boxes
    boxes = 6
    x = 5000/boxes

    # w = "white" #  (255,255,255)
    # b = "black" #  (0,0,0)
    for j in range(0,boxes,1):
        for i in range(0,boxes,1):
            if (i+j)%2==0:
                # w = (randint(0,255),randint(0,255),randint(0,255),180)
                draw.rounded_rectangle([(j*x,i*x),((j+1)*x,(i+1)*x)], fill=rainbow[randint(0,6)], outline=None,radius=0)
            else:
                draw.rounded_rectangle([(j*x,i*x),((j+1)*x,(i+1)*x)], fill=b, outline=None,radius=0)
    # img.save("dlete"+str(dd)+".png","PNG")
    # print("HO GYA"+str(dd))
    img.save("rainbow_checker_"+str(dd)+".png","PNG")
    print("HO GYA "+str(dd))
    break