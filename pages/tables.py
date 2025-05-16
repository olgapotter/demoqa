from components.components import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Tables(BasePage):
    def __init__(self, driver):
        base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, '.modal-content')
        self.btn_delete_row = WebElement(driver, 'span[title="Delete"]', locator_type='css')
        self.edit_btn = WebElement(driver, 'span[title="Edit"]', locator_type='css')
        self.table_rows = WebElement(driver, '.rt-tbody')

        self.no_data = WebElement(driver, 'div.rt-noData', locator_type='css')

        self.input_first_name = WebElement(driver, '#firstName')
        self.input_last_name = WebElement(driver, '#lastName')
        self.input_email = WebElement(driver, '#userEmail')
        self.input_age = WebElement(driver, '#age')
        self.input_salary = WebElement(driver, '#salary')
        self.input_dept = WebElement(driver, '#department')

    def fill_form(self, first, last, email, age, salary, dept):
        self.input_first_name.clear()
        self.input_first_name.send_keys(first)

        self.input_last_name.clear()
        self.input_last_name.send_keys(last)

        self.input_email.clear()
        self.input_email.send_keys(email)

        self.input_age.clear()
        self.input_age.send_keys(age)

        self.input_salary.clear()
        self.input_salary.send_keys(salary)

        self.input_dept.clear()
        self.input_dept.send_keys(dept)

    def delete_all_rows(self):
        from selenium.webdriver.common.by import By
        while True:
            delete_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
            if not delete_buttons:
                break
            delete_buttons[0].click()

    def get_column_headers(self):

        return self.driver.find_elements(By.CSS_SELECTOR, '.rt-th')