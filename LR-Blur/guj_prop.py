from pdf2image import convert_from_path
import pandas as pd
import tesserocr
from appblur import getimage
pdfpath  = getimage()
# pdfpath = "p1.pdf"
print(pdfpath,"i m in guj_sath")

def district(lt):
    """from text data return district"""
    for i,j in enumerate(lt):
        if 'District' in j or 'જીલ્લો' in j:
            if len(lt[i+1])>2:
                return lt[i+1]
            elif len(lt[i+2])>2:
                return lt[i+2]


def survey_o(lt):
    """from text data return city survey office"""
    for i,j in enumerate(lt):
        if 'સીટી સરવે ઓફીસ' in j or 'City Survey Office' in j:
            if len(lt[i+1])>=1:
                return lt[i+1]
            elif len(lt[i+2])>=1:
                return lt[i+2]
            
def ward(lt):
    """from text data return ward"""
    for i,j in enumerate(lt):
        if '(વો્ડ)' in j or 'Ward' in j:
            if len(lt[i+1])>=1:
                return lt[i+1]
            elif len(lt[i+2])>=1:
                return lt[i+2]

def sheetno(lt):
    """from text data return survey no."""
    for i,j in enumerate(lt):
        if 'શીટ નંબર' in j or 'Sheet No' in j:            
            if len(lt[i+1])>=1:
                return lt[i+1]
            elif len(lt[i+2])>=1:
                return lt[i+2]
          
def survey(lt):
    """from text data return survey no."""
    for i,j in enumerate(lt):
        if 'સીટી સરવે નંબર' in j:
            if len(lt[i+1])>=1:
                return lt[i+1]
            elif len(lt[i+2])>=1:
                return lt[i+2]
        
def fp(lt):
    """from text data return fp no."""
    for i,j in enumerate(lt):
        if 'FP' in j:
            if len(lt[i+1])>=1 and 'T' not in lt[i+1]:
                return lt[i+1]
            elif len(lt[i+2])>=1 and 'T' not in lt[i+1] and 'T' not in lt[i+2]:
                return lt[i+2]
            break
        
def tp(lt):
    """from text data return tp no."""
    for i,j in enumerate(lt):
        if 'TP' in j:
            if len(lt[i+1])>=1 and 'Area' not in lt[i+1]:
                return lt[i+1]
            elif len(lt[i+2])>=1 and 'Area' not in lt[i+1] and 'Area' not in lt[i+2]:
                return lt[i+2]
            break

def area(lt):
    """from text data return area"""
    for i,j in enumerate(lt):
        if 'ક્ષેત્રકળ' in j or 'ચો.મી.' in j or 'Area' in j:
            if len(lt[i+1])>=1:
                return lt[i+1]
            elif len(lt[i+2])>=1:
                return lt[i+2]

def land_use(lt):
    """from text data return land use"""
    for i,j in enumerate(lt):
        if 'મિલ્કતનો ઉપયોગ' in j:
            if len(lt[i+1])>=1 and 'વિગત' not in lt[i+1]:
                return lt[i+1]
            elif len(lt[i+2])>=1 and 'વિગત' not in lt[i+1] and 'વિગત' not in lt[i+2]:
                return lt[i+2]
def pdf_date(lt):
    import re
    z = re.findall("[0-9]{2}/[0-9]{2}/[0-9]{4}",str(lt))
    data = str(z[0]).strip("[]'")
    return data
     
def owner(lt):
    """from text data return owner names"""
    own = []
    for i,j in enumerate(lt):
        if ('મુળ ધારણકતાં' in j) or ('મુળ ધારણકર્તા' in j):
            for k in range(i+1,len(lt)):
                if 'નોંધ નંબર' in lt[k]:
                    return own
                if len(lt[k])>1:
                    own.append(lt[k])
    return own

def pdf_to_text(path):
    """from file convert pdf to image and image to text return text data"""
    #print(path)
    # print(tesserocr.get_languages())
    texts_guj = []
    #texts_eng = []
# Convert Pdf to Image
    # os.environ["PATH"]+=os.pathsep+os.path.join(r'\poppler-0.68.0','bin')
    # pop_path = "/Users/rushangipatel/Downloads/Web Driver /usr/local/bin/chromedriver"
    images = convert_from_path(path,260,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    for i in range(len(images)):
        text_g = tesserocr.image_to_text(images[i],lang='guj')
        #text_e = tesserocr.image_to_text(images[i],lang='eng+guj')
        texts_guj.append(text_g)
        #texts_eng.append(text_e)
    return texts_guj
    #return texts_guj,texts_eng

def text_by_line(text):
    """Split Texts Data Line By Line"""
    text_by_line = []
    for k in text:
        text_by_line.extend(''.join(k).split('\n'))
    return text_by_line

# def fields(guj_txt):
#     """takes text data and return in format [District,taluka,village,Survey,Area,land_use,owner,encumbrance]"""
#     guj = guj_txt
#     return ['','','','',area(guj),'',', '.join(owner(guj)),'']

def fields(guj_txt, eng_txt):
    guj, eng = guj_txt, eng_txt
    return [district(guj),survey_o(guj),ward(guj),sheetno(guj),survey(guj+eng),fp(eng),tp(eng),area(guj+eng),', '.join(owner(guj)),pdf_date(eng),land_use(eng)]

def guj_propertycard():
    """Main Function to call sub function Gujarat Property Card Required Extraction Fields - Area, Owner"""
    #text_guj, text_eng = pdf_to_text(path)
    text_guj = pdf_to_text(pdfpath)
    text_eng = pdf_to_text(pdfpath)
    guj_text = text_by_line(text_guj)
    eng_text = text_by_line(text_eng)
    #eng_text = text_by_line(text_eng)
    #dt = fields(guj_text, eng_text)
    dt = fields(guj_text,eng_text)
    print(dt)
    return dt
# guj_propertycard()
'''
dt = main(path)
columns = ['File Name', 'District', 'Survey Office', 'Ward', 'Survey', 'FP NO', 'TP NO', 'Area', 'Land Use', 'Owner']
df = pd.DataFrame(dt, columns=columns)
df.to_excel(output_path,index=False)
print('Completed')
'''
