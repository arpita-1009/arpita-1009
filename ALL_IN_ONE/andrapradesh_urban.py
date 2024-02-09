from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import time, os
from datetime import date

driver = webdriver.Chrome()
driver.get('https://cdma.ap.gov.in/en/ptpayments')
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/Andhra Pradesh_urban.xlsx"
path1= f"static/{today}/Andhra Pradesh_urban(e).xlsx"
def andrapradesh():

    time.sleep(2)
    
    district_dropdown = Select(driver.find_element_by_xpath('//*[@id="ulbreports"]/div[1]/select'))
    
    data = []
    
    for district_option in district_dropdown.options:
        district_1 = district_option.text
        municipality_dropdown = Select(driver.find_element_by_xpath('//*[@id="ulbreports"]/div[1]/div[2]/select'))
        for municipality_option in municipality_dropdown.options:
            if municipality_option.get_attribute("data-district") == district_1:
                selected_municipality = municipality_option.get_attribute("value")
                data.append([district_1, selected_municipality])
                print([district_1, selected_municipality])
    
    df = pd.DataFrame(data, columns=['District', 'Municipality'])
    df.to_excel(path, index=False)
    
    driver.quit()
andrapradesh()
