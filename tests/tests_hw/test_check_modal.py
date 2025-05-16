import time
import allure
from pages.modal_dialogs import ModalDialogs

@allure.title("Проверка Small и Large модальных окон")
def test_modal_dialogs(browser):
    page = ModalDialogs(browser)
    page.visit()

    assert page.btn_small_modal.exist()
    assert page.btn_large_modal.exist()

    page.btn_small_modal.click()
    time.sleep(1)
    assert page.small_modal_title.exist()
    page.close_small_modal.click()
    time.sleep(1)
    assert not page.small_modal_title.exist()

    page.btn_large_modal.click()
    time.sleep(1)
    assert page.large_modal_title.exist()
    page.close_large_modal.click()
    time.sleep(1)
    assert not page.large_modal_title.exist()
