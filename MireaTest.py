from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pathlib
import unittest
import urllib.request

class MireaTest(unittest.TestCase):
    # Путь к текущей папке
    cur_path = pathlib.Path().absolute()
    # Настройки драйвера
    options = Options()
    # Местоположение Chrome
    options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
    # Адрес сайта
    site_url = "https://www.mirea.ru/"
           
    def test(self):
        driver = webdriver.Firefox(options=self.options, executable_path=str(self.cur_path) + "\geckodriver.exe")
        print("Браузер открыт")
        print("Примечение: все запрещенные к использованию файловой системой символы будут закодированы в URL ASCII кодировке.")
        driver.get(self.site_url)
        print("Открыт сайт: " + driver.current_url)
        print("Запуск поиска картинок по сайту...\n")
        img_list = driver.find_elements_by_tag_name("img")
        for img in img_list:
            src = str(img.get_attribute("src"))
            src = src.replace("\\", "%5c")
            src = src.replace("/", "%2f")
            src = src.replace(":", "%3a")
            dest = "images//" + src
            print("Найдено изображение с ссылкой: ", img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), dest)
            print("Изображение успешно сохранено на компьютер с именем: ", src,"\n") 
        driver.quit()
        print("Браузер закрыт")
        
if __name__ == "__main__":
    unittest.main()

