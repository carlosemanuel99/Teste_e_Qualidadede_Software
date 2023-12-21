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
        time.sleep(2)
        add_to_cart_button.click()
        time.sleep(3)
        cart_icon = cls.driver.find_element("id", "shopping_cart_container")
        time.sleep(2)
        cart_icon.click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após o teste
        cls.driver.quit()

    def test_finalizar_compra(self):
        # CT03 | Finalizar compra
        checkout_button = self.driver.find_element("xpath", "//button[text()='Checkout']")
        checkout_button.click()

        time.sleep(3)

        # Verificar se está na página "https://www.saucedemo.com/checkout-step-one.html" após o checkout
        self.assertEqual("https://www.saucedemo.com/checkout-step-one.html", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
