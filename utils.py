import json
import logging
import time

import allure
import selenium.webdriver
import appium.webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


# 定义浏览器驱动的工具类-自定义
class DriverUtils:
    # 自媒体驱动对象私有属性
    __mp_driver = None
    # 后台管理系统
    __mis_driver = None
    # APP
    __app_driver = None

    # mp浏览器驱动开关
    __mp_key = True

    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            # 创建浏览器驱动对象 --> 打开浏览器
            cls.__mp_driver = selenium.webdriver.Firefox()
            # cls.__mp_driver.maximize_window()  # 窗口最大化
            cls.__mp_driver.implicitly_wait(15)  # 隐式等待
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    # 自媒体-关闭浏览器驱动的方法
    @classmethod
    def quit_mp_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__mp_driver is not None and cls.__mp_key:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__mp_driver.quit()
            # 将__driver设置为空
            cls.__mp_driver = None

    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    # mis浏览器驱动开关
    __mis_key = True

    # 后台管理系统获取驱动对象得方法
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            # 创建浏览器驱动对象 --> 打开浏览器
            cls.__mis_driver = selenium.webdriver.Firefox()
            # cls.__mis_driver.maximize_window()  # 窗口最大化
            cls.__mis_driver.implicitly_wait(15)  # 隐式等待
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    # 后台管理系统-关闭浏览器驱动的方法
    @classmethod
    def quit_mis_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__mis_driver is not None and cls.__mis_key:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__mis_driver.quit()
            # 将__driver设置为空
            cls.__mis_driver = None

    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    # app系统获取驱动对象得方法
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
            desired_caps['appActivity'] = '.MainActivity'
            # 保持登录
            desired_caps['noReset'] = True
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    # 后台管理系统-关闭浏览器驱动的方法
    @classmethod
    def quit_app_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__app_driver is not None:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__app_driver.quit()
            # 将__driver设置为空
            cls.__app_driver = None


def is_element_exist(driver, text):
    xpath = '//*[contains(text(),"{}")]'.format(text)
    try:
        return WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_xpath(xpath))
    except Exception as e:
        logging.error(NoSuchElementException("找不到文本为{}的元素对象".format(text)))
        return False


def is_el_by_attribute(driver, attr_name, attr_value):
    xpath = '//*[contains(@{},"{}")]'.format(attr_name, attr_value)
    try:
        return WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_xpath(xpath))
    except Exception as e:
        NoSuchElementException("找不到属性{}为{}的元素对象".format(attr_name, attr_value))
        return False


def check_channel_option(driver, chang_name, element):
    str_xpath = "//*[contains(@placeholder,'{}')]".format(chang_name)
    driver.find_element_by_xpath(str_xpath).click()
    element_list = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    is_suc = False
    for i in element_list:
        # 如果找到则点击并返回
        if i.text == element:
            i.click()
            is_suc = True
            break
        # 找不到则鼠标悬停并按向下的按键
        else:
            action = ActionChains(driver)
            action.move_to_element(i).send_keys(Keys.DOWN).perform()

    # 始终未找到则抛出异常
    if is_suc is False:
        NoSuchElementException("找不到元素{}".format(element))


# 封装读取数据并组装成parameteriz所要求数据格式函数
def get_case_data(file_path):
    # 定义一个空列表
    test_data = []
    # 1.读取数据文件中的数据
    with open(file=file_path, encoding="utf-8")as f:
        str_dict = json.load(f)
        # 2.遍历所有的键值
        for i in str_dict.values():
            # 3.一次性获取键值所有键值,并且把返回的结果直接追加到空列表中
            test_data.append(list(i.values()))
            print(test_data)
    return test_data


def get_allure_png(driver, filename):
    allure.attach(driver.get_screenshot_as_png(), filename, allure.attachment_type.PNG)
