from selenium import webdriver
import pandas as pd
from datetime import time,date
import os , time , datetime
driver = webdriver.Chrome()
# DataStore
database = []

# Bihar Website Url
driver.get(r'http://meebhoomi.ap.gov.in/')
# District extract Dropdown Data here
time.sleep(4)
submit = driver.find_element_by_xpath('//*[@id="GetAddangalPage"]')
driver.execute_script("arguments[0].click();", submit)
#
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
    
path= f"static/{today}/Andhra Pradesh_Rural.xlsx"
path1= f"static/{today}/Andhra Pradesh_Rural(e).xlsx"
#
def excel():
    time.sleep(2)
    dis_db = []
    dis = driver.find_element_by_id('dl_district')
    dis_db.extend(dis.text.split('\n'))
    # try:
    print(dis_db,"district")
    for i in range(2,len(dis_db)+1):
        time.sleep(2)
        dis = driver.find_element_by_xpath(f'//*[@id="dl_district"]/option[{i}]')
        dis.click()
        time.sleep(2)

        sub_db = []
        sub = driver.find_element_by_id('dl_mandal')    
        sub_db.extend(sub.text.split('\n'))
        print(sub_db,"mandal")
        for j in range(2,len(sub_db)+1):
            # time.sleep(4)
            sub_1 = driver.find_element_by_xpath(f'//*[@id="dl_mandal"]/option[{j}]')                        
            sub_1.click()
            time.sleep(3)

            rani_db = []
            rani = driver.find_element_by_id('dl_village')
            rani_db.extend(rani.text.split('\n'))
            print(len(rani_db),"length")
            for l in range(2,len(rani_db)+1):
                database.append(dis_db[i-1]+'%'+sub_db[j-1]+'%'+rani_db[l-1])
                print(dis_db[i-1],sub_db[j-1],rani_db[l-1])



    # Create DataFrame and DataStore in Excel 
    a = [i.split('%') for i in  database]
    df = pd.DataFrame(a,columns=['District','Taluka','Village'])
    df.to_excel(path,index=True,  engine='xlsxwriter')
    # except Exception as e:
    #     print(str(e))
    #     # Create DataFrame and DataStore in Excel 
    #     a = [i.split('%') for i in  database]
    #     df = pd.DataFrame(a,columns=['District','Taluka','Village'])
    #     df.to_excel(path1,index=True,  engine='xlsxwriter')
excel()        