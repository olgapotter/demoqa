import allure
from pages.tables import Tables


@allure.title("Тест сортировки по заголовкам столбцов в WebTables")
def test_sort_table_columns(browser):
    page = Tables(browser)
    page.visit()

    headers = page.get_column_headers()
    assert headers, "Заголовки таблицы не найдены"

    for header in headers:
        header_text = header.text
        header.click()

        classes = header.get_attribute("class")
        assert "-sort-" in classes, f"Сортировка по колонке '{header_text}' не произошла"