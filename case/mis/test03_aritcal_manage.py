import pytest

import config
from page.mis.mis_aaritcal import MisAtcalProxy
from page.mis.mis_home_page import MisHomePage
from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist

@pytest.mark.run(order=13)
class TestAritcalMana():
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mis_driver()
        # 登录页面的业务层对象
        self.login_page = MisLoginProxy()
        # 首页的业务层对象
        self.home_page = MisHomePage()
        # 文章审核的业务层对象
        self.ad_page = MisAtcalProxy()

    def teardown_class(self):
        DriverUtils.quit_mis_driver()

    def teardown(self):
        self.driver.get('http://ttmis.research.itcast.cn/#/home')

    # 登录
    # @pytest.mark.run(order=1)
    # def test_login(self):
    #     self.login_page.test_mp_login("testid","testpwd123")

    # 测试审核文章的测试用例
    def test_aduit_ari_pass(self):
        self.home_page.to_aaritcal_page()
        self.ad_page.test_aduit_pass(config.PUB_ARITCAL_TITLE)

        assert is_element_exist(self.driver,"驳回")

    # @pytest.mark.run(order=3)
    # def test_aduit_ari_reject(self):
    #     self.home_page.to_aaritcal_page()
    #     self.ad_page.test_reject_pass("开拔开拔开拔")
    #
    #     assert is_element_exist(self.driver,"驳回")
