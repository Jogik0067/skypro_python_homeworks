from lesson_7v1.Mag.MainModul import MainMag
from lesson_7v1.Mag.mag_sells import all_sells


def test_mag(chrome_browser):
    mag = MainMag(chrome_browser)
    mag.auto_vhod()
    mag.sell_item()
    mag.pay_item()
    
    assert mag.total_buy() == all_sells