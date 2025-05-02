from pages.demoqa import DemoQa
from components.components import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_check_center_text_on_elements_page(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    demo_qa_page.btn_elements.click()

    # Проверка URL
    expected_url = 'https://demoqa.com/elements'
    actual_url = browser.current_url
    assert actual_url == expected_url

    # Ждём появления текста по центру
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.playgound-body .col-md-6'))
    )

    # Проверка текста по центру
    center_text_element = WebElement(browser, '.playgound-body .col-md-6')
    expected_text = 'Please select an item from left to start practice.'
    actual_text = center_text_element.get_text()

    assert actual_text == expected_text

    def test_page_elements(browser):
        el_page = ElementsPage(browser)

        el_page.visit()
        assert el_page.text.elements.get.text() == 'Please select an item from left to start practice.'