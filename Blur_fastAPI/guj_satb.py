from pdf2image import convert_from_path
import pandas as pd
import tesserocr
import os
import time
import re

'''
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


def pdf_to_text(path):
    pdfs = sorted_alphanumeric(os.listdir(path))
    titles = []
    files_guj = []
    files_eng = []
    for pdf in pdfs:
        if (pdf.split('.')[-1]).lower() == 'pdf':
            print(pdf, 'In Process....')
            texts_guj = []
            texts_eng = []
            pdf_path = os.path.join(path,pdf)
            images = convert_from_path(pdf_path,260,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
            for i in range(len(images)):
                text_g = tesserocr.image_to_text(images[i],lang='guj')
                text_e = tesserocr.image_to_text(images[i],lang='eng+guj')
                texts_guj.append(text_g)
                texts_eng.append(text_e)
            titles.append(pdf)
            files_guj.append(texts_guj)
            files_eng.append(texts_eng)
        else:
            continue
    return files_guj,files_eng, titles
'''

def district(lt):
    for i,j in enumerate(lt):
        if 'District' in j or 'જીલ્લો' in j:
            if len(lt[i+1])>2:
                return lt[i+1]
            elif len(lt[i+2])>2:
                return lt[i+2]


def taluka(lt):
    for i,j in enumerate(lt):
        if 'Taluka' in j or 'તાલુકો' in j:
            if len(lt[i+1])>2:
                return lt[i+1], i
            elif len(lt[i+2])>2:
                return lt[i+2], i           
            
def village(lt, iter_ind):
    for i,j in enumerate(lt):
        if 'Village' in j or 'ગામ' in j:
            if len(lt[i+1])>2 and i>iter_ind:
                return lt[i+1]
            elif len(lt[i+2])>2 and i>iter_ind:
                return lt[i+2] 
            
def survey(lt):
    for i,j in enumerate(lt):
        if 'સરવે' in j or 'Survey' in j :
            if len(lt[i+1])>=1:
                return lt[i+1]
            elif len(lt[i+2])>=1:
                return lt[i+2]


def area(lt):
    for i,j in enumerate(lt):
        if 'ક્ષેત્રકળ' in j or 'ચો.મી.' in j or 'ક્ષેત્રફળ' in j or 'ચોમી.' in j:
            if len(lt[i+1])>=1:
                return lt[i+1]
            elif len(lt[i+2])>=1:
                return lt[i+2]


def land_use(lt):
    for i,j in enumerate(lt):
        if 'ઉપયોગ' in j or 'Use' in j :
            if len(lt[i+1])>=1 and 'ખેતર' not in lt[i+1]:
                return lt[i+1]
            elif len(lt[i+2])>=1 and 'ખેતર' not in lt[i+1] and 'Name' not in lt[i+2]:
                return lt[i+2]

def owner(lt):
    own = []
    for i,j in enumerate(lt):
        if 'નોંધ નંબરો તથા ખાતેદાર' in j:
            for k in range(i+1,len(lt)):
                if 'Boja' in lt[k] or 'બોજા' in lt[k]:
                    return own, k
                if len(lt[k])>1:
                    own.append(lt[k])
    return own,i
        
def boja(lt, iter_ind):
    boj = []
    for i,j in enumerate(lt):
        if 'Boja' in j or 'બોજા' in j:
            for k in range(i+1,len(lt)):
                if '* અહીં' in lt[k]:
                    return boj
                if len(lt[k])>1 and k>iter_ind:
                    boj.append(lt[k])                  
    return boj


def pdf_to_text(path):
    texts_guj = []
    #texts_eng = []
    images = convert_from_path(path,260,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    for i in range(len(images)):
        text_g = tesserocr.image_to_text(images[i],lang='guj')
        #text_e = tesserocr.image_to_text(images[i],lang='eng+guj')
        texts_guj.append(text_g)
        #texts_eng.append(text_e)
    #return texts_guj,texts_eng
    return texts_guj

def text_by_line(text):
    text_by_line = []
    for k in text:
        text_by_line.extend(''.join(k).split('\n'))
    return text_by_line

def fields(guj_txt):
    guj= guj_txt
    ow, index = owner(guj)
    return ['','','','',area(guj),'',', '.join(ow),', '.join(boja(guj, index))]

#def fields(guj_txt, eng_txt):
    #pc = []
    #guj, eng = guj_txt, eng_txt
    #ow, index = owner(guj)
    #ta, index1 = taluka(guj)
    #pc.append([district(guj),ta,village(guj, index1),survey(eng),area(guj),land_use(guj),', '.join(ow),', '.join(boja(guj, index))])
    #return pc
    #return [district(guj),ta,village(guj, index1),survey(eng),area(guj),land_use(guj),', '.join(ow),', '.join(boja(guj, index))]

def guj_satbara(path):
    #text_guj, text_eng = pdf_to_text(path)
    text_guj = pdf_to_text(path)
    guj_text = text_by_line(text_guj)
    #eng_text = text_by_line(text_eng)
    #dt = fields(guj_text, eng_text)
    dt = fields(guj_text)
    return dt

#print('Completed')
 














