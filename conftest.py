import pytest
from selene import browser, be, have


@pytest.fixture(scope='session')
def browser_settings():
    browser.config.window_width = 1440
    browser.config.window_height = 720
    yield
    browser.close()

