from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import pathlib
import unittest

class CardGeneratorTest(unittest.TestCase):
    # Путь к текущей папке
    cur_path = pathlib.Path().absolute()
    # Настройки драйвера
    options = Options()
    # Местоположение Firefox
    options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

    def setUp(self):
        self.driver = webdriver.Firefox(options=self.options, executable_path=str(self.cur_path) + "\geckodriver.exe")
        self.driver.get("https://castlots.org/generator-igralnyh-kart/")

    # Тест №1: проверка возможности ввода данных
    def test_1(self):
        print("Тест №1")
        check_p = self.driver.find_element(By.ID, "check-p")
        check_b = self.driver.find_element(By.ID, "check-b")
        check_c = self.driver.find_element(By.ID, "check-c")
        check_t = self.driver.find_element(By.ID, "check-t")
        check_p.click()
        check_p.click()
        check_b.click()
        check_b.click()
        check_c.click()
        check_c.click()
        check_t.click()
        check_t.click()
        print("Выбор масти карт работает коректно")
        radio36and52 = self.driver.find_elements_by_xpath("//input[@type='radio']")
        radio36and52[1].click()
        radio36and52[0].click()
        print("Выбор размера колоды работает корректно")
        slider = self.driver.find_element(By.ID, "slider-kosti")
        # Кликнем по центру
        slider.click()
        # Переместим на четверть скроллбара
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        # Переместим на три четверти скроллабара
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 162, 10)
        action.click()
        action.perform()
        # Полностью заполним скроллбар
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 232, 10)
        action.click()
        action.perform()
        print("Выбор количества карт для генерации работает корректно")
        print("Тест №1 Завершен успешно")
        print("")

    # Тест №2: проверка совпадения количества указанных для генерации карт с количеством сгенерированных
    def test_2(self):
        radio36and52 = self.driver.find_elements_by_xpath("//input[@type='radio']")
        slider = self.driver.find_element(By.ID, "slider-kosti")
        amount = self.driver.find_element(By.ID, "amount")
        button = self.driver.find_element(By.ID, "kosti-button")
        img_list = self.driver.find_elements_by_tag_name("img")
        basic_img_value = len(img_list)
        print("")
        print("Тест №2")
        
        # Генерация 13 карт из колоды в 52 карты
        radio36and52[1].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")

        # Генерация 13 карт из колоды в 36 карт
        radio36and52[0].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")

        # Генерация 19 карт из колоды в 52 карты
        radio36and52[1].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 80, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")

        # Генерация 19 карт из колоды в 36 карт
        radio36and52[0].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 80, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")

        # Генерация 22 карт из колоды в 52 карты
        radio36and52[1].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 92, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")

        # Генерация 22 карт из колоды в 36 карт
        radio36and52[0].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 92, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        
            
        # Генерация 28 карт из колоды в 52 карты
        radio36and52[1].click()
        slider.click()
        button.click()
        button.click()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")

        # Генерация 28 карт из колоды в 36 карт
        radio36and52[0].click()
        slider.click()
        button.click()
        button.click()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        print("Тест №2 завершен успешно")
        print("")

    def test_3(self):
        check_p = self.driver.find_element(By.ID, "check-p")
        check_b = self.driver.find_element(By.ID, "check-b")
        check_c = self.driver.find_element(By.ID, "check-c")
        check_t = self.driver.find_element(By.ID, "check-t")
        radio36and52 = self.driver.find_elements_by_xpath("//input[@type='radio']")
        slider = self.driver.find_element(By.ID, "slider-kosti")
        amount = self.driver.find_element(By.ID, "amount")
        button = self.driver.find_element(By.ID, "kosti-button")
        img_list = self.driver.find_elements_by_tag_name("img")
        basic_img_value = len(img_list)
        print("")
        print("Тест №3")

        # Выбрать только масть Бубны
        check_p.click()
        check_c.click()
        check_t.click()
        
        # Генерация 13 карт из колоды в 52 карты масти Бубны
        radio36and52[1].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        counter = 0
        for img in final_img_list:
            src = str(img.get_attribute("src"))
            if "b-" in src or "-j" in src:
                counter += 1
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        if counter == final:
            print("Все карты принадлежат масти Бубны")
        else:
            print("Не все карты принадлежат масти Бубны")


        # Генерация 13 карт из колоды в 36 карт масти Бубны
        radio36and52[0].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        counter = 0
        for img in final_img_list:
            src = str(img.get_attribute("src"))
            if "b-" in src or "-j" in src:
                counter += 1
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        if counter == final:
            print("Все карты принадлежат масти Бубны")
        else:
            print("Не все карты принадлежат масти Бубны")

        # Выбрать только масть Червы
        check_b.click()
        check_c.click()

        # Генерация 13 карт из колоды в 52 карты масти Червы
        radio36and52[1].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        counter = 0
        for img in final_img_list:
            src = str(img.get_attribute("src"))
            if "c-" in src or "-j" in src:
                counter += 1
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        if counter == final:
            print("Все карты принадлежат масти Червы")
        else:
            print("Не все карты принадлежат масти Червы")


        # Генерация 13 карт из колоды в 36 карт масти Червы
        radio36and52[0].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        counter = 0
        for img in final_img_list:
            src = str(img.get_attribute("src"))
            if "c-" in src or "-j" in src:
                counter += 1
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        if counter == final:
            print("Все карты принадлежат масти Червы")
        else:
            print("Не все карты принадлежат масти Червы")

        # Выбрать только масть Трефы
        check_c.click()
        check_t.click()

        # Генерация 13 карт из колоды в 52 карты масти Трефы
        radio36and52[1].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        counter = 0
        for img in final_img_list:
            src = str(img.get_attribute("src"))
            if "t-" in src or "-j" in src:
                counter += 1
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        if counter == final:
            print("Все карты принадлежат масти Трефы")
        else:
            print("Не все карты принадлежат масти Трефы")


        # Генерация 13 карт из колоды в 36 карт масти Трефы
        radio36and52[0].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        counter = 0
        for img in final_img_list:
            src = str(img.get_attribute("src"))
            if "t-" in src or "-j" in src:
                counter += 1
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        if counter == final:
            print("Все карты принадлежат масти Трефы")
        else:
            print("Не все карты принадлежат масти Трефы")

        # Выбрать только масть Пики
        check_t.click()
        check_p.click()

        # Генерация 13 карт из колоды в 52 карты масти Трефы
        radio36and52[1].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        counter = 0
        for img in final_img_list:
            src = str(img.get_attribute("src"))
            if "p-" in src or "-j" in src:
                counter += 1
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 52 карты")
        if counter == final:
            print("Все карты принадлежат масти Пики")
        else:
            print("Не все карты принадлежат масти Пики")


        # Генерация 13 карт из колоды в 36 карт масти Трефы
        radio36and52[0].click()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(slider, 54, 10)
        action.click()
        action.perform()
        button.click()
        begin = int(amount.text)
        final_img_list = self.driver.find_elements_by_tag_name("img")
        counter = 0
        for img in final_img_list:
            src = str(img.get_attribute("src"))
            if "p-" in src or "-j" in src:
                counter += 1
        final = len(final_img_list) - basic_img_value
        if final == begin:
            print("Есть совпадение, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        else:
            print("Нет совпадения, было указано",amount.text,"карт для генерации и сгенерировано",final,"карт из колоды в 36 карт")
        if counter == final:
            print("Все карты принадлежат масти Пики")
        else:
            print("Не все карты принадлежат масти Пики")

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()

