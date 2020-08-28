import allure
import pytest
from page.mp.login_page import LoginProxy
from utils import DriverUtils, is_element_exist

@pytest.mark.run(order=2)
class TestLogin():
    def setup_class(self):
        # 创建浏览器驱动对象
        self.driver = DriverUtils.get_mp_driver()
        # 创建业务所在类的对象
        self.login_proxy = LoginProxy()

    def teardown_class(self):
        DriverUtils.quit_mp_driver()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        username = "13911111111"
        code = "246810"

        # 调用执行业务方法
        self.login_proxy.test_mp_login(username,code)

        # 断言
        assert is_element_exist(self.driver,"江苏")
