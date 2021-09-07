from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pathlib
import unittest
import urllib.request
import os

class UrlParserTest(unittest.TestCase):
    # Путь к текущей папке
    cur_path = pathlib.Path().absolute()
    # Настройки драйвера
    options = Options()
    # Местоположение Chrome
    options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
           
    def test(self):
        file = open('urls.txt', 'r')
        src = ""
        urls = []
        if os.path.isfile("result.txt"):
            os.remove("result.txt")
        # Извлечем данные из файла
        for line in file:
            if len(urls) < 10:
                urls.append(line)
            else:
                src = line
        file.close()
        driver = webdriver.Firefox(options=self.options, executable_path=str(self.cur_path) + "\geckodriver.exe")
        print("Браузер открыт")
        result = open("result.txt", "w+")
        result.close()
        result = open("result.txt", "a+")
        for i in range(len(urls)):
            driver.get(urls[i])
            print("Открыт сайт №",i,": ",driver.current_url)
            print("Запуск поиска картинки с указанной ссылкой по сайту...")
            flag = True
            img_list = driver.find_elements_by_tag_name("img")
            for img in img_list:
                current_src = str(img.get_attribute("src"))
                if src == current_src:
                    print("Найдено изображение с указанной ссылкой")
                    result.write(driver.current_url + "\n")
                    print("Ссылка на данный сайт записана в результирующий файл")
                    print("")
                    flag = False
                    break
            if flag:
                print("Ссылок на укзанную картинку найдено не было")
                print("")
        result.close()
        driver.quit()
        print("Браузер закрыт")
        
if __name__ == "__main__":
    unittest.main()

