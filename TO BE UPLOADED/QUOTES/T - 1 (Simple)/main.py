'''
Simple quotes 
by wala part add krna h
'''
from random import randint
from PIL import Image , ImageDraw, ImageFont
quotes = ["Every twenty years I reinvent myself.","I have time to fix this.","Fearlessness is the mother of reinvention.","This is your year to sparkle.","Be your own person, be unique.","Still fit into high school earrings.","I made a choice about business.","You got to nourish to flourish.","What's the stop sign mean again?","Change what you are complaining about.","Don’t wait for opportunity. Create it!","A decision was made, I complied.","I live my best life now.","I'm figuring it out by myself.","Recipe for failure. Changed my ingredients.","Talking without action is just complaining.","Stay patient and trust your journey.","I am this now and always.","I stopped getting my piano tuned.","Be young while you still can.","Associate with people who inspire you.","I learned mechanics in rocket league.","Every problem has a creative solution.","Someone has to do the paperwork.","Lost in wilderness, he found himself.","Normal is boring, weird is fun.","Boisterous gas freed, relief, remorse, pride!","Nothing to declare. Much to remember.","Lovers gonna love, haters gonna hate.","Sharp new yellow pencil. Limitless potential.","Spongebob is my one true love.","Apathetic prophet makes a pathetic profit.","Lost my wallet, found my desires.","Insomnia gives me time to think.","Married, till fatness do us part.","Say something nice or don't talk.","Coffee before art, goodbye straight lines.","I got it from my mama.","Painfully, he changed is to was.","Protect your dreams from your nightmare.","Lightning hides the color of night.","Honestly, all crows are not ravens.","Sorry soldier, shoes sold in pairs.","Love hurts because it holds hearts.","Voyager still transmitted, but Earth didn’t.","Seed becomes a tree, son becomes stranger.","Power does not pardon, power punishes.","I asked, you answered in silence.","Sometimes pretty birds cannot sing well.","Tripped over luck, stumbled upon tragedy.","Recover never really ends, does it?"]
W,H = (5000,5000)
myfont = ImageFont.truetype('fonts\Simply2CondensedRegular-owB1d.ttf',690)
background = (randint(0,255),randint(0,255),randint(0,255),0)

for i in range(len(quotes)):
    print(i," chal rha h")
    msg = quotes[i]
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
        img.save("test"+str(i)+".png","PNG")
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
        draw.text(((W-w)/2,(H-h)/2), sms,font=myfont,align='center',fill =(randint(0,255),randint(0,255),randint(0,255))) 
        img.save("test"+str(i)+".png","PNG")
        continue
    else:
        continue