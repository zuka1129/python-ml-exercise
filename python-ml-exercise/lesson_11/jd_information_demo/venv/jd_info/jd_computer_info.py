from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import os


def get_jd_info():
    driver = webdriver.Chrome()
    driver.get('https://www.jd.com')
    computer = driver.find_element_by_link_text('电脑')
    ActionChains(driver).move_to_element(computer).perform()
    time.sleep(1)
    driver.find_element_by_link_text('笔记本').click()

    #切换句柄
    handles = driver.window_handles
    current_handle = driver.current_window_handle
    #切换到所有笔记本页面
    for handle in handles:
        if handle != current_handle:
            driver.switch_to_window(handle)
    #点击戴尔标签
    driver.find_element_by_xpath('//*[@id="brand-5821"]/a').click()
    #点击销量第一的电脑
    driver.find_element_by_xpath('//*[@id="plist"]/ul/li[1]/div/div[1]/a/img').click()
    #切换到最新的句柄
    notebook_handle = driver.current_window_handle
    new_handles = driver.window_handles
    font_handles = [current_handle, notebook_handle]
    for handle in new_handles:
        if handle not in font_handles:
            driver.switch_to_window(handle)
    #执行js滑动鼠标直至看到商品介绍
    driver.execute_script('$(window.scrollTo(0, 1500))')
    time.sleep(2)
    #点击规格和参数
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[2]').click()
    # 定义一个存放所有信息的列表
    all_info = []

    #拿到规格信息所在标签
    time.sleep(2)
    spacification_infos = driver.find_elements_by_class_name('Ptable-item')
    #迭代出含有规格信息的所有标签
    for info in spacification_infos:
        #解析标签获得文本内容（字典格式）
        spacification_info = analyse_info(info)
        #追加入列表
        all_info.append(spacification_info)
    #拿到包装信息所在标签，取到文本
    packaging_info = driver.find_element_by_class_name('package-list')
    packaging_key = packaging_info.find_element_by_tag_name('h3').text
    packaging_value = packaging_info.find_element_by_tag_name('p').text
    #将包装信息封装成字典格式数据
    packaging = {}
    packaging[packaging_key] = packaging_value
    #追加至所有信息列表里
    all_info.append(packaging)
    return all_info

#解析标签获取文本信息
def analyse_info(info):
    h3 = info.find_element_by_tag_name('h3')
    dt = info.find_elements_by_tag_name('dt')
    dd = info.find_elements_by_xpath('dl//dd[not(@*)]')
    #定义一个空字典，key为第一列信息，value为后两列信息
    dict1 = {}
    #定义一个空字典，key为第二列信息，value为最后列信息
    dict2 = {}
    for i in range(len(dt)):
        dict2[dt[i].text] = dd[i].text
    dict1[h3.text] = dict2
    return dict1
#存储文本信息
def save_jd_info():
    info_list = get_jd_info()
    path = os.path.abspath(os.path.curdir)
    file_path = path + '\\goods_info\\'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open(file_path + 'computer.infos', 'a', encoding='utf-8') as f:
        f.write(str(info_list))
        print(str(info_list))

if __name__ == '__main__':
    save_jd_info()