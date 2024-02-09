from selenium import webdriver
import pandas as pd
import time, os
from datetime import date

import time
import time 
print(time.ctime())
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
driver = webdriver.Chrome(options = chrome_options)
database = []

driver.get("https://anyror.gujarat.gov.in/emilkat/GeneralReport_IDB.aspx")
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/gujarat_urban.xlsx"
path1= f"static/{today}/gujarat_urban(e).xlsx"
def gujarat():

    drop = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddl_app"]/option[2]').click()
    time.sleep(3)
    # state extract Dropdown Data here
    dis_db = [] 
    dis = driver.find_element_by_id('ContentPlaceHolder1_ddldistrict')

    dis_db.extend(dis.text.split('\n'))
    print(dis_db)
    try:  
        for i in range(2,len(dis_db)+1):
            time.sleep(2)
            dis = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_ddldistrict"]/option[{i}]')
            dis.click()
            time.sleep(2)
            city_sur_db = []
            teh = driver.find_element_by_id('ContentPlaceHolder1_ddlcsoffice')
            city_sur_db.extend(teh.text.split('\n'))
            print(city_sur_db)
            for j in range(2,len(city_sur_db)+1):
                time.sleep(2)
                teh_1 = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlcsoffice"]/option[{j}]')
                teh_1.click()
                time.sleep(2)
                ward_db = []
                rani = driver.find_element_by_id('ContentPlaceHolder1_ddlward')
                ward_db.extend(rani.text.split('\n'))
                for l in range(2,len(ward_db)+1):
                    database.append(dis_db[i-1]+'%'+city_sur_db[j-1]+'%'+ward_db[l-1])
                    print(dis_db[i-1]+'  %  '+city_sur_db[j-1]+'  %  '+ward_db[l-1])

            a = [i.split('%') for i in  database]
            df = pd.DataFrame(a,columns=['District','City Survey Office','Ward'])
            df.to_excel(path,index=True,  engine='xlsxwriter')
            print(time.ctime())
    except Exception as e:
        print(str(e))
        # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['District','City Survey Office','Ward'])
        df.to_excel(path1,index=True,  engine='xlsxwriter')
        print(time.ctime())
       
       
gujarat()