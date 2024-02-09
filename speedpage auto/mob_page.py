from selenium import webdriver
import time , os , shutil
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://pagespeed.web.dev/')

url = driver.find_element_by_xpath('//*[@id="i2"]')
url.send_keys('www.easyime.com')

analyse = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div[2]/div/div[2]/form/div[2]/button/span').click()

diagnose =  WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div[2]/div/div[2]/div[3]/div/div[2]/span/div/c-wiz/div/div/div[2]/div[2]')))

driver.find_element_by_xpath('//*[@id="unused-javascript"]/details/summary/div/div/div[2]/div[3]').click()
driver.find_element_by_xpath('//*[@id="render-blocking-resources"]/details/summary/div/div/div[2]/div[3]').click()