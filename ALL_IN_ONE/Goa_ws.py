from selenium import webdriver
import pandas as pd
import time, os
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


driver = webdriver.Chrome()

# DataStore
database = []

# Bihar Website Url
driver.get(r'https://dslr.goa.gov.in/f114new.aspx')
#
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/Goa_Rural.xlsx"
path1= f"static/{today}/Goa_Rural(e).xlsx"
#
def excel():
    # District extract Dropdown Data here
    tal_db = []
    tal = driver.find_element_by_id('ContentPlaceHolder1_DDtaluka')
    tal_db.extend(tal.text.split('\n'))
    try:
        for i in range(2,len(tal_db)+1):
            time.sleep(5)
            dis = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_DDtaluka"]/option[{i}]')
            dis.click()
            wait = WebDriverWait(driver, 60)
            element = wait.until(EC.element_to_be_clickable((By.ID, 'ContentPlaceHolder1_DDVillage')))

            vil_db = []
            time.sleep(3)
            vil = driver.find_element_by_id('ContentPlaceHolder1_DDVillage')
            vil_db.extend(vil.text.split('\n'))
            for j in range(2,len(vil_db)+1):
                # time.sleep(5)
                # teh_1 = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlVillage"]/option[{j}]')
                # teh_1.click()s
                database.append(tal_db[i-1]+'%'+vil_db[j-1])
                print(tal_db[i-1]+'%'+vil_db[j-1])


            # # Create DataFrame and DataStore in Excel 
            a = [i.split('%') for i in  database]
            df = pd.DataFrame(a,columns=['Taluka','Village'])
            df.to_excel(path,index=True,  engine='xlsxwriter')
            print(time.ctime())
            
    except Exception as e:
        print(str(e))
        # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['Taluk','Village'])
        df.to_excel(path1,index=True,  engine='xlsxwriter')
        print(time.ctime())


excel()
# from app import master_data
# master_da