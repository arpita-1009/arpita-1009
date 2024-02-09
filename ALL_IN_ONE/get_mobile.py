# from appp import get_date
# path = get_date()
# file = path[0]

# print(file,"****************")

# def excel_no():
#     return file
import pandas as pd
import openpyxl ,re
workbook = openpyxl.load_workbook("All_in_one/GDMA Data.xlsx")
sheet = workbook.worksheets[0]
names = []
for column in sheet.iter_cols():
    column_name = column[0].value
    if column_name == "Executive":
        for cell in column:
            names.append(cell.value)
print(names)
number = []
for i in range(len(names)-1):
    if names[i] != 'Executive':
        c_name = names[i].split()[0]+' '+names[i].split()[1]+' '+names[i].split()[2]
        x = re.findall("[0-9]{10}", names[i])
        y = re.findall("[0-9]{5} [0-9]{5}", names[i])
        if len(x) == 1 and len(y)==1:
            number.append(c_name+'%'+x[0]+'%'+y[0]+'%'+'')
        if len(x) == 0 and len(y)==0:
            number.append(c_name+'%'+''+'%'+''+'%'+'')
        if len(x)==2 and len(y) == 0:
            number.append(c_name+'%'+x[0]+'%'+x[1]+'%'+'')
        if len(x)==0 and len(y) == 2:
            number.append(c_name+'%'+y[0]+'%'+y[1]+'%'+'')
        if len(x)==1 and len(y) == 0:
            number.append(c_name+'%'+x[0]+'%'+''+'%'+'')
        if len(x)==0 and len(y) == 1:
            number.append(c_name+'%'+y[0]+'%'+''+'%'+'')
    else:
        pass

print(number)
a = [i.split('%') for i in  number]
df = pd.DataFrame(a,columns=['Name','Mobile1','Mobile2','Mobile3'])
df.to_excel('extract_mobile.xlsx',index=True,  engine='xlsxwriter')