import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from utils.attach import add_logs, add_screenshot, add_html, add_video
from utils.helper import BaseSession


@pytest.fixture(scope="function")
def reqres_api():
    with BaseSession(base_url="https://reqres.in") as session:
        yield session


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='chrome'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def reqres_ui(request):
    with BaseSession(base_url="https://reqres.in") as session:
        browser_name = request.config.getoption('--browser_version')
        options = Options()

        selenoid_capabilities = {
            "browserName": browser_name,
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options
        )

        browser.config.driver = driver
        driver.implicitly_wait(60)
        yield session
    add_logs(browser)
    add_screenshot(browser)
    add_html(browser)
    add_video(browser)
    browser.quit()
