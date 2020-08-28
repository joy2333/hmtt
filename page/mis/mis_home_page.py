from selenium.webdriver.common.by import By
from base.mis_base.base_page import BasePage, BaseHandle


class MisHomePage(BasePage, BaseHandle):
    def __init__(self):
        super().__init__()
        self.info_mange_tab = (By.XPATH, "//*[contains(text(),'信息管理')]")
        self.context_mange_tab = (By.XPATH, "//*[contains(text(),'内容审核')]")

    def to_aaritcal_page(self):
        self.find_elt(self.info_mange_tab).click()
        self.find_elt(self.context_mange_tab).click()
