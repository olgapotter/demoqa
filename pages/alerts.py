from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.alertButton = WebElement(driver, '#alertButton')
        self.confirmButton = WebElement(driver, '#confirmButton')
        self.confirmResult = WebElement(driver, '#confirmResult')
        self.promptButton = WebElement(driver, '#promptButton')
        self.promptResult = WebElement(driver, '#promptResult')
        self.timerAlertButton = WebElement(driver, '#timerAlertButton')

    def click_timer_alert(self):
        self.timerAlertButton.click()

    def wait_for_alert(self, timeout=7):
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
