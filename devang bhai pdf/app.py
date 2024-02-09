import re
from pdf2image import convert_from_path
import tesserocr
file = 'devang bhai pdf/ordaug23.pdf'
images = convert_from_path(file,260)#
base_name = []
print(len(images))
for filename in range(len(images)):
    part = 24
    for size in range(1,part+1):
        print(size,"i m part")
        if size ==1:    
            box =(50,100,730,500)
        if size == 2:
            box =(700,100,1400,500)
        if size ==3:
            box =(1400,100,2090,500)
        if size == 4:
            box =(50,500,730,850)
        if size ==5:
            box =(700,500,1400,850)
        if size == 6:
            box =(1400,500,2090,850)
        if size ==7:
            box =(50,850,730,1200)
        if size == 8:
            box =(700,850,1400,1200)
        if size == 9:
            box =(1400,850,2090,1200)
        if size == 10:
            box =(50,1150,730,1550)
        if size ==11:
            box =(700,1150,1400,1550)
        if size == 12:
            box =(1400,1150,2090,1550)
        if size == 13:
            box =(50,1500,730,1900) 
        if size == 14:
            box =(700,1500,1400,1900)
        if size ==15:
            box =(1400,1500,2090,1900)
        if size == 16:
            box =(50,1850,730,2250)
        if size == 17:
            box =(700,1850,1400,2250)
        if size == 18:
            box =(1400,1850,2090,2250)
        if size ==19:
            box =(50,2200,730,2600)
        if size == 20:
            box =(700,2200,1400,2600)
        if size ==21:
            box =(1400,2200,2090,2600) 
        if size == 22:
            box =(50,2550,730,2950)
        if size ==23:
           box =(700,2550,1400,2950)    
        if size == 24:
            box =(1400,2550,2090,2950) 

        cropped_img = images[filename].crop(box)
        text = tesserocr.image_to_text(cropped_img ,lang='eng')
        finallist1 = text.split()
        print(finallist1,"-------------")
        
        if len(finallist1) < 7 :
            continue
        else:
            mobile_no = re.findall("([0-9]{10})",str(finallist1))
            print(mobile_no)
            if mobile_no == []:
                string1  = str(finallist1[4])+"%"+str(finallist1[5])+"%"+str(finallist1[6])+"%"+"-"+"%"+"-"+"%"+"-"
                base_name.append(string1)
                print(str(finallist1[4]),str(finallist1[5]),str(finallist1[6]))
            elif len(mobile_no) == 1 :
                mobile = str(mobile_no).strip("[]'")
                string1  = str(finallist1[4])+"%"+str(finallist1[5])+"%"+str(finallist1[6])+"%"+mobile+"%"+"-"+"%"+"-"
                base_name.append(string1)
                print(str(finallist1[4]),str(finallist1[5]),str(finallist1[6]),mobile)
            
            elif len(mobile_no) == 2 :
                mobile1 = str(mobile_no[0])
                mobile2 = str(mobile_no[1])
                # mobile12 = str(mobile_no).strip("[]'")
                string1  = str(finallist1[4])+"%"+str(finallist1[5])+"%"+str(finallist1[6])+"%"+mobile1+"%"+mobile2+"%"+"-"
                base_name.append(string1)
                print(str(finallist1[4]),str(finallist1[5]),str(finallist1[6]),mobile1,mobile2)
            else:
                mobile1 = str(mobile_no[0])
                mobile2 = str(mobile_no[1])
                mobile3 = str(mobile_no[2])
                # mobile12 = str(mobile_no).strip("[]'")
                string1  = str(finallist1[4])+"%"+str(finallist1[5])+"%"+str(finallist1[6])+"%"+mobile1+"%"+mobile2+"%"+mobile3
                base_name.append(string1)
                print(str(finallist1[4]),str(finallist1[5]),str(finallist1[6]),mobile1,mobile2,mobile3)
        
print(len(base_name))
import pandas as pd
a = [i.split('%') for i in  base_name]
df = pd.DataFrame(a,columns=['Surname','Firstname','Lastname','mobile_no','op_mobile','2op_mobile'])
df.to_excel('devang bhai pdf/ordaug23.xlsx',index=True,  engine='xlsxwriter')

