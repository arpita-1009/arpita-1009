from pdf2image import convert_from_path
import pdfplumber 
import pandas as pd

"""header part done"""
pdf = pdfplumber.open('Report (7).pdf')
page = pdf.pages[0]
text = page.extract_text()
print(text)
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

a = [i.split('%') for i in  main_data]
df = pd.DataFrame(a,columns=['Name','Address','Phone','Fed ID','Del Date','TYPE','DATE','INVOICE','SLM','ACCT NO','PHONE NO','TRIP','STOP'])
df.to_excel('Report (7).xlsx',index=True,  engine='xlsxwriter')