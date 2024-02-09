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
driver.get("https://www.cersai.org.in")
time.sleep(4)
data = driver.find_element_by_xpath('//*[@id="ps-dropdown"]').click()
data1 = driver.find_element_by_xpath('//*[@id="preloginMenu"]/li[4]/div/a[1]').click()
time.sleep(3)

drop = driver.find_element_by_xpath('//*[@id="assetCategory"]')
drop.send_keys('I')
time.sleep(1)
drop1 = driver.find_element_by_xpath('//*[@id="assetType"]')
drop1.send_keys('R')
sur_no = driver.find_element_by_xpath('//*[@id="Survey Number"]')
sur_no.send_keys('1-1-36')
plot_no = driver.find_element_by_xpath('//*[@id="Plot Number"]')
plot_no.send_keys('80/300')
house_no = driver.find_element_by_xpath('//*[@id="House / Flat Number"]')
house_no.send_keys('80/300')
floor_no = driver.find_element_by_xpath('//*[@id="Floor No"]')
floor_no.send_keys('1')
build_no = driver.find_element_by_xpath('//*[@id="Building Number"]')
build_no.send_keys('EASTERN SIDE B M ROAD B M ROAD')
nameofproject = driver.find_element_by_xpath('//*[@id="Name of the Project"]')
nameofproject.send_keys('Arpita')
street_no = driver.find_element_by_xpath('//*[@id="Street Number"]')
street_no.send_keys('B M ROAD B M ROAD')
pocket= driver.find_element_by_xpath('//*[@id="Pocket"]')
pocket.send_keys('NAGAMANGALA')
locality= driver.find_element_by_xpath('//*[@id="Locality / Sector"]')
locality.send_keys('NAGAMANGALA NAGAMANGALA')
state= driver.find_element_by_xpath('//*[@id="immovableAssetAddress state"]')
state.send_keys('k')
# state.send_keys('g')
district = driver.find_element_by_xpath('//*[@id="immovableAssetAddress districtName"]')
district.send_keys('Mandya')
city_town= driver.find_element_by_xpath('//*[@id="immovableAssetAddress citytown"]')
city_town.send_keys('Mandya')
pincode= driver.find_element_by_xpath('//*[@id="immovableAssetAddress pincode"]')
pincode.send_keys('571432')

chance_captcha = 0
while chance_captcha <= 4:
    img_captcha_base64 = driver.execute_async_script("""
        var ele = arguments[0], callback = arguments[1];
        ele.addEventListener('load', function fn(){ele.removeEventListener('load', fn, false);
        var cnv = document.createElement('canvas');
        cnv.width = 200; cnv.height = 55;
        cnv.getContext('2d').drawImage(this, 0, 0);
        callback(cnv.toDataURL('image/jpeg').substring(22));}, false);ele.dispatchEvent(new Event('load'));
        """, driver.find_element_by_xpath('//*[@id="assetSearchInputDetails"]/form/div[3]/div[1]/div[2]/img'))

    with open(r"cersai_captcha.jpg", 'wb') as f:
        f.write(base64.b64decode(img_captcha_base64))

    import pytesseract
    path = f'cersai_captcha.jpg'
    img = cv2.imread(path)
    config = ('-l eng --oem 1 --psm 3')
    text_captcha = pytesseract.image_to_string(img, config=config)
    print(text_captcha)
    # time.sleep(10)
    # txt = driver.find_element_by_xpath('//*[@id="jcaptcha"]').click()
    # from selenium.webdriver.common.action_chains import ActionChains
    # actions = ActionChains(driver) 
    # actions.send_keys(Keys.TAB*3)
    # actions.send_keys(text_captcha)
    # # actions.perform()
    
                
    # submit = driver.find_element_by_xpath('//*[@id="assetSearchInputDetails"]/form/div[4]/button')
    # # submit.send_keys(Keys.ENTER)
    # driver.execute_script("arguments[0].click();", submit)
    time.sleep(2)
    try:
        if driver.find_element_by_class_name('custom_alert_box'):
            driver.find_element_by_xpath('//*[@id="assetSearchInputData"]/div[4]/div/section/div/button').click()
            chance_captcha = chance_captcha + 1
        else:
            os.remove('cersai_captcha.jpg')
            break
    except:
        os.remove('cersai_captcha.jpg')
        break
wait = WebDriverWait(driver, 30)
driver.current_window_handle
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="referenceConf"]/div/div[5]/div/input')))
driver.find_element_by_xpath('//*[@id="referenceConf"]/div/div[5]/div/input').click()
button = driver.find_element_by_xpath('//*[@id="referenceConf"]/div/div[6]/button[1]').click()
wait = WebDriverWait(driver, 10)
driver.current_window_handle
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkoutmodal"]/div')))

point  = driver.find_element_by_xpath('//*[@id="option_cards"]').click()
time.sleep(2)
# cvv = '695'
# card_number ='4160210101973884'
# date = '07/24'
# name ='Arpita'

element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="paymethod-newCards"]/div/ul/li/div/div[1]')))
card_no = driver.find_element_by_xpath('//*[@id="paymethod-newCards"]/div/ul/li/div/div[1]/div/input')
card_no.send_keys('4160210101973884')
dates = driver.find_element_by_xpath('//*[@id="paymethod-newCards"]/div/ul/li/div/div[2]/div/input')
dates.send_keys('0724')
name = driver.find_element_by_xpath('//*[@id="paymethod-newCards"]/div/ul/li/div/div[3]/div/input')
name.send_keys('Arpita Patel')
cvv = driver.find_element_by_xpath('//*[@id="paymethod-newCards"]/div/ul/li/div/div[4]/div/input')
cvv.send_keys('695')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="paymethod-newCards"]/div/ul/li/div/div[1]/div/input').click()
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver) 
actions.send_keys(Keys.TAB*1).perform()
actions.send_keys(Keys.TAB*1).perform()
actions.send_keys(Keys.ENTER).perform()
# actions.perform()
# driver.find_element_by_class_name('checkout_btn').click()
# sub_1 = driver.find_element_by_id('btnCards_Submit').click()
# sub = driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/div[12]/div/div[2]/button')
# driver.execute_script("arguments[0].click();", sub_1)
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[0])