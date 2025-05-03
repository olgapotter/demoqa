from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    # Проверяем количество кнопок модальных окон
    buttons = modal_page.modal_buttons.find_elements()
    assert len(buttons) == 2

    def test_navigation_modal(browser):
        modal_page = ModalDialogs(browser)
        demoqa_page = DemoQa(browser)

        # Переход на страницу модальных окон
        modal_page.visit()

        # Обновить страницу
        browser.refresh()

        # Переход на главную через иконку
        modal_page.icon.click()

        # Шаг назад
        browser.back()

        # Установка размеров окна
        browser.set_window_size(900, 400)

        # Шаг вперёд
        browser.forward()

        # Проверка URL и title
        assert browser.current_url == demoqa_page.base_url

        # Проверка заголовка страницы
        assert browser.title == "ToolsQA"

        # Возврат размера окна по умолчанию
        browser.set_window_size(1000, 1000)