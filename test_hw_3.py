from selene import browser, be, have


def test_search_not_found(browser_settings):
    browser.open('https://duckduckgo.com/')
    browser.element('[placeholder="Поиск без отслеживания"]').should(be.blank).type('#######').press_enter()
    browser.element('[data-area="mainline"]').should(have.text('ничего не найдено.'))


def test_search_found(browser_settings):
    browser.open('https://duckduckgo.com/')
    browser.element('[placeholder="Поиск без отслеживания"]').should(be.blank).type('qa_guru').press_enter()
    browser.element('.//span[contains(text(), "QAGuru Inc - Quality Accelerated")]').should(have.text('QAGuru'))