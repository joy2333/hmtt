import pytest
from utils import DriverUtils

@pytest.mark.run(order=11)
class Test_begin():
    def test_begin(self):
        DriverUtils.change_mis_key(False)
