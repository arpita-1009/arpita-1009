import tesserocr
from PIL import Image
import pypyodbc


print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

image = Image.open('sample.jpg')
print(tesserocr.image_to_text(image))  # print ocr text from image
# or
print(tesserocr.file_to_text('sample.jpg'))


# import cv2
# import pytesseract
# import tesserocr


# img = cv2.imread('invoice-sample.jpg')

# d = pytesseract.image_to_data(img)
# print(d)
# from pdf2image import convert_from_path
# # import pandas as pd
# # import tesserocr

# def pdf_to_text(path):
#    texts_guj = []
#    #texts_eng = []
#    print("ghghds")
#    images = convert_from_path(path,260,output_folder=r'')
#    print("ghghds")
#    for i in range(len(images)):
#       print(i)
#       # text_g = tesserocr.image_to_text(images[i],lang='guj')
#       # texts_guj.append(text_g)

#    return texts_guj


# pdf_to_text(r'Gujarati Poems.pdf')