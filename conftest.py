import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
      
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                 help="Choose language: ru/en/ua etc...")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language is not None:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should not be empty")
    yield browser
    print("\nquit browser..")
    browser.quit()