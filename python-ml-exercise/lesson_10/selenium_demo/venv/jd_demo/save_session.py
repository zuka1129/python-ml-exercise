from selenium import webdriver
import time
import os
import json

browser = webdriver.Chrome()
#browser.get('https://www.jd.com')
def login():
    browser.get('https://www.jd.com')
    browser.find_element_by_css_selector('#ttbar-login > a.link-login').click()
    browser.find_element_by_link_text('账户登录').click()
    browser.find_element_by_id('loginname').send_keys('15738397655')
    browser.find_element_by_name('nloginpwd').send_keys('951129@ZHOUKAI')
    browser.find_element_by_css_selector('#loginsubmit').click()

    save_cookie(browser)

def save_cookie(browser):
    real_path = os.path.dirname(os.getcwd())
    project_path = '\jd_demo\cookies\\'
    file_path = real_path + project_path
    print(file_path)
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    cookies = browser.get_cookies()
    with open(file_path + 'jd.cookies', 'w') as f:
        json.dump(cookies, f)
    print(cookies)
login()
def get_url_with_cookies():
    #login()
    real_path = os.path.dirname(os.getcwd())
    project_path = '\jd_demo\cookies\\'
    file = real_path + project_path + 'jd.cookies'
    #读取cookies文件
    f = open(file, 'r')
    cookies_line = f.readline()

    cookies_json = json.loads(cookies_line)
    print(cookies_json)
    #清除旧的cookie
    time.sleep(3)
    browser.get('https://www.jd.com')
    browser.delete_all_cookies()
    #将新的cookies写入
    for cookie in cookies_json:
        print(cookie)
        if 'expiry' in cookie:
            del cookie['expiry']
        browser.add_cookie(cookie)
    browser.get('https://order.jd.com/center/list.action')

get_url_with_cookies()