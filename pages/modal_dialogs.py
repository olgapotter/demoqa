from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)


        self.modal_buttons = WebElement(driver, 'button[id^="show"]')
        self.icon = WebElement(driver, '#app > header > a')