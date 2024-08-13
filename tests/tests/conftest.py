import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import os
from typing import Final

BASE_URL: Final = os.getenv("BASE_URL", "https://app.linkbuilder.com/ru/login")

@pytest.fixture
def driver(request):
    """
    Фикстура для инициализации веб-драйвера Chrome с переданными опциями.
    Запускает браузер в режиме инкогнито и разворачивает его на весь экран.
    """
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
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
