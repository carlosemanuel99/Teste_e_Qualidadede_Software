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

        time.sleep(3)

        # CT02 | Adicionar produto ao carrinho
        add_to_cart_button = cls.driver.find_element("xpath", "//button[text()='Add to cart']")
        time.sleep(1)
        add_to_cart_button.click()

        # CT02 | Adicionar produto ao carrinho
        add_to_cart_button = cls.driver.find_element("xpath", "//button[text()='Add to cart']")
        time.sleep(1)
        add_to_cart_button.click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após o teste
        cls.driver.quit()

    def test_remover_item_do_carrinho(self):
        # CT06 | Remover item do carrinho

        # Remover 1 item do carrinho
        remove_button = self.driver.find_element("xpath", "//button[text()='Remove']")
        remove_button.click()

        time.sleep(3)

        # Verificar se o ícone do carrinho exibe 1 item apenas
        cart_icon = self.driver.find_element("class name", "shopping_cart_badge")
        self.assertEqual("1", cart_icon.text)


if __name__ == "__main__":
    unittest.main()
