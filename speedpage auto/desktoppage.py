from requests import delete
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from speedpage import upload_file
# print(upload_file())
# url = upload_file()
url = "www.esmsys.com"
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(r"C:\Users\Arpita Patel\Documents\GitHub\chromedriver.exe",options = chrome_options)
driver.refresh()
driver.get("https://pagespeed.web.dev/")
ser = driver.find_element_by_name('url')

ser.send_keys(url)
time.sleep(5)
ana = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div[2]/div/div[2]/form/div[2]/button/span').click()
vil  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop_tab"]/span[2]')))
driver.find_element_by_xpath('//*[@id="desktop_tab"]/span[2]').click()

# """no data"""
# try:
#     vil  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div[2]/div/div[2]/div[3]/div/div[3]/span/div/c-wiz/div/div/div[1]/div[2]/div[1]/div/div/div[2]/label/span[1]')))
#     button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div[2]/div/div[2]/div[3]/div/div[3]/span/div/c-wiz/div/div/div[1]/div[2]/div[1]/div/div/div[2]/label/span[1]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="performance"]/div[2]/div[1]/label')))
#     button = driver.find_element_by_xpath('//*[@id="performance"]/div[2]/div[1]/label')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="server-response-time"]/details/summary/div/div/div[1]')))
#     button = driver.find_element_by_xpath('//*[@id="server-response-time"]/details/summary/div/div/div[1]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="unused-javascript"]/details/summary/div/div/div[1]')))
#     button = driver.find_element_by_xpath('//*[@id="unused-javascript"]/details/summary/div/div/div[1]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="unused-css-rules"]/details/summary/div/div/div[1]')))
#     button = driver.find_element_by_xpath('//*[@id="unused-css-rules"]/details/summary/div/div/div[1]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="render-blocking-resources"]/details/summary/div/div/div[1]')))
#     button = driver.find_element_by_xpath('/html/body/c-wiz[2]/div[2]/div/div[2]/div[3]/div/div[3]/span/div/c-wiz/div/div/div[2]/div[2]/div/div/article/div/div[2]/div[2]/div/div/div[5]/div[4]/details/summary/div/div/div[1]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uses-long-cache-ttl"]/details/summary/div')))
#     button = driver.find_element_by_xpath('//*[@id="uses-long-cache-ttl"]/details/summary/div/span[2]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="critical-request-chains"]/details/summary/div')))
#     button = driver.find_element_by_xpath('//*[@id="critical-request-chains"]/details/summary/div')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     # button = driver.find_element_by_xpath('//*[@id="critical-request-chains"]/details/summary/div/div').click()
#     pass
# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resource-summary"]/details/summary/div/span[2]')))
#     button = driver.find_element_by_xpath('//*[@id="resource-summary"]/details/summary/div/span[2]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass

# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="largest-contentful-paint-element"]/details/summary/div/span[2]')))
#     button = driver.find_element_by_xpath('//*[@id="largest-contentful-paint-element"]/details/summary/div/span[2]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-shift-elements"]/details/summary/div/span[2]')))
#     button = driver.find_element_by_xpath('//*[@id="layout-shift-elements"]/details/summary/div/span[2]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass
# try:
#     vil  = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="non-composited-animations"]/details/summary/div/span[2]')))
#     button =driver.find_element_by_xpath('//*[@id="non-composited-animations"]/details/summary/div/span[2]')
#     driver.execute_script("arguments[0].click();",button)
# except:
#     pass


print("Xpath flow done")
time.sleep(3)
a = driver.execute_cdp_cmd("Page.printToPDF", {"path": 'html-page.pdf', "format": 'A4'})
print(a)
base = str(a).strip("{'data': '}")
def desktop():
    return base
