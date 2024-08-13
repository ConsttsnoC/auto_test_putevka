import base64
import time

import pytest

from tests.pages.base_page import BasePage
from tests.pages.locators import Locators
from loguru import logger


class RegistrationPage(BasePage):

    def registration_process(self):
        self.assert_url_is_equal('https://app.linkbuilder.com/ru/login')
        logger.info("Нажатие кнопки \"Зарегистрироваться\"")
        self.find_and_click_element(Locators.login_link_locator)
        first_name = self.generate_first_name()
        self.find_and_send(Locators.input_name, first_name)
        logger.info(f"Введено имя: {first_name}")
        email = self.generate_email()
        self.find_and_send(Locators.input_email, email)
        logger.info(f"Введен email: {email}")
        password = self.generate_password()
        self.find_and_send(Locators.input_password, password)
        logger.info(f"Введен пароль: {password}")
        self.find_and_send(Locators.input_repeat_password, password)
        logger.info(f"Введен повторный пароль: {password}")
        logger.info("Нажатие кнопки \"Зарегистрироваться\"")
        self.find_and_click_element(Locators.registration_button)
        logger.info(f"Введен пароль для входа: {password}")
        self.find_and_send(Locators.login_password, password)
        logger.info("Нажатие кнопки \"Вход\"")
        self.find_and_click_element(Locators.login_button)
        self.wait_for_body_to_load()
        self.assert_url_is_equal('https://app.linkbuilder.com/ru')
        url = self.get_current_url()
        logger.info(f"Вход выполнен успешно, url сменился на: {url}")
        logger.info("Нажатие на изображение аккаунта")
        self.find_and_click_element(Locators.image_account)
        logger.info("Нажатие кнопки \"Выход\"")
        self.find_and_click_element(Locators.logout_account)





