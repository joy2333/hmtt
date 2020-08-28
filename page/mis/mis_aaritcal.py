import time
from selenium.webdriver.common.by import By
from base.mis_base.base_page import BasePage, BaseHandle
from utils import check_channel_option, DriverUtils


# 对象库层
class MisAcalPage(BasePage):

    def __init__(self):
        super().__init__()
        # 文章标题搜索输入框
        self.ari_title_box = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 查询按钮
        self.query_btn = (By.CSS_SELECTOR, ".find")
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 驳回按钮
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        # 通过驳回确认按钮
        self.con_rej_btn = (By.CSS_SELECTOR, '.el-button--primary')

    # 找到文章标题搜索输入框
    def find_ari_title_box(self):
        return self.find_elt(self.ari_title_box)

    # 找到查询按钮
    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    # 找到通过按钮
    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    # 找到驳回按钮
    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    # 找到通过确认按钮
    def find_con_rej_btn(self):
        return self.find_elt(self.con_rej_btn)


# 操作层
class MisAtcalHandle(BaseHandle):
    def __init__(self):
        self.mis_atcal_page = MisAcalPage()

    # 文章标题搜索框输入
    def input_ari_title(self, ari_title):
        self.input_text(self.mis_atcal_page.find_ari_title_box(), ari_title)

    # 选中文章状态
    def check_ari_status(self, ari_status):
        check_channel_option(DriverUtils.get_mis_driver(),'请选择', ari_status)

    # 点击查询按钮
    def click_query_btn(self):
        self.mis_atcal_page.find_query_btn().click()

    # 点击通过按钮
    def click_pass_btn(self):
        self.mis_atcal_page.find_pass_btn().click()

    # 点击驳回按钮
    def click_reject_btn(self):
        self.mis_atcal_page.find_reject_btn().click()

    # 点击审核/通过确定按钮
    def click_confim_btn(self):
        self.mis_atcal_page.find_con_rej_btn().click()


class MisAtcalProxy():
    def __init__(self):
        self.mis_at_h1 = MisAtcalHandle()

    # 审核通过测试用例
    def test_aduit_pass(self, ari_title):
        # 输入搜索的文字名称
        self.mis_at_h1.input_ari_title(ari_title)
        # 选中文章状态
        self.mis_at_h1.check_ari_status('待审核')
        # 点击查询按钮
        self.mis_at_h1.click_query_btn()
        time.sleep(2)
        # 点击通过按钮
        self.mis_at_h1.click_pass_btn()
        # 点击提示框的确认按钮
        self.mis_at_h1.click_confim_btn()
        time.sleep(2)
        #  选择文章状态为：审核通过
        self.mis_at_h1.check_ari_status('审核通过')
        # 点击查询按钮
        self.mis_at_h1.click_query_btn()
        time.sleep(3)

    # 审核驳回测试用例
    def test_reject_pass(self, ari_title):
        # 输入搜索的文字名称
        self.mis_at_h1.input_ari_title(ari_title)
        # 选中文章状态
        self.mis_at_h1.check_ari_status('待审核')
        # 点击查询按钮
        self.mis_at_h1.click_query_btn()
        time.sleep(2)
        # 点击驳回按钮
        self.mis_at_h1.click_reject_btn()
        # 点击提示框的确认按钮
        self.mis_at_h1.click_confim_btn()
        time.sleep(2)
        #  选择文章状态为：审核通过
        self.mis_at_h1.check_ari_status('审核失败')
        # 点击查询按钮
        self.mis_at_h1.click_query_btn()
        time.sleep(3)
