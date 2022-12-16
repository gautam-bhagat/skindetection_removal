import PIL
from PIL import Image
from PIL import ImageChops # used for multiplying images

# open images
painting = Image.open("Testimage2.jpg")
mask     = Image.open("YCRCBRESULT.jpg")


def black_onto(img1, img2):  
    # create blank white canvas to put img2 onto
    resized = Image.new("RGB", img1.size, "white")

    # define where to paste mask onto canvas
    img1_w, img1_h = img1.size
    img2_w, img2_h = img2.size
    box = (img1_w//2-img2_w//2, img1_h//2-img2_h//2, img1_w//2-img2_w//2+img2_w, img1_h//2-img2_h//2+img2_h)

    # multiply new mask onto image
    resized.paste(img2, box)
    return ImageChops.multiply(img1, resized)


out = black_onto(painting, mask)
print(type(out))
out.show() # this gives the output image shown above
out = out.save("final.jpg")