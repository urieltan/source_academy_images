import PIL
from PIL import Image
import numpy as np

#Please downsize it to 64x64 before using
samp_jpg = "C:/Users/Tan/Downloads/nice_image.jpg"
samp_img = Image.open(samp_jpg)
print( samp_img.size)

I = np.asarray(samp_img)
print(I.shape)
print(I)



f = open("C:/Users/Tan/Downloads/nice_string.txt", "w")
for z in range(4096):
    x=0
    y=0
    for i in range(12):
        if i%2==1:
            x=x|((z&(1<<i))>>((i+1)//2))
        else:
            y=y|((z&(1<<i))>>((i)//2))
    x=x^0b101010
    y=y^0b101010
    value = 1024 + I[y*2][x*2][0]//16*256 + I[y*2][x*2][1]//16*16 + I[y*2][x*2][2]//16 
    f.write(str(value))
f.close()
