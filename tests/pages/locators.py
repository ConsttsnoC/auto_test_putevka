from selenium.webdriver.common.by import By


class Locators:
    """
    Класс для хранения локаторов веб-элементов.

    Этот класс используется для определения и группировки локаторов, которые
    будут использованы на различных страницах веб-приложения.
    """

    login_link_locator = (By.XPATH, '//*[@id="__nuxt"]/div/div[1]/section/div/form/p/a')
    input_name = (
        By.CSS_SELECTOR,
        "#__nuxt > div > div.login-layout__main > section > div > form > div:nth-child(1) > input",
    )
    input_email = (
        By.CSS_SELECTOR,
        "#__nuxt > div > div.login-layout__main > section > div > form > div:nth-child(2) > input",
    )
    input_password = (
        By.CSS_SELECTOR,
        "#__nuxt > div > div.login-layout__main > section > div > form > div:nth-child(3) > div > input",
    )
    input_repeat_password = (
        By.CSS_SELECTOR,
        "#__nuxt > div > div.login-layout__main > section > div > form > div:nth-child(4) > div > input",
    )
    registration_button = (
        By.CSS_SELECTOR,
        "#__nuxt > div > div.login-layout__main > section > div > form > button",
    )
    login_password = (
        By.CSS_SELECTOR,
        "#__nuxt > div > div.login-layout__main > section > div > form > div:nth-child(2) > div > input",
    )
    login_button = (
        By.CSS_SELECTOR,
        "#__nuxt > div > div.login-layout__main > section > div > form > button",
    )
    image_account = (
        By.CSS_SELECTOR,
        "#app-wrapper > header > div > div.site-header__user > div.site-header__user-profile > button",
    )
    logout_account = (
        By.CSS_SELECTOR,
        "#app-wrapper > header > div > div.site-header__user > div.site-header__user-profile > div > footer > a > span",
    )
