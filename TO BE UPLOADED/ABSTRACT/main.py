# print(612/250)
# print(5000/2.5)

from PIL import ImageDraw , Image
img = Image.new('RGBA',(5000,5000),color=(150,150,150,0))
draw = ImageDraw.Draw(img)
# left red
draw.polygon([(0,0),(2000+1000,0),(1000,5000),(0,5000)], fill=(255,63,74,100))
# purple background middle
draw.polygon([(2000,0),(5000,0),(5000-2000,5000),(0,5000)], fill=(45,9,83,180))
img.save("delete.png","PNG")