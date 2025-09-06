from selene import browser, be, have


def test_hw_3(browser_settings):
    browser.open('https://duckduckgo.com/')
    browser.element('[placeholder="Поиск без отслеживания"]').should(be.blank).type('#######').press_enter()
    browser.element('[class="THG_yNtlhifBrJDatoUn wZ4JdaHxSAhGy1HoNVja wN0KrcRQzChXFKiMHpCZ"]').should(have.text('ничего не найдено.'))