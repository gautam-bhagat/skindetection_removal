import cv2 as c
import numpy as np

#opening image for operations
img = c.imread("testimage.jpg")
# print(img)

hsvLowerSkinRange = (0,15,0)
hsvHigherSkinRange = (17,170,255)

ycrLowerSkinRange = (0,135,85)
ycrHigherSkinRange = (255,180,135)

#CONVERTING RGB IMAGE TO HSV
img_hsv  = c.cvtColor(img, c.COLOR_BGR2HSV)
hsv_mask = c.inRange(img_hsv,hsvLowerSkinRange,hsvHigherSkinRange)
hsv_mask = c.morphologyEx(hsv_mask,c.MORPH_OPEN,np.ones((3,3),np.uint8))

#CONVERTING RGB IMAGE TO YCrCb
img_ycrcb  = c.cvtColor(img, c.COLOR_BGR2YCrCb)
ycrcb_mask = c.inRange(img_ycrcb,ycrLowerSkinRange,ycrHigherSkinRange)
ycrcb_mask = c.morphologyEx(ycrcb_mask,c.MORPH_OPEN,np.ones((3,3),np.uint8))

# MERGING SKIN DETECTION FOR MORE OPTIMAL RESULT (HSV and YCRCB)
global_m = c.bitwise_and(ycrcb_mask,hsv_mask)
global_m = c.medianBlur(global_m,3)
global_m = c.morphologyEx(global_m,c.MORPH_OPEN,np.ones((4,4),np.uint8))



HSV_RESULT = c.bitwise_not(hsv_mask)
YCRCB_RESULT = c.bitwise_not(ycrcb_mask)
GLOBAL_RESULT = c.bitwise_not(global_m)

#SHOW RESULT
# c.imshow("HSVRESULT.jpg",HSV_RESULT)
# c.imshow("YCRCBRESULT.jpg",YCRCB_RESULT)
# c.imshow("GLOBALRESULT.jpg",GLOBAL_RESULT)

c.imwrite("HSVRESULT.jpg",HSV_RESULT)
c.imwrite("YCRCBRESULT.jpg",YCRCB_RESULT)
c.imwrite("GLOBALRESULT.jpg",GLOBAL_RESULT)

c.waitKey(0)
c.destroyAllWindows()

import PIL
from PIL import Image
from PIL import ImageChops # used for multiplying images

# open images
painting = Image.open("testimage.jpg")
mask     = Image.open("YCRCBRESULT.jpg")


def black_onto(img1, img2):  
    resized = Image.new("RGB", img1.size, "white")

    
    img1_w, img1_h = img1.size
    img2_w, img2_h = img2.size
    box = (img1_w//2-img2_w//2, img1_h//2-img2_h//2, img1_w//2-img2_w//2+img2_w, img1_h//2-img2_h//2+img2_h)

    
    resized.paste(img2, box)
    return ImageChops.multiply(img1, resized)


out = black_onto(painting, mask)
print(type(out))

out = out.save("final.jpg")
# img = Image.open('GLOBALRESULT.png')
# img = img.convert("RGBA")

# pixdata = img.load()

# width, height = img.size
# for y in range(height):
#     for x in range(width):
#         if pixdata[x, y] == (255, 255, 255, 255):
#             pixdata[x, y] = (255, 255, 255, 0)

# img.save("img2.png", "PNG")

# OVERLaying try1
# background = Image.open("testimage.jpg")
# overlay = Image.open("img2.png")

# background = background.convert("RGBA")
# overlay = overlay.convert("RGBA")

# new_img = Image.blend(background, overlay, 0.5)
# new_img.save("new.png","PNG")

#OVERLAYING try2
# image_1 = Image.open('testimage.jpg') 
# image_2 = Image.open('YCRCBRESULT.jpg') 
# pixels = list(image_2.getdata())

# for y in range(image_2.size[1]):
#     for x in range(image_2.size[0]):
#         if pixels ==(o,o,o):
#           image_2.putdata(pixels((x,y),(0,0,0)))

# image_2.save('painted.bmp')



# import PIL
# from PIL import Image
# from PIL import ImageChops # used for multiplying images

# img = Image.open("testimage.jpg")
# img = img.tobitmap()

# # open images
# painting = img
# mask     = Image.open("YCRCBRESULT.bmp")


# def black_onto(img1, img2):  
#     # create blank white canvas to put img2 onto
#     resized = Image.new("RGB", img1.size, "white")

#     # define where to paste mask onto canvas
#     img1_w, img1_h = img1.size
#     img2_w, img2_h = img2.size
#     box = (img1_w/2-img2_w/2, img1_h/2-img2_h/2, img1_w/2-img2_w/2+img2_w, img1_h/2-img2_h/2+img2_h)

#     # multiply new mask onto image
#     resized.paste(img2, box)
#     return ImageChops.multiply(img1, resized)


# out = black_onto(painting, mask)
# out.show() # this gives the output image shown above

# painting = Image.open("painting.bmp")
