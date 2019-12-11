from selenium import webdriver
import time

def search_12306():
    driver = webdriver.Chrome()
    driver.get("https://www.12306.cn/index/")
    from_element = driver.find_element_by_id("fromStationText")
    time.sleep(2)
    from_element.click()
    time.sleep(2)
    from_element.send_keys("北京")
    time.sleep(2)
    driver.find_element_by_xpath("//*[text()='北京北']").click()

    to_element = driver.find_element_by_id("toStationText")
    time.sleep(2)
    to_element.click()
    time.sleep(2)
    to_element.send_keys("长春")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='citem_0']").click()
    js = "$('input[id=train_date]').removeAttr('readonly')"
    driver.execute_script(js)
    date_element = driver.find_element_by_id("train_date")
    time.sleep(2)
    date_element.click()
    time.sleep(2)
    date_element.clear()
    date_element.send_keys("2019-06-01")
    time.sleep(2)
    driver.find_element_by_class_name("form-label").click()
    time.sleep(2)
    driver.find_element_by_id("search_one").click()
search_12306()
