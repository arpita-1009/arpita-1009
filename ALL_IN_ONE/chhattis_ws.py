from selenium import webdriver
import pandas as pd
from datetime import time,date
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
driver = webdriver.Chrome(options = chrome_options)
# DataStore
database = []

# chhattisgard Website Url
driver.get("https://revenue.cg.nic.in/bhuiyanuser/User/Selection_Report_For_KhasraDetail.aspx")
#
#
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/Chhattisgarh_Rural.xlsx"
path1= f"static/{today}/Chhattisgarh_Rural(e).xlsx"
#
def excel():
# state extract Dropdown Data here
    dis_db = []
    dis = driver.find_element_by_id('ddlDist')
    dis_db.extend(dis.text.split('\n'))
    print(dis_db)
    try:
        for i in range(2,len(dis_db)):
            time.sleep(2)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="ddlDist"]/option[{i}]')))
            dis1 = driver.find_element_by_xpath(f'//*[@id="ddlDist"]/option[{i}]').text
            driver.find_element_by_xpath(f'//*[@id="ddlDist"]/option[{i}]').click() 
            time.sleep(2)
            dis_db.append(dis1)

                # district extract Dropdown Data here 
            teh_db = []
            tal = driver.find_element_by_id('ddlTehsil')
            teh_db.extend(tal.text.split('\n'))
            time.sleep(2)
            print(teh_db)
            for j in range(2,len(teh_db)):
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="ddlTehsil"]/option[{j}]')))
                tal1 = driver.find_element_by_xpath(f'//*[@id="ddlTehsil"]/option[{j}]').text
                driver.find_element_by_xpath(f'//*[@id="ddlTehsil"]/option[{j}]').click() 
                time.sleep(2)
                teh_db.append(tal1)
        #         #tract Dropdown Data here 
                vil_db = []
                vil = driver.find_element_by_id('ddlGram')
                vil_db.extend(vil.text.split('\n'))
                time.sleep(2)
                print(vil_db)
                for k in range(1,len(vil_db)):
    #                 WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="ddlGram"]/option[{k}]')))
    #                 vil1 = driver.find_element_by_xpath(f'//*[@id="ddlGram"]/option[{k}]').text
                    # vil_db.append(vil1)
                    database.append(dis_db[i-1]+'%'+teh_db[j-1]+'%'+vil_db[k-1])
                    print(dis_db[i-1]+'%'+teh_db[j-1]+'%'+vil_db[k-1])


    #         # # Create DataFrame and DataStore in Excel 
            a = [i.split('%') for i in  database]
            df = pd.DataFrame(a,columns=['District','Taluka','Village'])
            df.to_excel(path,index=True,  engine='xlsxwriter')
    except Exception as e:
        print(str(e))
        # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['state','District','Village'])
        df.to_excel(path1,index=True,  engine='xlsxwriter')
excel()