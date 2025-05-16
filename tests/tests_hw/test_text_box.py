from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box = TextBox(browser)

    full_name_text = "Tester Testerov"
    current_address_text = "123 Demo Street"

    text_box.visit()
    text_box.full_name.send_keys(full_name_text)
    text_box.current_address.send_keys(current_address_text)

    text_box.btn_submit.scroll_to_element()
    text_box.btn_submit.click()

    assert full_name_text in text_box.output_name.get_text()
    assert current_address_text in text_box.output_address.get_text()