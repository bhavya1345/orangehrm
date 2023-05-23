from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from orange_HRM_project_2.pages.orange_hrm_web_elements import OrangeHrmElements


class AdminPage:
    role_dropdown_expect_result = []
    status_dropdown_expect_result = []

    def __init__(self, driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.admin_module_XPATH).click()

    def click_user_management(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.user_management_navigation_XPATH).click()

    def click_users(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.users_XPATH).click()

    def click_user_role_dropdown(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.user_role_dropdown_button_XPATH).click()
        user_role_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.user_role_dropdown_list_XPATH)
        for list_of_item in user_role_list:
            self.role_dropdown_expect_result.append(list_of_item.text)

    def click_user_status_dropdown(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.status_dropdown_button_XPATH).click()
        statu_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.status_dropdown_list_XPATH)
        for list_of_item in statu_list:
            self.status_dropdown_expect_result.append(list_of_item.text)
