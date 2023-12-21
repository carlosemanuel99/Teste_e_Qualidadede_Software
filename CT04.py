import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar o driver do Selenium
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.saucedemo.com/")

        # CT001 | Login com credenciais válidas
        username = cls.driver.find_element("id", "user-name")
        password = cls.driver.find_element("id", "password")
        login_button = cls.driver.find_element("id", "login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após todos os testes na classe
        cls.driver.quit()

    def test_logout_bem_sucedido(self):
        # CT004 | Logout bem-sucedido

        menu_button = self.driver.find_element("id", "react-burger-menu-btn")
        menu_button.click()
        time.sleep(2)

        logout_button = self.driver.find_element("id", "logout_sidebar_link")
        logout_button.click()

        # Adicionar uma pausa de 5 segundos para observar o que acontece após o logout
        time.sleep(3)

        # Verificar se houve redirecionamento para a página de login
        self.assertEqual("https://www.saucedemo.com/", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
