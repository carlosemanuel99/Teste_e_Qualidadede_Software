import unittest
import time
from selenium import webdriver

class TestSauceDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar o driver do Selenium
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.saucedemo.com/")

        # CT01 | Login com credenciais válidas
        username = cls.driver.find_element("id", "user-name")
        password = cls.driver.find_element("id", "password")
        login_button = cls.driver.find_element("id", "login-button")
        time.sleep(2)
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        time.sleep(2)
        login_button.click()

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após o teste
        cls.driver.quit()

    def test_navegacao_entre_paginas(self):
        # CT08 | Navegação Link About

        menu_button = self.driver.find_element("id", "react-burger-menu-btn")
        time.sleep(2)
        menu_button.click()

        about_button = self.driver.find_element("id", "about_sidebar_link")
        time.sleep(2)
        about_button.click()

        time.sleep(2)

        # Verificar se houve redirecionamento para a página de saucelabs
        self.assertEqual("https://saucelabs.com/", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
