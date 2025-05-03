import time
from pages.accordion import Accordion

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    # Убедимся, что секция видна до клика
    assert accordion_page.section1_content.is_visible()

    # Кликаем по заголовку, чтобы скрыть контент
    accordion_page.section1_heading.click()
    time.sleep(2)

    # Проверяем, что после клика контент больше не отображается
    assert not accordion_page.section1_content.is_visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    # Просто проверяем, что страница загружается и элемент доступен
    assert accordion_page.section1_content.exist()

def test_check_hidden_elements(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    # Проверка, что секция 2 контента скрыта по умолчанию
    assert not accordion_page.section2_content1.is_visible()
    assert not accordion_page.section2_content2.is_visible()

    # Проверка, что секция 3 контента скрыта по умолчанию
    assert not accordion_page.section3_content.is_visible()