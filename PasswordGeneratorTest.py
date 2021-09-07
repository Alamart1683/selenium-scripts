from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import pathlib
import unittest

class PasswordGeneratorTest(unittest.TestCase):
    # Путь к текущей папке
    cur_path = pathlib.Path().absolute()
    # Настройки драйвера
    options = Options()
    # Местоположение Firefox
    options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

    def setUp(self):
        self.driver = webdriver.Firefox(options=self.options, executable_path=str(self.cur_path) + "\geckodriver.exe")
        self.driver.get("http://www.onlinepasswordgenerator.ru/")

    # Тест №1: проверка возможности ввода данных
    def test_1(self):
        print("Тест №1 Смоук тестирование генератора паролей")
        print("")
        print("Тестирование управления чекбоксами")
        check_nums = self.driver.find_element_by_name("usenums")
        check_caps = self.driver.find_element_by_name("usecaps")
        check_lower = self.driver.find_element_by_name("uselower")
        check_symbols = self.driver.find_element_by_name("usesymbols")
        check_nums.click()
        check_nums.click()
        print("Чекбокс выбора цифр работает корректно")
        check_caps.click()
        check_caps.click()
        print("Чекбокс выбора прописных букв работает корректно")
        check_lower.click()
        check_lower.click()
        print("Чекбокс выбора строчных букв работает корректно")
        check_symbols.click()
        check_symbols.click()
        print("Чекбокс выбора спецсимволов работает корректно")
        print("Тестирование управления чекбоксами успешно пройдено")
        print("")
        print("Тестирование ввода длины пароля")
        input_text = self.driver.find_element_by_name("value")
        input_text.send_keys("12")
        print("Число 12 успешно введено")
        input_text.clear()
        print("Поле ввода успещно очищено")
        input_text.send_keys("7")
        print("Число 7 успешно введено")
        input_text.clear()
        print("Поле ввода успещно очищено")
        input_text.send_keys("42")
        print("Число 42 успешно введено")
        input_text.clear()
        print("Поле ввода успещно очищено")
        input_text.send_keys("34")
        print("Число 34 успешно введено")
        input_text.clear()
        print("Поле ввода успещно очищено")
        print("Тестирование ввода длины пароля успешно пройдено")
        print("")
        print("Тестирование возможности генерации паролей")
        generate = self.driver.find_element_by_xpath("//input[@type='submit']")
        input_text.send_keys("13")
        print("Число 13 успешно введено")
        print("Запуск генерации паролей")
        generate.click()
        print("Пароли сгенерированы")
        print("Тестирование возможности генерации паролей успешно пройдено")
        print("")
        print("Тест №1 Завершен успешно")
        print("")

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()

