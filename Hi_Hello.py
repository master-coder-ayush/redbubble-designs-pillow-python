import os
from PIL import Image,ImageFont,ImageDraw
from random import randint

fonts = os.listdir(r'D:\Ayush\1 Million$ - 31-12-2023\REDBUBBLE\CODING\fonts')
for i in range(15):
    x,y,z = randint(1,255),randint(1,255),randint(1,255)
    img = Image.new("RGBA",(5000,5000),color=(x,y,z))
    myfont = ImageFont.truetype('fonts\\'+fonts[i],750)
    d = ImageDraw.Draw(img)
    
    d.text((500,1800),'HI\nHello',fill=(150,160,201),font=myfont)
    img.save('lol'+str(i)+'.png')