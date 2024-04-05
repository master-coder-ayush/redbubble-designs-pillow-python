'''
proper range of rgb only for light shades 
'''
from random import randint
from PIL import Image , ImageDraw, ImageFont
msg = "MADE\nWITH\nLOVE"
W,H = (5000,5000)
myfont = ImageFont.truetype('fonts\AnnyantRoman.ttf',850)
# background = (randint(0,255),randint(0,255),randint(0,255),0)

for i in range(50):
    img = Image.new('RGBA',(5000,5000),color=(0,0,0,0))
    draw = ImageDraw.Draw(img)
    w,h = draw.textsize(msg,font=myfont)
    draw.ellipse(((0,0),(5000,5000)), fill =(randint(30,255),randint(30,255),randint(30,255)))
    draw.text(((W-w)/2,(H-h)/2), msg,font=myfont,fill =(randint(0,255),randint(0,255),randint(0,255))) 
    draw.text(((W-w-80)/2,(H-h-80)/2), msg,font=myfont,fill=(randint(0,255),randint(0,255),randint(0,255))) 
    draw.text(((W-w-80-40)/2,(H-h-80-40)/2), msg,font=myfont,fill=(randint(0,255),randint(0,255),randint(0,255))) 
    draw.text(((W-w-80-80)/2,(H-h-80-80)/2), msg,font=myfont,fill=(randint(0,255),randint(0,255),randint(0,255))) 
    draw.text(((W-w-80-100)/2,(H-h-80-100)/2), msg,font=myfont,fill=(randint(0,255),randint(0,255),randint(0,255))) 
    img.save("test"+str(i)+".png","PNG")