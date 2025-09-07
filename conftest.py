import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_settings():
    browser.config.window_width = 1440
    browser.config.window_height = 720
    yield
    browser.quit()

