import logging
import time
import allure
import pytest
import config
from page.mp.publish_artical_page import ProxyAri
from page.mp.home_page import HomeProxy
from utils import DriverUtils, is_element_exist, get_case_data, get_allure_png


@pytest.mark.run(order=3)
class TestAri():
    def setup_class(self):
        # 创建浏览器驱动对象
        self.driver = DriverUtils.get_mp_driver()
        # 创建业务所在类的对象
        self.home_proxy = HomeProxy()
        self.proxy_ari = ProxyAri()

    def setup(self):
        self.driver.get("http://ttmp.research.itcast.cn/")
        time.sleep(2)

    def teardown_class(self):
        DriverUtils.quit_mp_driver()

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(("title","context","channel","expect"),get_case_data("./data/mp/ari_data.json"))
    def test_ari(self,title,context,channel,expect):
        config.PUB_ARITCAL_TITLE = title
        logging.info('发布的文章标题{}'.format((config.PUB_ARITCAL_TITLE)))
        # 调用前置方法
        self.home_proxy.to_pub_ari_page()

        # 调用执行业务方法
        self.proxy_ari.test_ari(config.PUB_ARITCAL_TITLE,context,channel)

        # 截图
        get_allure_png(self.driver,expect)
        # 断言
        assert is_element_exist(self.driver,expect)
