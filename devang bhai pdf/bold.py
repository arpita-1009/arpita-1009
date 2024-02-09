from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
file = 'aprilmonthord.pdf'
bold_txt=[]
for page_layout in extract_pages(file):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                for character in text_line:
                    if isinstance(character, LTChar):
                        if 'Bold' in character.fontname:
                            bold_txt.append(text_line)

len_bold = len(bold_txt)
name_ext =[]
for i in range(0,len_bold):
    data = str(bold_txt[i])
    data1 = data.strip()
    data2 = data.split()
    if len(data2) == 5 :
        name = data1.split()[2].split("'")[1]
        name1 = data1.split()[3]
        name2 = data1.split()[4].strip("\n'>")
        name3 = name+'%'+name1+'%'+name2
        name_ext.append(name3)
    elif len(data2) == 4:
        name = data1.split()[2].split("'")[1]
        name1 = data1.split()[3].strip("\n'>")
        name3 = name+'%'+name1+'%'+"-"
        name_ext.append(name3)
    elif len(data2) == 3:
        name = data1.split()[2].split("'")[1]
        name3 = name+'%'+"-"+'%'+"-"
        name_ext.append(name3)
    elif len(data2)==6:
        name = data1.split()[2].split("'")[1]
        name1 = data1.split()[3]
        name2 = data1.split()[4]
        name4  = data1.split()[5].strip("\n'>")
        name3 = name+'%'+name1+'%'+name2+name4
        name_ext.append(name3)
    else:
        print(data1)


res = []
for i in name_ext:
    if i not in res:
        res.append(i)

print(len(res))

