import time

from tests.pages.base_page import BasePage
from tests.pages.locators import Locators
from loguru import logger


class RegistrationPage(BasePage):
    """
     Класс для взаимодействия со страницей регистрации на портале.

     Этот класс содержит методы для автоматизации процесса регистрации пользователя на портале.
     Он наследует базовый функционал от класса BasePage и добавляет специализированные шаги,
     такие как ввод имени, email, пароля, и выполнение действий по регистрации и входу.
     """

    def registration_process(self):
        """
               Выполняет процесс регистрации и входа на портал.

               Метод выполняет следующие действия:
               1. Проверяет начальный URL страницы.
               2. Нажимает на кнопку "Зарегистрироваться".
               3. Генерирует и вводит случайное имя пользователя.
               4. Генерирует и вводит случайный email.
               5. Генерирует и вводит пароль, а также повторный пароль.
               6. Нажимает на кнопку "Зарегистрироваться".
               7. Проверяет, что URL изменился после регистрации и содержить email.

               В случае возникновения ошибок:
               - Исключение будет залогировано.
               - Исключение будет повторно возбуждено для завершения теста.

               Raises:
                   Exception: Если в процессе выполнения возникает ошибка.
               """
        try:
            self.assert_url_is_equal("https://app.linkbuilder.com/ru/login")
            logger.info('Нажатие кнопки "Зарегистрироваться"')
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
            logger.info('Нажатие кнопки "Зарегистрироваться"')
            self.find_and_click_element(Locators.registration_button)
            logger.info('Ожидаем смены url после регистрации')
            self.wait_for_body_to_load()
            logger.info('Получение текущего url')
            current_url = self.driver.current_url
            assert email in current_url, f"Email '{email}' не найден в URL: {current_url}"
            logger.info(f"Email '{email}' успешно найден в URL: {current_url}")
            logger.info('Пользователь успешно зарегистрирован')
        except Exception as e:
            logger.error(f"Ошибка в процессе регистрации: {str(e)}")
            raise
