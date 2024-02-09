from selenium import webdriver
import pandas as pd
import time 
import time, os
from datetime import date
driver = webdriver.Chrome()
database = []
website_1 = r"https://ghmc.gov.in/eodb_revenue/Search.aspx"
driver.get(website_1)
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/telangana_urban.xlsx"
path1= f"static/{today}/telangana_urban(e).xlsx"
def telangana():

    time.sleep(3)

    cir_db = []
    tal = driver.find_element_by_id('ContentPlaceHolder1_ddlcircle')
    cir_db.extend(tal.text.split('\n'))

    print(cir_db)

    for i in range(2,len(cir_db)+1):
        
        database.append(cir_db[i-1])
        print(cir_db[i-1])

        # # Create DataFrame and DataStore in Excel 
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['circle'])
        df.to_excel(path,index=True,  engine='xlsxwriter')
telangana()