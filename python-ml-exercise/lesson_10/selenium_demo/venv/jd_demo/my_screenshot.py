from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#打开浏览器
browser = webdriver.Chrome()
browser.get('https://www.jd.com')

elem = browser.find_element_by_link_text('手机')
ActionChains(browser).move_to_element(elem).perform()
time.sleep(2)
browser.find_element_by_link_text('老人机').click()

all_handle = browser.window_handles
print(all_handle)
current_handle = browser.current_window_handle
print(current_handle)
for handle in all_handle:
    if handle != current_handle:
        browser.close()
        browser.switch_to.window(handle)
        browser.save_screenshot('jdlaorenji.png')