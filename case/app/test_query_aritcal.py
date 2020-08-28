import unittest

from parameterized import parameterized

from page.app.index_page import IndexProxy
from utils import DriverUtils, is_el_by_attribute, is_element_exist


class TestQueryAcitcal(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtils.get_app_driver()
        cls.index_proxy = IndexProxy()

    def setUp(self) -> None:
        self.driver.start_activity("com.itcast.toutiaoApp",".MainActivity")

    @parameterized.expand(['python','linux'])
    def test_qy_aritcal(self,channel_name):
        self.index_proxy.test_qari_by_channel(channel_name)
        self.assertTrue(is_el_by_attribute(self.driver, 'text', '关注'))

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_app_driver()
