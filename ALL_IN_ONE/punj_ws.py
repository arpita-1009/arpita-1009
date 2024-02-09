
from selenium import webdriver
import pandas as pd
import time, os
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

print(time.ctime())
driver = webdriver.Chrome()

today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/Punjab_Rural.xlsx"
path1= f"static/{today}/Punjab_Rural(e).xlsx"

driver.get("https://jamabandi.punjab.gov.in/")
def excel():

    eng = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/nav/ul/li[2]/div/div[3]/div')))
    dropdown_trigger = driver.find_element_by_xpath('//*[@id="header"]/nav/ul/li[2]/div/div[3]/div').click()
    dropdown_option_1 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="header"]/nav/ul/li[2]/div/div[3]/div/ul/li[1]')))
    dropdown_option_1.click()
    time.sleep(5)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'ContentPlaceHolder1_fsSelectRegion')))
    database = []
    dist_db = []
    dist = driver.find_elements_by_xpath(f'//*[@id="ContentPlaceHolder1_fsSelectRegion"]/div/div[2]/div[1]/div/ul/li')
    try :
        for i in range(2,len(dist)+1):
            dist_1 = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_fsSelectRegion"]/div/div[2]/div[1]/div/ul/li[{i}]').get_attribute('innerHTML')
            element  = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_fsSelectRegion"]/div/div[2]/div[1]/div/ul/li[{i}]')
            driver.execute_script("arguments[0].click();", element)
            dist_db.append(dist_1)
            # print(dist_db,"district")
            time.sleep(2)
            teh_db = []
            tehs = driver.find_element_by_id('ContentPlaceHolder1_ddlTehsil') 
            teh = driver.find_elements_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlTehsil"]/option')
            for l in range(2,len(teh)+1):
                teh_1 = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_fsSelectRegion"]/div/div[2]/div[2]/div/ul/li[{l}]').get_attribute('innerHTML')
                # print(teh_1,"tehsil")
                print("<<<<<<<data _enter function in tehsil>>>>>>>>")
                element1 = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_fsSelectRegion"]/div/div[2]/div[2]/div/ul/li[{l}]')
                driver.execute_script("arguments[0].click();", element1)
                teh_db.append(teh_1)
                time.sleep(1)
                vil_db = []
                village = driver.find_element_by_id('ContentPlaceHolder1_ddlVillage')
                time.sleep(3)
                vil1 = driver.find_elements_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlVillage"]/option')
                for m in range(2,len(vil1)+1):
                    vil2 = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlVillage"]/option[{m}]').get_attribute("innerHTML")
                    print("pass")
                    vil_db.append(vil2)
                    database.append(dist_db[i-2]+'%'+teh_db[l-2]+'%'+vil_db[m-2])
                    print(dist_db[i-2]+'%'+teh_db[l-2]+'%'+vil_db[m-2])

        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['District','Tehsil','Village'])
        df.to_excel(path,index=True,  engine='xlsxwriter')
        
    except Exception as e:
        print(str(e))
        # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['District','Tehsil','Village'])
        df.to_excel(path1,index=True,  engine='xlsxwriter')
excel()        