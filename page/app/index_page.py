import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.app_base.base_page import BasePage
from utils import DriverUtils


# 对象库层
class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 频道元素对象
        self.channel_option = (By.XPATH, '//*[contains(@text,"{}")]')
        # 频道选项区域元素对象
        self.channel_area = (By.XPATH, '//android.widget.HorizontalScrollView')
        # 第一条文章的元素对象
        self.first_aritcle = (By.XPATH, '//*[contains(@text,"评论")]')

    # 找到频道元素对象
    def find_channel_option(self, channel_name):
        # return self.find_elt(self.channel_option)
        # self.channel_option = (self.channel_option[0],self.channel_option[1].format(channel_name))
        # return self.find_elt(self.channel_option)
        return DriverUtils.get_app_driver().find_element(self.channel_option[0],self.channel_option[1].format(channel_name))

    # 找到频道选项区域元素对象
    def find_channel_area(self):
        return self.find_elt(self.channel_area)

    # 找到第一条文章的元素对象
    def find_first_aritcle(self):
        return self.find_elt(self.first_aritcle)


# 操作层
class IndexHandle:
    def __init__(self):
        self.index_page = IndexPage()

    # 选中频道
    def check_channel_option(self, channel_name):
        # 获取区域元素的所在位置
        area_element = self.index_page.find_channel_area()
        x = area_element.location["x"]
        y = area_element.location["y"]

        # 获取区域元素的大小
        w = area_element.size["width"]
        h = area_element.size["height"]

        # 计算按住的起始位置
        start_x = x + w * 0.5
        start_y = y + h * 0.5

        # 计算按住的结束位置
        end_x = x + w * 0.2
        end_y = start_y

        while True:
            # 获取界面的全部信息：page_source
            page_old = DriverUtils.get_app_driver().page_source
            # 在当前区域中查找我们所想选择的频道元素对象
            try:
                # 如果能找到则点击
                self.index_page.find_channel_option(channel_name).click()
                break
                # 如果找不到则再次滑动页面
            except Exception as e:
                DriverUtils.get_app_driver().swipe(start_x, start_y, end_x, end_y,3000)
                time.sleep(2)
                # 再获取一次界面信息和滑动前的相等
                page_new = DriverUtils.get_app_driver().page_source
                # .如果滑动之后的页面信息和滑动之前的相等则抛出异常没找到目标的选项
                if page_new == page_old:
                    raise NoSuchElementException('没有找到频道')

    # 点击第一条文章
    def check_first_aritcle(self):
        self.index_page.find_first_aritcle().click()


# 业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 根据频道查询文章的方法
    def test_qari_by_channel(self, channel_name):
        # 选择频道
        self.index_handle.check_channel_option(channel_name)
        time.sleep(3)
        # 点击第一条文章
        self.index_handle.check_first_aritcle()
