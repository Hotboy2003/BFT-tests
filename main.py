from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class SiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_website(self):
        # Шаг 1: Открыть сайт
        self.driver.get("https://habr.com/ru/articles/")

        # Шаг 2: Проверить заголовок страницы
        # Проверка 1:
        self.assertEqual("Все статьи подряд / Хабр", self.driver.title, "Заголовок страницы не соответствует ожидаемому.")

        # Шаг 3: Найти элемент заголовка и проверить его текст
        # Проверка 2:
        header_element = self.driver.find_element(By.XPATH, "//h1")
        header_text = header_element.text
        self.assertEqual("Все потоки", header_text, "Текст заголовка не соответствует ожидаемому.")

        # Шаг 4: Найти ссылку и кликнуть по ней
        more_info_link = self.driver.find_element(By.XPATH, "//a[text()='Разработка']")
        more_info_link.click()

        # Шаг 5: Проверить, что мы находимся на новой странице
        # Проверка 3:
        header_element = self.driver.find_element(By.XPATH, "//h1")
        header_text = header_element.text
        self.assertEqual("Разработка", header_text, "Не удалось перейти на новую страницу.")

        # Шаг 6: Убедиться, что кнопка "Войти" отображается на новой странице
        # Проверка 4:
        back_button = self.driver.find_element(By.XPATH,
                                               "//button[text()='Войти']")  # Замените на актуальный текст кнопки
        self.assertTrue(back_button.is_displayed(), "Кнопка 'Войти' не отображается на новой странице.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
