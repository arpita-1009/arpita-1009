import pdfplumber
import pandas as pd
pdf = pdfplumber.open("Report-7.pdf")
page = pdf.pages
total_data = []
for p in page:
    ts = {"vertical_strategy": "lines","horizontal_strategy": "text","explicit_horizontal_lines": [ min(x["top"] for x in p.edges) ]}
    tables = p.extract_tables(table_settings=ts)
    page = pdf.pages[0]
    text = page.extract_text()
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
    print(main_data)

    data1 = []
    for ele in tables[-1]:
        data = list(filter(lambda item: item is not None, ele))
        data1.append(data)
    print(data1)
    start_index = None
    for i, row in enumerate(data1):
        if row == ['ORDER', 'SHIP', '', '', '', 'NUMBER', '', '# OF\nRU UN', 'RC\nUN', '', 'X', '', '']:
            start_index = i
            break

    if start_index is not None:
        cleaned_data = data1[start_index:]
    else:
        print("The specified line was not found in the data.")

    description = []
    category = []
    for j,ele1 in enumerate(cleaned_data):
        try:
            if '*' in ele1[6]:
                temp = ele1[6]
                print(temp)
                description.append(ele1[6])
            else:
                category.append(ele1[6])
        except:
            pass
        if len(ele1) == 15:
            ele1[6 : 8] = [''.join(ele1[6 : 8])]
        if len(ele1) == 16:
            ele1[6 : 9] = [''.join(ele1[6 : 9])]
        if len(ele1) == 17:
            ele1[6 : 10] = [''.join(ele1[6 : 10])]
        if len(ele1) == 18:
            ele1[6 : 11] = [''.join(ele1[6 : 11])]
        if ele1[0] == 'DRY FRZ COOL FRZ2 R/S WHS6 TOTAL WEIGHT CUBE':
            end_index = j
            end_index1 = end_index + 1 
            end_index2 = end_index + 2
            end_index3 = end_index + 3
            tax = cleaned_data[end_index1][2]
            payable_amount = cleaned_data[end_index3][1]
            dry = cleaned_data[end_index2][0]
            frz = cleaned_data[end_index2][1]
            cool = cleaned_data[end_index2][2]
            frz2 = cleaned_data[end_index2][3]
            rs = cleaned_data[end_index2][4]
            whs6 = cleaned_data[end_index2][5]
            total = cleaned_data[end_index2][6]
            weight = cleaned_data[end_index2][7]
            cube = cleaned_data[end_index2][8]
            data_list = [tax , payable_amount,dry, frz, cool, frz2, rs, whs6, total, weight, cube]
            del cleaned_data[end_index:]


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

df = pd.DataFrame(total_data,columns = ['Name','Address','Phone','Fed ID','Del Date','TYPE','DATE','INVOICE','SLM','ACCT NO','PHONE NO','TRIP','STOP','QTY|Order','SHIP','UNIT','SIZE','BRAND','ITEM NUMBER','DESCRIPTION','RU','UN','RC|UN','  ','TAX','UNIT PRICE','EXTENTSION','TOTAL TAX','PAY THIS AMOUNT','DRY','FRZ','COOL','FRZ2','R/S','WHS6','TOTAL','WEIGHT','CUBE'] )
df.to_excel('Report-7.xlsx', engine='xlsxwriter', index=False)
