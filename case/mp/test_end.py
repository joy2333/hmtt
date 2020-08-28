import pytest
from utils import DriverUtils


@pytest.mark.run(order=9999)
class Test_begin():
    def test_begin(self):
        DriverUtils.change_mp_key(True)
        DriverUtils.quit_mp_driver()
