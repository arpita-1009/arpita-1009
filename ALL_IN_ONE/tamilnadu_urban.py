from selenium import webdriver
import pandas as pd
import time 
import time, os
from datetime import date


print(time.ctime())
driver = webdriver.Chrome()
# DataStore
database = []

website_1 = r"https://clip.tn.gov.in/clip/index.html"
driver.get(website_1)
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/tamilnadu_urban.xlsx"
path1= f"static/{today}/tamilnadu_urban(e).xlsx"
def tamilnadu():

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="dvlandMain2"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="dvlandSub2"]/div[1]/a').click()
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    dis_db = [] 
    dis = driver.find_element_by_id('udist')
    dis_db.extend(dis.text.split('\n'))
    try:
        for i in range(2,len(dis_db)+1):
            time.sleep(1)
            dis = driver.find_element_by_xpath(f'//*[@id="udist"]/option[{i}]')
            dis.click()
            time.sleep(2)
            teh_db = []
   
            teh = driver.find_element_by_id('utaluk')
            teh_db.extend(teh.text.split('\n'))
            for j in range(2,len(teh_db)+1):
                time.sleep(1)
                teh_1 = driver.find_element_by_xpath(f'//*[@id="utaluk"]/option[{j}]')
                teh_1.click()
                time.sleep(1)
                rani_db = []
                rani = driver.find_element_by_id('town')
                rani_db.extend(rani.text.split('\n'))
                for l in range(2,len(rani_db)+1):
                    time.sleep(2)
                    teh_1 = driver.find_element_by_xpath(f'//*[@id="town"]/option[{l}]')
                    teh_1.click()
                    time.sleep(2)

                    ward_db = []
                    ward1 = driver.find_element_by_id('ward')
                    ward_db.extend(ward1.text.split('\n'))
                    for k in range(2,len(ward_db)+1):
                        
                        print(dis_db[i-1] , teh_db[j-1],rani_db[l-1],ward_db[k-1])
                        database.append(dis_db[i-1]+'%'+teh_db[j-1]+'%'+rani_db[l-1]+'%'+ward_db[k-1])

        # # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['District','Taluka','Town','Ward'])
        df.to_excel(path,index=True,  engine='xlsxwriter')

    except:
        pass
tamilnadu()

