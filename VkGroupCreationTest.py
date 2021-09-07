from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import pathlib
import unittest
import random

class VkGroupCreationTest(unittest.TestCase):
    phone = "input phone"
    password = "input password"
    groupName = "input group"
    
    # Путь к текущей папке
    cur_path = pathlib.Path().absolute()
    # Настройки драйвера
    options = Options()
    # Местоположение Firefox
    options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

    def setUp(self):
        self.driver = webdriver.Firefox(options=self.options, executable_path=str(self.cur_path) + "\geckodriver.exe")

   # Тест 1 создание сообщества
    def test_create_group_add_friends(self):
        self.driver.get("https://vk.com/groups")
        self.login()
        print("Авторизация пройдена")
        self.driver.get("https://vk.com/groups")
        print("Открыта вкладка сообществ")
        self.driver.get("https://vk.com/groups_create")
        print("Открыта вкладка создания сообществ")
        tematicButton = self.driver.find_element_by_xpath("//div[@class='groups_create_tile groups_create_tile_thematic']")
        tematicButton.click()
        print("Открыта вкладка создания тематического сообщества")
        inputTitle = self.driver.find_element(By.ID, "groups_create_box_title")
        inputTitle.send_keys(self.groupName)
        inputTheme = self.driver.find_element_by_xpath("//input[@class='selector_input']")
        inputTheme.click()
        inputTheme.send_keys("Наука")
        inputTheme.send_keys(Keys.ENTER)
        createButton = self.driver.find_element_by_xpath("//button[@class='flat_button']")
        createButton.click()
        print("Сообщество создано успешно")
        recommButton = self.driver.find_elements_by_xpath("//*[text() = 'Рекомендовать']")
        print("Сообщество успешно порекомендовано друзьям")

    def tearDown(self):
        self.driver.quit()

    def login(self):
        print("Необходимо авторизоваться")
        phone_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "pass")
        phone_input.send_keys(self.phone)
        password_input.send_keys(self.password)
        self.driver.find_element(By.ID, "login_button").click()
        
if __name__ == "__main__":
    unittest.main()

