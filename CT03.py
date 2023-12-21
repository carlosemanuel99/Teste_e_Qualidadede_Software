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
        time.sleep(5)
        # CT002 | Adicionar produto ao carrinho
        add_to_cart_button = cls.driver.find_element("xpath", "//button[text()='Add to cart']")
        # Adicionar uma pausa de 2 segundos
        time.sleep(2)
        add_to_cart_button.click()
        time.sleep(5)
        cart_icon = cls.driver.find_element("id", "shopping_cart_container")
        time.sleep(2)
        cart_icon.click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após todos os testes na classe
        cls.driver.quit()

    def test_finalizar_compra(self):
        # CT003 | Finalizar compra
        # (Assumindo que há produtos no carrinho. Caso contrário, adicione produtos ao carrinho primeiro)
        checkout_button = self.driver.find_element("xpath", "//button[text()='Checkout']")
        checkout_button.click()

        # Adicionar uma pausa de 2 segundos para observar o que acontece após o checkout
        time.sleep(5)

        # Verificar se há uma confirmação de compra bem-sucedida após o checkout
        self.assertEqual("https://www.saucedemo.com/checkout-step-one.html", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
