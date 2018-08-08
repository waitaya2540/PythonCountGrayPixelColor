import os
from PIL import Image

gray = 0
no_gray = 0

for root, dirs, files in os.walk("imgtest"):
    # print files
    for name in files:
        img = Image.open(os.path.join(root, name))

        for pixel in img.getdata():
            if pixel >= (128, 128, 128):
                gray += 1
            else:
                no_gray += 1
    

print('Gray = ' + str(gray)+' pixels. || NO Gray = '+str(no_gray) + ' pixels.')