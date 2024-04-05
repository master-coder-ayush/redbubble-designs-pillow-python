from PIL import Image , ImageDraw,ImageFont
import os
fonts = os.listdir('D:\\Ayush\\1 Million$ - 31-12-2023\\REDBUBBLE\\CODING\\fonts')
W,H = (5000,5000)
img = Image.new('RGBA',(5000,5000),color=(200,150,150,180))
draw = ImageDraw.Draw(img)

myfont = ImageFont.truetype('fonts\\'+fonts[0],1100)

# left most box
draw.polygon([(0,0),(999,0),(999,5000),(0,5000)], fill='black', outline=None)
# center most box
draw.polygon([(1019,0),(3981,0),(3981,5000),(1019,5000)], fill='gray', outline=None)
# right most box
draw.polygon([(4000,0),(5000,0),(5000,5000),(4000,5000)], fill='black', outline=None)
# text
draw.text(((W-1570)/2,(H-1500)/2),"222",fill = 'red',font=myfont)

# lines
for i in range(20):
    draw.line((1000+i, 0) + (1000+i,5000), fill='white')
    draw.line((5000-(1000+i), 0) + (5000-(1000+i),5000), fill='white')

img.save("delete.png")