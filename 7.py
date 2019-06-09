#Challenge 7
#http://www.pythonchallenge.com/pc/def/hockey.html -> "it's in the air. look at the letters."
#http://www.pythonchallenge.com/pc/def/oxygen.html

#need to install pillow: pip install Pillow
from PIL import Image 
  
filename = "oxygen.png"
with Image.open(filename) as image:
   pixels=image.load()
   #Gets the middle row from image (more or less the grey pixels)
   row = [image.getpixel((x, image.height/2)) for x in range(image.width)]
   #Ignore all the pixels that repeats by 7 times
   row=row[::7]
   print(row)
   #because any pixel in Grey has R=G=B
   ords = [r for r, g, b, a in row if r == g == b]
   #Translate the pixels to char (because is in the range 0 to 255)
   #And the hint: it's in the air. look at the letters.
   print("".join(map(chr, ords)))
   #Translate the message from the image
   nxt_level=[105, 110, 116, 101, 103, 114, 105, 116, 121]
   print("".join(map(chr, nxt_level)))
   #Use the bellow for to print the entire image pixel by pixel
   for i in range(image.height):
      row = [image.getpixel((x, i)) for x in range(image.width)]
      #print(row)
      #print('/n')
   