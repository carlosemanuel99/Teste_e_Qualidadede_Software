import unittest
import time
from selenium import webdriver

class TestSauceDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar o driver do Selenium
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.saucedemo.com/")

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após o teste
        cls.driver.quit()

    def test_login_com_credenciais_validas(self):
        # CT01 | Login com credenciais válidas
        username = self.driver.find_element("id", "user-name")
        password = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login-button")

        time.sleep(2)

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")

        time.sleep(2)

        login_button.click()

        time.sleep(2)

        # Verificar se o redirecionamento para a página de produtos ocorre após o login bem-sucedido
        self.assertEqual("https://www.saucedemo.com/inventory.html", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
