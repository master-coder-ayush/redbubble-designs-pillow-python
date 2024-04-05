# import winsound
# duration = 1000 # milliseconds
# freq = 440 # Hz
# winsound.Beep(freq,duration)

'''
Good fonts
AnnyantRoman.ttf
Simply2CondensedRegular-owB1d.ttf
BADABB__.ttf
'''

'''
I can use paint to find the coordinates of an image
''' 

# for making a blank image with a single color
# from PIL import Image
# img = Image.new('RGB', (5000, 5000), color = (14,25,35))   # img = Image.new(mode, size, color)
# img.save('pil_red.png')                                    # img.save(filename)

# for writing text on image
# documentation
# from PIL import Image, ImageDraw
# img = Image.new('RGB', (100, 30), color = (73, 109, 137))
# d = ImageDraw.Draw(img)
# d.text((10,10), "Hello World", fill=(255,255,0)) 
# img.save('pil_text.png')

# edited
# from PIL import Image, ImageDraw
# img = Image.new('RGB', (100, 30), color = (73, 109, 137))
# d = ImageDraw.Draw(img)
# texts = ['text1','text2','text3','text4','text5','text6','text7','text8','text9','text10']
# for i in range(10):
#     text = texts[i]
#     d.text((10,10), text , fill=(255,255,0))
#     filename = 'text'+str(i)+'.png'
#     img.save(filename)

# from PIL import Image, ImageDraw
# img = Image.new('RGB', (5000, 5000), color = (73, 109, 137))
# d = ImageDraw.Draw(img)
# texts = ['text1','text2','text3','text4','text5','text6','text7','text8','text9','text10']
# for i in range(10):
#     text = texts[i]
#     d.text((1000,1000), text , fill=(255,255,0))
#     d.text((1000,1000), 'overwrite' , fill=(255,255,0))
#     filename = 'text'+str(i)+'.png'
#     img.save(filename)

# using font documentation
# from PIL import Image, ImageDraw, ImageFont
# img = Image.new('RGB', (100, 30), color = (73, 109, 137))
# fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
# d = ImageDraw.Draw(img)
# d.text((10,10), "Hello world", font=fnt, fill=(255, 255, 0))  d.text(text coordinates, text, font, fill=color)
# img.save('pil_text_font.png')

# setting text size using font
# from PIL import Image, ImageDraw ,ImageFont
# img = Image.new('RGB', (5000, 5000), color = (73, 109, 137))
# d = ImageDraw.Draw(img)
# myfont = ImageFont.truetype('fonts\Lobster-Regular.ttf',500)
# d.text((4500,10), "Hello World",font=myfont, fill=(255,255,0)) 
# img.save('pil_text.png')

# Making transparent images by using RGBA color format and putting (,,,0) i.e., 0 at the end value
# from PIL import Image, ImageDraw ,ImageFont
# img = Image.new('RGBA', (5000, 5000), color = (73, 109, 137,0))
# d = ImageDraw.Draw(img)
# myfont = ImageFont.truetype('fonts\Lobster-Regular.ttf',500)
# d.text((4500,10), "Hello World",font=myfont, fill=(255,255,0)) 
# img.save('pil_text.png')

# Drawing cross over image using lines
# from PIL import Image,ImageDraw
# img = Image.new('RGBA',(5000,5000),color=(75,68,200,255)) # color=(red,blue,green,opacity*255 full opacity , 128 half opacity*)
# draw = ImageDraw.Draw(img)
# draw.line((0, 0) + img.size, fill='black')
# draw.line((0, img.size[1], img.size[1], 0), fill='black')
# img.save('draw.png')

# Draw multiline text
# from PIL import Image,ImageDraw,ImageFont
# img = Image.new('RGBA',(5000,5000),color=(122,64,84,128))
# draw = ImageDraw.Draw(img)
# draw.multiline_text((2000,2000),'LOL\nhi',fill='black')
# img.save('lines.png')

# Drawing arc 
# from PIL import Image, ImageDraw
# img = Image.new('RGBA',(500,500),color=(150,250,160,244))
# draw = ImageDraw.Draw(img)
# draw.arc([(100,150),(300,450)], 0, 120, fill=(128,128,128), width=10)
# img.save('arc.png')

# Drawing ellipse
# from PIL import Image,ImageDraw
# img = Image.new('RGBA',(500,500),color=(150,250,160,244))
# draw = ImageDraw.Draw(img)
# draw.ellipse([(100,250),(300,400)], fill=(200,164,65), outline='black', width=10)
# img.save('ellipse.png')

# Drawing curved lines - faltu h kisi kam ka nhi 
# from PIL import Image,ImageDraw
# img = Image.new('RGBA',(500,500),color=(150,250,160,244))
# draw = ImageDraw.Draw(img)
# draw.line([(0,0),(200,254)], fill='black', width=2, joint='curve')
# draw.line([(200,254),(0,451)], fill='black', width=2, joint='curve')
# img.save('curved_lines.png')

# Drawing a polygon
# from PIL import Image,ImageDraw
# img = Image.new('RGBA',(500,500),color=(150,250,160,244))
# draw = ImageDraw.Draw(img)
# draw.polygon([(100,100),(125,150),(200,225),(450,400),(200,50),(50,336)], fill=(154,33,200), outline='black')
# img.save('polygon.png')

# Drawing a point
# from PIL import Image,ImageDraw
# img = Image.new('RGBA',(100,100),color=(150,250,160,244))
# draw = ImageDraw.Draw(img)
# draw.point((52,65), fill='black')
# img.save('point.png')

# Text in the middle of the image 
# from PIL import Image , ImageDraw
# msg = "HI!!!"
# W,H = (5000,5000)
# img = Image.new('RGBA',(5000,5000),color=(150,150,150,0))
# draw = ImageDraw.Draw(img)
# if you have ImageFont and myfont the specify it like
# w,h = draw.textsize(msg,font = myfont)
# w,h = draw.textsize(msg)
# draw.text(((W-w)/2,(H-h)/2),msg,fill = "BLACK")
# img.save("hello.png","PNG")

# Round rectangles
# from PIL import Image , ImageDraw
# img = Image.new('RGBA',(5000,5000),color=(150,150,150,0))
# draw = ImageDraw.Draw(img)
# draw.rounded_rectangle([(1405,3535),(4020,4555)], fill=(255,0,0,180), outline=None,radius=15)
# img.save("hello.png","PNG")

# Circle -- can be used as background
# from PIL import Image , ImageDraw
# img = Image.new('RGBA',(5000,5000),color=(150,150,150,0))
# draw = ImageDraw.Draw(img)
# draw.ellipse([(0,0),(5000,5000)], fill=(255,0,0,180), outline=None,width=0)
# img.save("hello.png","PNG")

# Text in center -- options left,right,center
# from PIL import Image , ImageDraw,ImageFont
# msg = "HI!!!"
# W,H = (5000,5000)
# img = Image.new('RGBA',(5000,5000),color=(150,150,150,0))
# draw = ImageDraw.Draw(img)
# myfont = ImageFont.truetype('fonts\Lobster-Regular.ttf',500)
# w,h = draw.textsize(msg,font = myfont)
# draw.text(((W-w)/2,(H-h)/2),msg,fill = "BLACK",font=myfont, align = 'center')
# img.save("hello.png","PNG")