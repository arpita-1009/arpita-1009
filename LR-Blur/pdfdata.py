from pdf2image import convert_from_path
import pandas as pd
import tesserocr



def pdf_to_text(path):
    texts_guj = []
    #texts_eng = []
    images = convert_from_path(path,260,poppler_path=r'C:\Users\Arpita Patel\Documents\GitHub\poppler-0.68.0\bin')
    for i in range(len(images)):
        text_g = tesserocr.image_to_text(images[i],lang='guj')
        #text_e = tesserocr.image_to_text(images[i],lang='eng+guj')
        texts_guj.append(text_g)
        #texts_eng.append(text_e)
    #return texts_guj,texts_eng
    return texts_guj

# def text_by_line(text):
#     text_by_line = []
#     for k in text:
#         text_by_line.extend(''.join(k).split('\n'))
#     return text_by_line


def guj_satbara(path):
    # text_guj, text_eng = pdf_to_text(path)
    text_guj = pdf_to_text(path)
    
    print(text_guj)
    return text_guj

#print('Completed')

if __name__ == '__main__':
    guj_satbara(r'C:\Users\Arpita Patel\Documents\GitHub\General\LR-Blur\અમદાવાદ_વિરમગામ_હાંસલપુર-(શે.) - 026_609_10-9-2022.png.pdf')