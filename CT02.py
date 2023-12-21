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

    def test_adicionar_produto_ao_carrinho(self):
        # CT02 | Adicionar produto ao carrinho
        add_to_cart_button = self.driver.find_element("xpath", "//button[text()='Add to cart']")

        time.sleep(2)
        
        add_to_cart_button.click()

        time.sleep(3)

        # Verificar se o ícone do carrinho exibe o número correto de itens
        cart_icon = self.driver.find_element("class name", "shopping_cart_badge")
        self.assertEqual("1", cart_icon.text)


if __name__ == "__main__":
    unittest.main()
