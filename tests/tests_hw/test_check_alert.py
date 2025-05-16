import allure
from pages.alerts import Alerts

@allure.title("Проверка появления алерта через 5 секунд после клика на кнопку Timer Alert")
def test_timer_alert(browser):
    page = Alerts(browser)
    page.visit()

    page.click_timer_alert()
    alert = page.wait_for_alert()
    assert alert is not None
    alert.accept()