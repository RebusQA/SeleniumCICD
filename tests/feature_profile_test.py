import random
import string
import time
import allure
import pytest

from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):


    @allure.title("Change profile name")
    @allure.step("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):

        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        # Генерация случайного имени длиной до 30 символов как требует сайт
        random_name = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 30)))
        # Изменение имени на странице
        self.personal_page.change_name(random_name)
        self.personal_page.save_changes()
        self.personal_page.is_changes_save()
        time.sleep(5)
        self.personal_page.make_screenshot("Success")