import pdfplumber
import pandas as pd
from app import get_date
path = get_date()
file = path[0]
pdf = pdfplumber.open(file)
page = pdf.pages
total_data = []

tax , payable_amount,dry, frz, cool, frz2, rs, whs6, total, weight, cube = '','','','','','','','','','',''
data_list = [tax , payable_amount,dry, frz, cool, frz2, rs, whs6, total, weight, cube]
description = []
category = []
for p in page:
    ts = {"vertical_strategy": "lines","horizontal_strategy": "text","explicit_horizontal_lines": [ min(x["top"] for x in p.edges) ]}
    tables = p.extract_tables(table_settings=ts)
    text = p.extract_text()
    lines = text.split("\n")
    main_data = []
    name = ''
    address = ''
    Phone = ''
    fedid = ''
    del_date = ''
    type = 'INVOICE'
    date = ''
    invoice = ''
    slm = ''
    acc_no = ''
    phone_no = ''
    trim = ''
    stop = ''
    for index,line in enumerate(lines):
        if line == "PERFORMANCE":
            name += lines[0]
            address += lines[1]
            address += lines[3]
            Phone += lines[4]
        if "Fed ID:" in line:
            fedid += line.split("Fed ID:")[1]
        if "Delv Date:" in line:
            del_date += line.split(":")[1]
        if "DATE INVOICE SLM ACCT NO" in line:
            all_data = lines[index + 1]
            date += all_data.split()[0]
            invoice += all_data.split()[1]
            slm += all_data.split()[2]
            acc_no += all_data.split()[3]
        if "COMMERCE WAY" in line:
            phone_no = line.split("COMMERCE WAY L")[1].split()[0]
            trim = line.split("COMMERCE WAY L")[1].split()[1]
            stop = line.split("COMMERCE WAY L")[1].split()[2]

    main_data.append(name+'%'+address+'%'+Phone+'%'+fedid+'%'+del_date+'%'+type+'%'+date+'%'+invoice+'%'+slm+'%'+acc_no+'%'+phone_no+'%'+trim+'%'+stop)

    data1 = []
    for ele in tables[-1]:
        data = list(filter(lambda item: item is not None, ele))
        data1.append(data)

    start_index = None
    for i, row in enumerate(data1):
        if row == ['ORDER', 'SHIP', '', '', '', 'NUMBER', '', '# OF\nRU UN', 'RC\nUN', '', 'X', '', '']:
            start_index = i
            break

    if start_index is not None:
        cleaned_data = data1[start_index:]
    else:
        print("The specified line was not found in the data.")

    for j,ele1 in enumerate(cleaned_data):
        if len(ele1) == 15:
            ele1[6 : 8] = [''.join(ele1[6 : 8])]
        if len(ele1) == 16:
            ele1[6 : 9] = [''.join(ele1[6 : 9])]
        if len(ele1) == 17:
            ele1[6 : 10] = [''.join(ele1[6 : 10])]
        if len(ele1) == 18:
            ele1[6 : 11] = [''.join(ele1[6 : 11])]
        if ele1[-1] == 'PAY THIS':
            end_index = j
            previous_index2 = end_index - 2 
            previous_index3 = end_index - 3
            previous_index4 = end_index - 4
            tax = cleaned_data[previous_index4][-1]
            payable_amount = cleaned_data[previous_index2][1]
            dry = cleaned_data[previous_index3][0]
            frz = cleaned_data[previous_index3][1]
            cool = cleaned_data[previous_index3][2]
            frz2 = cleaned_data[previous_index3][3]
            rs = cleaned_data[previous_index3][4]
            whs6 = cleaned_data[previous_index3][5]
            total = cleaned_data[previous_index3][6]
            weight = cleaned_data[previous_index3][7]
            cube = cleaned_data[previous_index3][8]
            data_list = [tax , payable_amount,dry, frz, cool, frz2, rs, whs6, total, weight, cube]
            del cleaned_data[previous_index4:]

    main_list = []
    for ele2 in cleaned_data:
        if ele2 == ['ORDER', 'SHIP', '', '', '', 'NUMBER', '', '# OF\nRU UN', 'RC\nUN', '', 'X', '', '']:
            pass
        else:
            main_list.append(ele2 + data_list)

    a = [i.split('%') for i in  main_data]   
    
    for i in main_list:
        for ele3 in a:
            total_data.append(ele3 + i)

test_list = []
for j in total_data:
    if j[-1] == '' and j[-2] == '' and j[-3] == ''and j[-4] == ''and j[-5] == ''and j[-6] == ''and j[-7] == ''and j[-8] == ''and j[-9] == ''and j[-10] == '' and j[-11] == 'TAX':
        del j[-11:]
        test_list.append(j + data_list)
    else:
        test_list.append(j)

test_list = test_list[1:-1]
for idx,l in enumerate(test_list):
    if l[13] == '' and l[14] == '' and l[15] == '' and l[16] == '' and l[17] == '' and l[18] == '' and l[19] != '' and l[20] == '' and l[21] == '' and l[22] =='' and l[23] == '' and l[24] == '' and l[25] == '' and l[26] == '':
        if '*' not in l[19]:
            test_list[idx-1][19] = test_list[idx-1][19] + ' ' +test_list[idx][19] 
        else:
            pass
database = []
temp = ''
try:
    for element in test_list:
        if element[17] == '' and element[18] == '':
            if '*' in element[19]:
                temp = element[19]
        if element[17] != '' and element[18] != '':
            if '*' not in element[19]:
                element.insert(19, temp)
                element.insert(20, element[19])
                element.pop(19)
                database.append(element)
except:
    pass

last =[]
for f in database:
    if str(f[15]).isalpha():
        last.append(f)
    else:
        del f

path_1 = path[0].replace('.pdf','.xlsx')
df = pd.DataFrame(last,columns = ['Name','Address','Phone','Fed ID','Del Date','TYPE','DATE','INVOICE','SLM','ACCT NO','PHONE NO','TRIP','STOP','QTY|Order','SHIP','UNIT','SIZE','BRAND','ITEM NUMBER','DESCRIPTION','CATEGORY','RU','UN','RC|UN','  ','TAX','UNIT PRICE','EXTENTSION','TOTAL TAX','PAY THIS AMOUNT','DRY','FRZ','COOL','FRZ2','R/S','WHS6','TOTAL','WEIGHT','CUBE'] )
df.to_excel(path_1, engine='xlsxwriter', index=False)
pdf.close()

def in_def():
    print ( path_1)
    return [path_1]
