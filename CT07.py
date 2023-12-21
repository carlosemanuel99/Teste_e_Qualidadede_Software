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
        add_to_cart_button.click()
        cart_icon = cls.driver.find_element("id", "shopping_cart_container")
        time.sleep(2)
        cart_icon.click()

        time.sleep(2)

        # CT03 | Finalizar compra
        checkout_button = cls.driver.find_element("xpath", "//button[text()='Checkout']")
        checkout_button.click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após o teste
        cls.driver.quit()

    def test_campos_obrigatorios_durante_checkout(self):
        # CT07 | Campos obrigatórios durante o checkout

        # Continuar sem preencher campos obrigatórios
        continue_button = self.driver.find_element("xpath", "//input[@value='Continue']")
        continue_button.click()

        time.sleep(2)

        # Verificar se as mensagens de erro são exibidas corretamente
        error_messages = self.driver.find_elements("class name", "error-message-container")
        self.assertTrue(len(error_messages) > 0)


if __name__ == "__main__":
    unittest.main()
