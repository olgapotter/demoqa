from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.automation_practice_form import PracticeForm


def test_login_form_validation(browser):
    form = PracticeForm(browser)
    form.visit()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "firstName")))

    # дальше уже можно делать проверки
    assert form.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form.email.get_dom_attribute('placeholder') == 'name@example.com'

    expected_pattern = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    assert form.email.get_dom_attribute('pattern') == expected_pattern