from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
import numpy as np
import cv2


im = Image.open('image.jpg')
mask = Image.new('L', im.size, 0)
draw = ImageDraw.Draw(mask)
draw.rectangle([(4500,1000), (200,2300) ], fill=255)
blurred = im.filter(ImageFilter.GaussianBlur(30))
im.paste(blurred, mask=mask)
im.save("blurredImg.jpg")
# 2nd part blur*********************************
im = Image.open('blurredImg.jpg')
mask = Image.new('L', im.size, 0)
draw = ImageDraw.Draw(mask)
draw.rectangle([ (2000,4000), (1600,4300) ], fill=255)
blurred = im.filter(ImageFilter.GaussianBlur(30))
im.paste(blurred, mask=mask)
im.save("12.jpg")
im = Image.open("12.jpg")
mask = Image.new('L', im.size, 0)
draw = ImageDraw.Draw(mask)
draw.rectangle([ (4000,4300), (300,5000) ], fill=255)
blurred = im.filter(ImageFilter.GaussianBlur(30))
im.paste(blurred, mask=mask)
im.save("12.jpg")
# path = "12.jpg"




# Open an image
# im = Image.open('image.jpg')

# x1=4000
# y1=2000
# x2=100
# y2=3300
# # ****************************************************************
# """some rectangle part is not blur """
# img = cv2.imread('image.jpg')
# blurred_img = cv2.GaussianBlur(img,(33,33),300)
# mask = np.zeros((6081,4300,3), 'uint8')
# mask = cv2.rectangle(mask, (x1,y1), (x2,y2), (255, 255, 255),-1)
# out = np.where(mask==np.array([255, 255, 255]), img, blurred_img)
# cv2.imwrite("./Blur.jpg", out)
# # *************************************************************
# """rectangle part is blur """
# Create rectangle mask
# mask = Image.new('L', im.size, 0)
# draw = ImageDraw.Draw(mask)
# draw.rectangle([ (x1,y1), (x2,y2) ], fill=255)

# # Blur image
# blurred = im.filter(ImageFilter.GaussianBlur(52))
# # Paste blurred region and save result
# im.paste(blurred, mask=mask)
# im.save("blurredImg.jpg")