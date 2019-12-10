from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# browser = webdriver.Chrome()
# browser.get('https://www.jd.com')
#
# browser.find_element_by_id('key').send_keys('电脑')
# time.sleep(2)
# browser.find_element_by_class_name('button').click()

browser = webdriver.Chrome()
browser.get('https://www.jd.com')

action = browser.find_element_by_id('key')
action.send_keys('学习机')
time.sleep(2)
action.send_keys(Keys.RETURN)

# browser.find_element_by_id('key').send_keys('电脑')
# time.sleep(2)
# browser.find_element_by_class_name('button').click()

# browser = webdriver.Chrome()
# browser.get('https://www.jd.com')
# browser.find_element_by_xpath('//*[@id="key"]')
# time.sleep(1)
# browser.find_element_by_class_name('button').click()
# time.sleep(2)
# browser.close()

# browser = webdriver.Chrome()
# browser.get('https://www.jd.com')
# browser.find_element_by_css_selector('#key').send_keys('电脑')
# time.sleep(1)
# browser.find_element_by_class_name('button').click()
#browser.close()
# mouse = browser.find_element_by_link_text('手机')
# time.sleep(2)
# mouse.click()




