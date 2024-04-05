'''
Simple quotes 
by wala part add krna h
6 se 7 words wale hi
'''
from random import randint
from PIL import Image , ImageDraw, ImageFont
with open ("life.txt", "r") as myfile:
    data = myfile.read().splitlines()

quotes = []
for x in range(len(data)):
    if(x%2==0):
        quotes.append(data[x])

W,H = (5000,5000)
myfont = ImageFont.truetype('fonts\Simply2CondensedRegular-owB1d.ttf',690)
background = (randint(0,255),randint(0,255),randint(0,255),0)

for i in range(len(quotes)):
    msg = quotes[i]
    title = msg
    msg = msg.split(" ")
    sms = []
    if(len(msg)<=6):
        for j in range(len(msg)):
            if(j==2):
                sms.append(msg[j]+" ")
                sms.append("\n")
            elif(j==4):
                sms.append(msg[j]+" ")
                sms.append("\n")
            else:
                sms.append(msg[j]+" ")
        sms = ''.join(www for www in sms)
        img = Image.new('RGBA',(5000,5000),color=(0,0,0,0))
        draw = ImageDraw.Draw(img)
        w,h = draw.textsize(sms,font=myfont)
        draw.text(((W-w)/2,(H-h)/2), sms,font=myfont,align='center',fill ='black') 
        img.save("Designs\\"+title+".png","PNG")
        print(i," ho gya")
        continue

    if(len(msg)>6 and len(msg)<=7):
        for j in range(len(msg)):
            if(j==2):
                sms.append(msg[j]+" ")
                sms.append("\n")
            elif(j==4):
                sms.append(msg[j]+" ")
                sms.append("\n")
            else:
                sms.append(msg[j]+" ")
        sms = ''.join(www for www in sms)
        img = Image.new('RGBA',(5000,5000),color=(0,0,0,0))
        draw = ImageDraw.Draw(img)
        w,h = draw.textsize(sms,font=myfont)
        draw.text(((W-w)/2,(H-h)/2), sms,font=myfont,align='center',fill ='black') 
        img.save("Designs\\"+title+".png","PNG")
        print(i," ho gya")
        continue

    else:
        continue

        