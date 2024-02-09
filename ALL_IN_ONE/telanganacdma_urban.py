from selenium import webdriver
import pandas as pd
import time 
import time, os
from datetime import date
driver = webdriver.Chrome()
database = []
website_1 = r"https://cdma.cgg.gov.in/cdma_arbs/CDMA_PG/PTMenu#"
driver.get(website_1)
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/telanganacdma_urban.xlsx"
path1= f"static/{today}/telanganacdma_urban(e).xlsx"
def telanganacdma():

    time.sleep(3)
    driver.maximize_window()

    driver.find_element_by_xpath('//*[@id="2"]/span/font').click()
    time.sleep(2)

    dis_db = [] 
    dis = driver.find_element_by_xpath('//*[@id="ddldistrict"]')

    dis_db.extend(dis.text.split('\n'))
    # print(dis_db)
    try:  
        for i in range(2,len(dis_db)+1):
            time.sleep(2)
            dis = driver.find_element_by_xpath(f'//*[@id="ddldistrict"]/option[{i}]')
            dis.click()
            time.sleep(2)
            ulb_db = []
            ulb = driver.find_element_by_xpath('//*[@id="ddlCircle"]')
            ulb_db.extend(ulb.text.split('\n'))
            print(ulb_db)
            for j in range(2,len(ulb_db)+1):
                time.sleep(2)
                ulb_1 = driver.find_element_by_xpath(f'//*[@id="ddlCircle"]/option[{j}]')
                ulb_1.click()
                time.sleep(2)
                # print(ulb_1)

                database.append(dis_db[i-1]+'%'+ulb_db[j-1])
                print(dis_db[i-1]+'%'+ulb_db[j-1])

                a = [i.split('%') for i in  database]
            df = pd.DataFrame(a,columns=['District','ulb'])
            df.to_excel(path,index=True,  engine='xlsxwriter')
            print(time.ctime())
    except Exception as e:
        print(str(e))
        # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['District','ULB'])
        df.to_excel(path1,index=True,  engine='xlsxwriter')
telanganacdma()