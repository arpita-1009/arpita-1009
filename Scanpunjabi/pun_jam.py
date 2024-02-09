from pdf2image import convert_from_path
# import pdfplumber
# import pandas as pd
import tesserocr

path = r"C:\Users\darsh\Desktop\ESMSYSWork\Punjab\Jamabandi2.pdf"
images = convert_from_path(path,260,poppler_path=r'C:\Users\darsh\Desktop\ESMSYSWork\poppler-22.01.0\Library\bin',fmt = 'jpg')

# # def text_by_line(text):
# #     """Split Texts Data Line By Line"""
# #     text_by_line = []
# #     for k in text:
# #         text_by_line.extend(''.join(k).split('\n'))
# #     return text_by_line

# # pdf = pdfplumber.open(path)
# # table = pdf.pages[0].extract_table()
# # # print(table)

# # def filter_table_contents(text_list):
# #     for words_list in text_list:
# #         for words in words_list:
# #             try:
# #                 if '\n' in words:
# #                     words = words.replace('\n','  ')
# #             except:
# #                 pass
# #     return text_list

# # print(filter_table_contents(table))

# def pdf_to_text(path):
#     """from file convert pdf to image and image to text return text data"""
#     texts_tam = [] 
#     #texts_eng = []
#     # Convert Pdf to Image
#     images = convert_from_path(path,260,poppler_path=r'C:\Users\darsh\Desktop\ESMSYSWork\poppler-22.01.0\Library\bin')
#     with tesserocr.PyTessBaseAPI(path=r'C:\Program Files\Tesseract-OCR\tessdata') as api:
#         print
#         api.GetAvailableLanguages()
#     # Image To text
#     for i in range(len(images)):
#         text_g = tesserocr.image_to_text(images[i],lang='pan')
#         #text_e = tesserocr.image_to_text(images[i],lang='eng+guj')
#         texts_tam.append(text_g) 
#         #texts_eng.append(text_e)
#     return texts_tam 

# # print(pdf_to_text(path))

# # -----------
# from pdf2image import convert_from_path
# import cv2
# import numpy as np
# import tesserocr
# from PIL import Image
# import os 

# def show(img):
#     cv2.imshow("winname",cv2.resize(img, (int(img.shape[1]/6), int(img.shape[0]/6))))
#     cv2.waitKey()
#     cv2.destroyAllWindows()

# images = convert_from_path(path,520,poppler_path=r'C:\Users\darsh\Desktop\ESMSYSWork\poppler-22.01.0\Library\bin')
# img1 = np.array(images[0])
# img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# img_bin = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
# img_bin = 255-img_bin

# # img_et = cv2.imread(r"C:\Users\darsh\Desktop\ESMSYSWork\kar_rtc.jpg")

# show(img_bin)
# # ----------------
# # import camelot as cam
# # import pandas as pd
# # table = cam.read_pdf(path,pages='1',flavor='stream',backend="poppler")
# # print(table[0].df)


# -------------------------

    # img = Image.open(path) #Open image using jpg path
    #box - left,upper,right,lower
# box = (740,500,1365,2850) # Name box location ------------------> Jambandi5
# box = (740,650,1365,2000)

# box = (2100,500,2470,2450) Area box location -------------------> 

# box = (2620,500,3700,2900) Encumbarance <-------------------
    # Crooping part based on box location from main image
# cropped_img = images[1].crop(box) # images[0]---> First-Page 
# cropped_img.show()

# images[0].show()

# text= tesserocr.image_to_text(cropped_img,lang ='pan+eng')
# print(text)

# output = ""

# for i in range(len(images)):
#     cropped_img = images[i].crop(box)
#     text= tesserocr.image_to_text(cropped_img,lang ='pan+eng')
#     output += text + "\n"

# print(output.replace('\n\n', '\n').replace('ਕਿਸੇ ਕਾਨੂੰਨੀ ਕੰਮ ਆਦਿ ਲਈ ਵਰਤਿਆ ਨਹੀਂ ਜਾ ਸਕਦਾ | ਪ੍ਰਮਾਣਿਤ ਫਰਦ ਜਾਰ', ''))

def getEnc():
    global images

    box = (2620,500,3700,2900)

    output = ""

    for i in range(len(images)):
        cropped_img = images[i].crop(box)
        text= tesserocr.image_to_text(cropped_img,lang ='pan+eng')
        output += text + "\n"
    
    return(output.replace('\n\n', '\n').replace('ਕਿਸੇ ਕਾਨੂੰਨੀ ਕੰਮ ਆਦਿ ਲਈ ਵਰਤਿਆ ਨਹੀਂ ਜਾ ਸਕਦਾ | ਪ੍ਰਮਾਣਿਤ ਫਰਦ ਜਾਰ', ''))


print(getEnc())