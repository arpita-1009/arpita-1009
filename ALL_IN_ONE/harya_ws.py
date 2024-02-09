from selenium import webdriver
import pandas as pd
from datetime import time,date
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #To Save Excel
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


driver = webdriver.Chrome(options = chrome_options)

database = []
driver.get(r'https://jamabandi.nic.in/land%20records/NakalRecord.aspx')
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/Haryana_Rural.xlsx"
path1= f"static/{today}/Haryana_Rural(e).xlsx"

# state extract Dropdown Data here
def excel():
    dis_db = []
    dis = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddldname')
    dis_db.extend(dis.text.split('\n'))
    # print(dis_db)
    try:
        for i in range(2,len(dis_db)+1):
            time.sleep(2)
            dis = driver.find_element_by_xpath(f'//*[@id="ctl00_ContentPlaceHolder1_ddldname"]/option[{i}]')
            dis.click()
            # print(dis)
            teh_db = []
            teh = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddltname')
            teh_db.extend(teh.text.split('\n'))
            # print(teh_db)
            for j in range(2,len(teh_db)+1):
                time.sleep(2)
                teh_1 = driver.find_element_by_xpath(f'//*[@id="ctl00_ContentPlaceHolder1_ddltname"]/option[{j}]')
                teh_1.click()
                vil_db = []
                vil = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlvname')
                vil_db.extend(vil.text.split('\n'))
                for k in range(2,len(vil_db)+1):

                    database.append(dis_db[i-1]+'%'+teh_db[j-1]+'%'+vil_db[k-1])
                    print(dis_db[i-1]+'%'+teh_db[j-1]+'%'+vil_db[k-1])

        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['District','tehsil' ,'Village'])
        df.to_excel(path,index=True,  engine='xlsxwriter')
        
    except Exception as e:
        print(str(e))
        # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['District','tehsil','Village'])
        df.to_excel(path1,index=True,  engine='xlsxwriter')
excel()        