from selenium import webdriver
import pandas as pd
from datetime import time,date
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #To Save Excel
import time
driver = webdriver.Chrome()
# DataStore
database = []

# chhattisgard Website Url
driver.get("https://himbhoomilmk.nic.in/viewlandrecords.aspx")
#
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/Himachal Pradesh_Rural.xlsx"
path1= f"static/{today}/Himachal Pradesh_Rural(e).xlsx"
# state extract Dropdown Data here
def excel():
    dis_db = []
    dis = driver.find_element_by_id('ctl00_ContentPlaceHolder1_cmbdistrict')
    dis_db.extend(dis.text.split('\n'))
    try:
        for i in range(2,len(dis_db)):
            time.sleep(2)
            dis = driver.find_element_by_xpath(f'//*[@id="ctl00_ContentPlaceHolder1_cmbdistrict"]/option[{i}]')
            dis.click()
            wait = WebDriverWait(driver, 180)
            # c = driver.find_element_by_id('ctl00_ContentPlaceHolder1_cmbtehsil')
            # wait.until(EC.staleness_of(c))

            # district extract Dropdown Data here 
            teh_db = []
            teh = driver.find_element_by_id('ctl00_ContentPlaceHolder1_cmbtehsil')
            teh_db.extend(teh.text.split('\n'))
            for j in range(2,len(teh_db)):
                time.sleep(4)
                teh_1 = driver.find_element_by_xpath(f'//*[@id="ctl00_ContentPlaceHolder1_cmbtehsil"]/option[{j}]')
                teh_1.click()
                # print(teh_1,"options tehsil")
                wait = WebDriverWait(driver, 180)
                # a = driver.find_element_by_id('ctl00_ContentPlaceHolder1_cmbvillage')
                # wait.until(EC.staleness_of(a))

                # Village extract Dropdown Data here 
                vil = driver.find_element_by_id('ctl00_ContentPlaceHolder1_cmbvillage')
                vil_db = []
                vil_db.extend(vil.text.split('\n'))
                for k in range(1,len(vil_db)+1):
                    # time.sleep(2)
                    # d3 = driver.find_element_by_xpath(f'//*[@id="ddlGram"]/option[{k}]')
                    # d3.click()
                    # wait = WebDriverWait(driver, 180)
            # DataAppend in DataFrame
                    database.append(dis_db[i-1]+'%'+teh_db[j-1]+'%'+vil_db[k-1])
                    print(dis_db[i-1]+'%'+teh_db[j-1]+'%'+vil_db[k-1])


            # # Create DataFrame and DataStore in Excel 
            a = [i.split('%') for i in  database]
            df = pd.DataFrame(a,columns=['state','District','Village'])
            df.to_excel(path,index=True,  engine='xlsxwriter')
    except Exception as e:
        print(str(e))
        # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['state','District','Village'])
        df.to_excel(path1,index=True,  engine='xlsxwriter')
               
excel()        