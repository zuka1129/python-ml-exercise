from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://list.jd.com/list.html?cat=670,671,672&ev=exbrand%5F5821&page=1&sort=sort_totalsales15_desc&trans=1&JL=4_2_0#J_main')
#WebDriverWait(driver, 20, 0.5)表示最长等待20秒， 每0.5秒刷新一次
#EC.presence_of_element_located（）表示要查找元素的条件，接收元祖
elem = WebDriverWait(driver, 20, 0.5).\
    until(EC.presence_of_element_located((By.XPATH,'//*[@id="plist"]/ul/li[2]/div/div[1]/a/img')))

elem.click()