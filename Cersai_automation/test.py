from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base64 import b64decode
import os , time ,base64 , cv2

chrome_options = Options()
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.mapsofindia.com/villages/assam/")
time.sleep(4)
database = []
driver.find_element_by_id('stateSelect')
driver.find_element_by_xpath('//*[@id="stateSelect"]/option[5]').click()
dis_db = []
driver.find_element_by_id('districtSelect')
time.sleep(2)
#changes pending for assam english data scrap
dist_1 = driver.find_elements_by_xpath(f'//*[@id="district"]/li/a')
time.sleep(2)
try:

    for i in range(1 ,len(dist_1)):
        time.sleep(2)
        dis = driver.find_element_by_xpath(f'//*[@id="district"]/li[{i}]/a').text
        driver.find_element_by_xpath(f'//*[@id="district"]/li[{i}]/a').click() 
        dis_db.append(dis)
        time.sleep(3)

        tal_db = []
        tal = driver.find_element_by_id('circles')
        time.sleep(2)
        tal_1 = driver.find_elements_by_xpath(f'//*[@id="circles"]/li/a')
        for j in range(1 ,len(tal_1)):
            tal1 = driver.find_element_by_xpath(f'//*[@id="circles"]/li[{j}]/a').text
            driver.find_element_by_xpath(f'//*[@id="circles"]/li[{j}]/a').click() 
            tal_db.append(tal1)
            time.sleep(3)

            vil_db = []
            vil = driver.find_element_by_id('villages')
            time.sleep(2)
            vil_1 = driver.find_elements_by_xpath(f'//*[@id="villages"]/li/a')
            for k in range(1 , len(vil_1)):
                vil1 = driver.find_element_by_xpath(f'//*[@id="villages"]/li[{k}]/a').text
                vil_db.append(vil1)
                database.append(dis_db[i-1]+'%'+tal_db[j-1]+'%'+vil_db[k-1])
                print(dis_db[i-1]+'%'+tal_db[j-1]+'%'+vil_db[k-1])

    a = [i.split('%') for i in  database]
    df = pd.DataFrame(a,columns=['District','circles' ,'Village'])
    df.to_excel('Assam.xlsx',index=True,  engine='xlsxwriter')
      
except Exception as e:
    print(str(e))
    # Create DataFrame and DataStore in Excel 
    a = [i.split('%') for i in  database]
    df = pd.DataFrame(a,columns=['District','circles','Village'])
    df.to_excel('Assam.xlsx',index=True,  engine='xlsxwriter')




