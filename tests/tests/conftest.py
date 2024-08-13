import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import os
from typing import Final

BASE_URL: Final = os.getenv("BASE_URL", "https://app.linkbuilder.com/ru/login")


def pytest_addoption(parser):
    """
    Эта функция используется для добавления опции `--headless` к командной строке pytest.
    Если эта опция указана, браузер будет запускаться в headless режиме, что позволяет
    запускать тесты без отображения пользовательского интерфейса браузера.
    """
    parser.addoption(
        "--headless", action="store_true", help="run browser in headless mode"
    )


@pytest.fixture
def driver(request):
    """
    Фикстура для инициализации веб-драйвера Chrome с переданными опциями.
    Запускает браузер в режиме инкогнито и разворачивает его на весь экран.
    """
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def open_website_and_clear(driver):
    """
    Фикстура для открытия сайта, очистки localStorage, sessionStorage и cookies.
    """
    logger.info(f"Ожидаем открытие {BASE_URL}")
    driver.get(BASE_URL)
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.delete_all_cookies()
    yield driver
