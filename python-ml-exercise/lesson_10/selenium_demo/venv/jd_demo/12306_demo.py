from selenium import webdriver
import time

def inquire():
    driver = webdriver.Chrome()
    driver.get('https://www.12306.cn')
    start = driver.find_element_by_id('fromStationText')
    start.click()
    time.sleep(1)
    start.send_keys('白河县')
    time.sleep(1)
    driver.find_element_by_class_name('citylineover').click()
    target = driver.find_element_by_id('toStationText')
    target.click()
    time.sleep(1)
    target.send_keys('郑州')
    time.sleep(1)
    driver.find_element_by_class_name('citylineover').click()
    time.sleep(1)
    js = '$("input[id=train_date]").removeAttr("readonly")'
    driver.execute_script(js)
    date = driver.find_element_by_id('train_date')
    date.click()
    date.clear()
    date.send_keys('2019-12-19')
    time.sleep(1)
    driver.find_element_by_class_name('form-label').click()
    time.sleep(1)
    driver.find_element_by_id('search_one').click()

inquire()