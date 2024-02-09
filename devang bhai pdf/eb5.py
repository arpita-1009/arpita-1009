import pdfplumber , re
import pandas as pd
import itertools
file = "IMG_0001_merged (1).pdf"
all_text = ''
mobile_no = []
with pdfplumber.open(file) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        #print(text)
        all_text += '\n' + text
mobile = re.findall("([0-9]{10})",str(all_text))
mobile_no.append(mobile)
cell_no = re.findall("([0-9]{3}-[0-9]{8})",str(all_text))
mobile_no.append(cell_no)
all_mobile = list(itertools.chain(*mobile_no))

a = [i.split('%') for i in  all_mobile]
df = pd.DataFrame(a,columns=['Mobile no'])
df.to_excel('IMG_0001_merged (1).pdf.xlsx',index=True,  engine='xlsxwriter')