import pytest
from selene import browser


@pytest.fixture()  # module, class or session
def firefox_browser_actions():
    browser.config.driver_name = "firefox"
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()
