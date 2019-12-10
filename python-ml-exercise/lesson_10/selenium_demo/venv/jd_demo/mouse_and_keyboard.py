from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get('https://www.jd.com')

elem = browser.find_element_by_link_text('手机')
ActionChains(browser).move_to_element(elem).perform()

time.sleep(2)

browser.find_element_by_link_text('对讲机').click()