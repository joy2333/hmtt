import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.mp_base.base_page import BasePage, BaseHandle

# 对象类库层
from utils import DriverUtils, check_channel_option


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 标题
        self.title = (By.CSS_SELECTOR, '[placeholder="文章名称"]')
        # iframe
        self.ari_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 内容
        self.text = (By.CSS_SELECTOR, '#tinymce')
        # 封面
        self.auto = (By.XPATH, '//*[text()="自动"]')
        # 频道选择框
        self.select = (By.CSS_SELECTOR, '[placeholder="请选择"]')
        # 频道选项
        self.channel = (By.XPATH, '//*[text()="c++"]')
        # 发表
        self.publish = (By.XPATH, '//*[text()="发表"]')

    # 找标题
    def find_title(self):
        return self.find_elt(self.title)

    # 找iframe
    def find_iframe(self):
        return self.find_elt(self.ari_iframe)

    # 找内容
    def find_text(self):
        return self.find_elt(self.text)

    # 找封面
    def find_auto(self):
        return self.find_elt(self.auto)

    # 找频道选择框
    def find_select(self):
        return self.find_elt(self.select)

    # 找频道选项
    def find_channel(self):
        return self.find_elt(self.channel)

    # 找发表按钮
    def find_publish(self):
        return self.find_elt(self.publish)


# 操作层
class HandleAri(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 输入标题
    def input_title(self, title):
        self.input_text(self.home_page.find_title(), title)

    # 输入文章内容
    def input_ari_text(self, text):
        DriverUtils.get_mp_driver().switch_to.frame(self.home_page.find_iframe())
        self.input_text(self.home_page.find_text(), text)
        DriverUtils.get_mp_driver().switch_to.default_content()

    # 选择自动
    def input_auto(self):
        time.sleep(1)
        self.home_page.find_auto().click()

    # 选择频道
    def input_channel(self, element):
        check_channel_option(DriverUtils.get_mp_driver(),"请选择",element)
        # 点击频道框
        # self.home_page.find_select().click()
        # # 获取所有频道名称
        # element_list = DriverUtils.get_mp_driver().find_elements_by_css_selector(".el-select-dropdown__item span")
        # # 是否找到的标识
        # is_suc = False
        # for i in element_list:
        #     # 如果找到则点击并返回
        #     if i.text == element:
        #         i.click()
        #         is_suc = True
        #         break
        #     # 找不到则鼠标悬停并按向下的按键
        #     else:
        #         action = ActionChains(DriverUtils.get_mp_driver())
        #         action.move_to_element(i).send_keys(Keys.DOWN).perform()
        #
        # # 始终未找到则抛出异常
        # if is_suc is False:
        #     NoSuchElementException("找不到元素{}".format(element))

    # 点击发布
    def click_publish(self):
        self.home_page.find_publish().click()


# 业务层
class ProxyAri():
    def __init__(self):
        self.handle_ari = HandleAri()

    def test_ari(self, title, text, channel):
        self.handle_ari.input_title(title)
        self.handle_ari.input_ari_text(text)
        self.handle_ari.input_auto()
        self.handle_ari.input_channel(channel)
        self.handle_ari.click_publish()
