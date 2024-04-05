'''
Pehle redbubble pe complete photo on complete t-shirt wale pe check krna taki txt corner pe hi visible ho
'''
from random import randint
from PIL import Image , ImageDraw ,ImageFont
# import os
# fonts = os.listdir(r'D:\Ayush\1 Million$ - 31-12-2023\REDBUBBLE\CODING\fonts')

for dd in range(20):
    img = Image.new('RGBA',(5000,5000),color=(randint(0,255),randint(0,255),randint(0,255),180))
    draw = ImageDraw.Draw(img)
    
    # for random fonts
    # myfont = ImageFont.truetype("fonts\\"+fonts[randint(0,len(fonts)-1)],250)

    myfont = ImageFont.truetype('fonts\Lobster-Regular.ttf',250)
    txt = "Don't tell your dreams show them!!!"
    msg = txt.split(" ")
    txt2 = msg[0]
    for x in range(1,len(msg)):
        if(x%2==0):
            txt2 = txt2+"\n"+msg[x]
        else:
            txt2 = txt2+" "+msg[x]
    draw.text((3500,800),txt2,font = myfont,fill = "BLACK")
    img.save("s"+str(dd)+".png","PNG")
    print("HO GYA "+str(dd))
    