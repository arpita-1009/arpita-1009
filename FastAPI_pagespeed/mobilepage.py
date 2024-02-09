
from selenium import webdriver
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main import upload_file
url = upload_file()
print(url,"***************************************************")
# url = 'www.easyime.com'
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(r"C:\Users\User\Documents\GitHub\chromedriver.exe",options = chrome_options)
driver.refresh()
driver.get("https://pagespeed.web.dev/")

ser = driver.find_element_by_class_name('VfPpkd-fmcmS-wGMbrd')
ser.send_keys(url)
time.sleep(5)
# ana = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div[2]/div/div[2]/form/div[2]/button/span').click()
# vil  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[1]/div[2]/div[1]/div/div/div[2]/label/span[1]')))
# first = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[1]/div[2]/div[1]/div/div/div[2]/label/span[1]').click()
# try:
#     vil  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="performance"]/div[2]/div[1]/label/span[1]')))
#     driver.find_element_by_xpath('//*[@id="performance"]/div[2]/div[1]/label/span[1]').click()  
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="unused-javascript"]/details/summary/div/div/div[2]/div[3]')))
#     driver.find_element_by_xpath('//*[@id="unused-javascript"]/details/summary/div/div/div[2]/div[3]').click()
# except:
#     pass
# try:
        
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="server-response-time"]/details/summary/div/div/div[2]/div[3]')))
#     driver.find_element_by_xpath('//*[@id="server-response-time"]/details/summary/div/div/div[2]/div[3]').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="unused-css-rules"]/details/summary/div/div/div[2]/div[3]')))
#     driver.find_element_by_xpath('//*[@id="unused-css-rules"]/details/summary/div/div/div[2]/div[3]').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="offscreen-images"]/details/summary/div/div/div[2]/div[3]')))
#     driver.find_element_by_xpath('//*[@id="offscreen-images"]/details/summary/div/div/div[2]/div[3]').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="render-blocking-resources"]/details/summary/div/div/div[2]/div[3]')))
#     driver.find_element_by_xpath('//*[@id="render-blocking-resources"]/details/summary/div/div/div[2]/div[3]').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uses-long-cache-ttl"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="uses-long-cache-ttl"]/details/summary/div/div').click()
# except:
#     pass

# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainthread-work-breakdown"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="mainthread-work-breakdown"]/details/summary/div/div').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="critical-request-chains"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="critical-request-chains"]/details/summary/div/div').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resource-summary"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="resource-summary"]/details/summary/div/div').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="largest-contentful-paint-element"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="largest-contentful-paint-element"]/details/summary/div/div').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="first-contentful-paint-3g"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="first-contentful-paint-3g"]/details/summary/div/div').click()
# except:
#     pass

# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-shift-elements"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="layout-shift-elements"]/details/summary/div/div').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="long-tasks"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="long-tasks"]/details/summary/div/div').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="non-composited-animations"]/details/summary/div/div')))
#     driver.find_element_by_xpath('//*[@id="non-composited-animations"]/details/summary/div/div').click()
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div[2]/div/div[2]/div[2]/span[2]/div[2]/button/span')))
#     driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div[2]/div/div[2]/div[2]/span[2]/div[2]/button/span').click()
# except:
#     pass

print("21 pass")
time.sleep(3)
a = driver.execute_cdp_cmd("Page.printToPDF", {"path": 'html-page.pdf', "format": 'A4'})

base = str(a).strip("{'data': '}")
def mobile():
    return base