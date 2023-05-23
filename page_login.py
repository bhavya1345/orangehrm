from _ast import Assert

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from orange_HRM_project_2.pages.orange_hrm_web_elements import OrangeHrmElements


class PageLogin:

    def __init__(self, driver):
        self.driver = driver

    def user_login(self, username, password):
        self.driver.find_element(By.XPATH, OrangeHrmElements.user_name_text_box_XPATH).send_keys(username)
        self.driver.find_element(By.XPATH, OrangeHrmElements.password_text_box_XPATH).send_keys(password)
        self.driver.find_element(By.XPATH, OrangeHrmElements.login_button_XPATH).click()

    def clear_invalid_data(self):
        clear_username = self.driver.find_element(By.XPATH, OrangeHrmElements.user_name_text_box_XPATH)
        clear_username.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        clear_password = self.driver.find_element(By.XPATH, OrangeHrmElements.password_text_box_XPATH)
        clear_password.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)


