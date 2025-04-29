from pages.demoqa import DemoQa

def test_check_icon(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()
    demo_qa_page.icon.click()
