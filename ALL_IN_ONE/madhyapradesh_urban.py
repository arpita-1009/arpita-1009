import time
import pandas as pd
import time, os
from datetime import date

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

# Assuming you have set up the driver

driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://mpenagarpalika.gov.in:8005/sap/bc/webdynpro/sap/zpt_existing_down#")
today = date.today()
delete_fol=os.path.join(os.getcwd(),'static', str(today))
from os.path import exists
if exists(delete_fol):
    pass
else:
    os.makedirs(delete_fol, exist_ok=True)
path= f"static/{today}/madhyapradesh_urban.xlsx"
path1= f"static/{today}/madhyapradesh_urban(e).xlsx"
def madhyapradesh():


    # Click on the button to retrieve data
    time.sleep(5)
    button = driver.find_element_by_xpath('//*[@id="WD28-btn"]')
    button.click()

    # Wait for the data to load
    time.sleep(2)

    # Find the table that contains the data
    table = driver.find_element_by_xpath('//*[@id="WD29-tab"]/tbody')
    rows = table.find_elements_by_tag_name("tr")
    print(len(rows))
    # Iterate through the rows and retrieve the city data
    city_data = []
    for row in rows:
        cells = row.find_elements_by_tag_name("td")
        # time.sleep(1)
        if len(cells) > 0:
            city_data.append([cells[0].text])

    # Print the city data
    for city in city_data:
        print(city)
        
    df = pd.DataFrame(city_data,columns=['CITY'])
    df.to_excel(path,index=True,  engine='xlsxwriter')

    # Close the browser
    driver.quit()
madhyapradesh()
