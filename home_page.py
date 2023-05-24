from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from orange_HRM_project_2.pages.orange_hrm_web_elements import OrangeHrmElements


class HomePage:
    result_data = []
    home_page_list = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard",
                      "Directory", "Maintenance", "Buzz"]

    def __init__(self, driver):
        self.driver = driver

    def validate_home_page_search_text_box(self, text):
        search_box = self.driver.find_element(By.XPATH, OrangeHrmElements.home_page_search_text_box_XPATH)
        for search_box_text in text:
            search_box.send_keys(search_box_text)
            result_text = self.driver.find_element(By.XPATH, "//span[contains(@class,'menu-item--name')]").text
            self.result_data.append(result_text)
            search_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
