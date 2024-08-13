from tests.pages.registration_page import RegistrationPage


class TestUserRegistration:

    def test_user_registration_process(self, open_website_and_clear):
        page = RegistrationPage(open_website_and_clear)
        page.registration_process()
