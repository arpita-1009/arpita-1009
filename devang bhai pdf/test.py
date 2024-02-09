import re
from pdf2image import convert_from_path
import tesserocr ,cv2 , pytesseract
file = 'Binder1.pdf'
images = convert_from_path(file,260)#
base_name = []
print(len(images))
# for filename in range(len(images)):
part = 10
for i in range(1,part+1):
    # if i == 1:
    #     box = (100, 300, 1600, 550)# (left, top, right, bottom))
    # if i == 2:
    #     box = (100,550,1600, 800)
    if i == 3:
        box = (100,800,1600, 1150)
    cropped_img = images[0].crop(box)
    cropped_img.save('myimage_cropped.jpg')



        
    # cropped_img = images[0].crop(box)

    # text = tesserocr.image_to_text(cropped_img ,lang='eng')
    # finallist1 = text.split()
    # print(finallist1,"-------------------------------")
    # mobile_no = re.findall("([0-9]{10})",str(finallist1))
    # print(mobile_no)