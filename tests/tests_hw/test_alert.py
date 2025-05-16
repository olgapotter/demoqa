from pages.alerts import Alerts
import time

def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert()

def test_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.alertButton.click()
    assert alert_page.alert().text == 'You clicked a button'

    alert_page.alert().acept()
    assert not alert_page.alert()

def test_confirm(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.confirmResult.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirmResult.get_test() == 'You select Cansel'
