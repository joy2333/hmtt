from selenium.webdriver.common.by import By
from base.mis_base.base_page import BasePage, BaseHandle
from utils import DriverUtils


class MisLoginPage(BasePage):
    def __init__(self):
        super().__init__()

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.ID, "inp1")

    def find_username(self):
        return self.find_elt(self.username)

    def find_password(self):
        return self.find_elt(self.password)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


class MisLoginHandle(BaseHandle):
    def __init__(self):
        self.mis_login_page = MisLoginPage()

    def input_username(self, username):
        self.input_text(self.mis_login_page.find_username(), username)

    def input_password(self, password):
        self.input_text(self.mis_login_page.find_password(), password)

    def click_login_btn(self):
        js_str = "document.getElementById('inp1').removeAttribute('disabled')"
        DriverUtils.get_mis_driver().execute_script(js_str)
        self.mis_login_page.find_login_btn().click()


class MisLoginProxy():
    def __init__(self):
        self.mis_login_handle = MisLoginHandle()

    def test_mp_login(self,username,password):
        self.mis_login_handle.input_username(username)
        self.mis_login_handle.input_password(password)
        self.mis_login_handle.click_login_btn()
