from pages.demoqa import DemoQa
from components.components import WebElement

def test_check_center_text_on_elements_page(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    demo_qa_page.btn_elements.click()

    # Проверка URL
    expected_url = 'https://demoqa.com/elements'
    actual_url = browser.current_url
    assert actual_url == expected_url

    # Проверка текста по центру
    center_text_element = WebElement(browser, '.playground-header div')
    expected_text = 'Please select an item from left to start practice.'
    actual_text = center_text_element.get_text()

    assert actual_text == expected_text