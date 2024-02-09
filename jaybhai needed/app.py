from ast import Break
from cgitb import text
from dataclasses import dataclass
from pdf2image import convert_from_path
import pandas as pd
import tesserocr
import glob
# import os.path
folder_path =r'G:\Solanki Ghanshyam singh - 2022-10-06\Solanki Ghanshyam singh - 2022-10-06 Part_1'
file_type = "/*.pdf"
files = glob.glob(folder_path + file_type)
# print(files,"files")

database =[]
date =[]
sur = []
for file in files:
    print(file)
    images = convert_from_path(file,260,poppler_path=r'C:\Users\Arpita Patel\Documents\GitHub\poppler-0.68.0\bin')
    # print(images)
    for i in range(len(images)):
        text_g = tesserocr.image_to_text(images[i],lang='guj')
        guj = str(text_g).split()

        # print(guj)
        for index,line in enumerate(guj):
            print(index , line)
            if 'તા.' in line:
                # print(line)
                date.append(line)
                # database.append(line.strip(''))
            if 'નંબર)' in line:
                
                print(line[162])
                # break
                sur.append(line)
        database.append(str(date)+"%"+str(sur))
    break

# import pandas as pd
# a = [i.split('%') for i in  database]
# df = pd.DataFrame(a,columns=['Date','sr_no'])
# df.to_excel('extract.xlsx',index=True,  engine='xlsxwriter')

