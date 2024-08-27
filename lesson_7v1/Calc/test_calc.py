from lesson_7v1.Calc.MainModul import CalcPage

def test_calculation(chrome_browser):
    calcut = CalcPage(chrome_browser)
    calcut.wait_rel()
    calcut.click_act()

    assert "15" in calcut.result_w()
