import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.tables import Tables

@allure.title("CRUD тест для WebTables")
def test_webtables_crud(browser):
    page = Tables(browser)
    page.visit()

    page.delete_all_rows()

    page.btn_add.click()
    assert page.modal_dialog.exist()

    page.btn_submit.click()
    assert page.modal_dialog.exist()

    test_data = {
        "first": "Olga",
        "last": "Ivanova",
        "email": "olga@example.com",
        "age": "28",
        "salary": "7000",
        "dept": "QA"
    }
    page.fill_form(**test_data)

    page.btn_submit.click()
    WebDriverWait(browser, 5).until(
        EC.invisibility_of_element((By.CSS_SELECTOR, '.modal-content'))
    )
    assert test_data["first"] in page.table_rows.get_text()

    page.edit_btn.click()
    assert page.modal_dialog.exist()
    assert page.input_first_name.get_dom_attribute("value") == test_data["first"]

    new_name = "Olya"
    page.input_first_name.clear()
    page.input_first_name.send_keys(new_name)
    page.btn_submit.click()
    WebDriverWait(browser, 5).until(
        EC.invisibility_of_element((By.CSS_SELECTOR, '.modal-content'))
    )
    assert new_name in page.table_rows.get_text()

    page.btn_delete_row.click()
    WebDriverWait(browser, 5).until(
        lambda d: new_name not in page.table_rows.get_text()
    )