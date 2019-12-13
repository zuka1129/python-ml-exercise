# import os.path as op
# import os
# print(op.basename(os.getcwd()))
# print(op.curdir)
# print(op.abspath(op.curdir))

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://item.jd.com/100005724680.html')
spacification_infos = driver.find_elements_by_class_name('Ptable-item')
print(len(spacification_infos))