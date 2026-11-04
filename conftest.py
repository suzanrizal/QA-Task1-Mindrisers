from selenium import webdriver
import pytest

# Register custom CLI option
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome, edge, firefox"
    )
# Setting up driver fixture to use the selected browser

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    yield driver
    driver.quit()