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

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após o teste
        cls.driver.quit()

    def test_verificacao_detalhes_do_produto(self):
        # CT05 | Verificação de detalhes do produto
        product_link = self.driver.find_element("id", "item_4_title_link")
        product_link.click()

        time.sleep(3)

        # Verificar se as informações do produto correspondem às expectativas
        expected_name = "Sauce Labs Backpack"
        expected_price = "$29.99"
        product_name = self.driver.find_element("class name", "inventory_details_name")
        product_price = self.driver.find_element("class name", "inventory_details_price")
        
        self.assertEqual(expected_name, product_name.text)
        self.assertEqual(expected_price, product_price.text)


if __name__ == "__main__":
    unittest.main()
