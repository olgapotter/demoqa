from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')

        self.small_modal_title = WebElement(driver, '#example-modal-sizes-title-sm')
        self.large_modal_title = WebElement(driver, '#example-modal-sizes-title-lg')

        self.close_small_modal = WebElement(driver, '#closeSmallModal')
        self.close_large_modal = WebElement(driver, '#closeLargeModal')