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
        # Configurar o driver do Selenium uma vez para todos os testes na classe
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.saucedemo.com/")

    @classmethod
    def tearDownClass(cls):
        # Fechar o navegador após todos os testes na classe
        cls.driver.quit()

    # def test_login_com_credenciais_validas(self):
    #     # CT001 | Login com credenciais válidas
    #     username = self.driver.find_element("id", "user-name")
    #     password = self.driver.find_element("id", "password")
    #     login_button = self.driver.find_element("id", "login-button")

    #     username.send_keys("standard_user")
    #     password.send_keys("secret_sauce")
    #     login_button.click()

    #     # Adicionar uma pausa de 2 segundos para observar o que acontece após o login
    #     time.sleep(5)

    #     # Verificar se o redirecionamento para a página de produtos ocorre após o login bem-sucedido
    #     self.assertEqual("https://www.saucedemo.com/inventory.html", self.driver.current_url)

    def test_adicionar_produto_ao_carrinho(self):

        # CT001 | Login com credenciais válidas
        username = self.driver.find_element("id", "user-name")
        password = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        # CT002 | Adicionar produto ao carrinho
        add_to_cart_button = self.driver.find_element("xpath", "//button[text()='Add to cart']")
        time.sleep(5)
        add_to_cart_button.click()

        # Adicionar uma pausa de 2 segundos para observar o que acontece após adicionar ao carrinho
        time.sleep(5)

        # Verificar se o ícone do carrinho exibe o número correto de itens
        cart_icon = self.driver.find_element("class name", "shopping_cart_badge")
        self.assertEqual("1", cart_icon.text)

    # def test_finalizar_compra(self):
    #     # CT003 | Finalizar compra
    #     # (Assumindo que há produtos no carrinho. Caso contrário, adicione produtos ao carrinho primeiro)
    #     checkout_button = self.driver.find_element("xpath", "//a[text()='CHECKOUT']")
    #     checkout_button.click()

    #     # Adicionar uma pausa de 2 segundos para observar o que acontece após o checkout
    #     time.sleep(2)

    #     # Verificar se há uma confirmação de compra bem-sucedida após o checkout
    #     confirmation_message = self.driver.find_element("class name", "complete-header")
    #     self.assertEqual("THANK YOU FOR YOUR ORDER", confirmation_message.text)

    # def test_logout_bem_sucedido(self):
    #     # CT004 | Logout bem-sucedido
    #     logout_button = self.driver.find_element("id", "logout_sidebar_link")
    #     logout_button.click()

    #     # Adicionar uma pausa de 2 segundos para observar o que acontece após o logout
    #     time.sleep(2)

    #     # Verificar se houve redirecionamento para a página de login
    #     self.assertEqual("https://www.saucedemo.com/", self.driver.current_url)

    # def test_verificacao_detalhes_do_produto(self):
    #     # CT005 | Verificação de detalhes do produto
    #     product_link = self.driver.find_element("xpath", "//div[@class='inventory_item']/div[@class='inventory_item_description']/a")
    #     product_link.click()

    #     # Adicionar uma pausa de 2 segundos para observar os detalhes do produto
    #     time.sleep(2)

    #     # Verificar se as informações do produto correspondem às expectativas
    #     product_name = self.driver.find_element("class name", "inventory_details_name")
    #     product_price = self.driver.find_element("class name", "inventory_details_price")
    #     self.assertEqual("Nome do Produto", product_name.text)
    #     self.assertEqual("Preço do Produto", product_price.text)

    # def test_remover_item_do_carrinho(self):
    #     # CT006 | Remover item do carrinho
    #     add_to_cart_button = self.driver.find_element("xpath", "//button[text()='ADD TO CART']")
    #     add_to_cart_button.click()

    #     # Adicionar uma pausa de 2 segundos para observar o que acontece após adicionar ao carrinho
    #     time.sleep(2)

    #     # Remover o item do carrinho
    #     remove_button = self.driver.find_element("xpath", "//button[text()='REMOVE']")
    #     remove_button.click()

    #     # Adicionar uma pausa de 2 segundos para observar o que acontece após remover do carrinho
    #     time.sleep(2)

    #     # Verificar se o ícone do carrinho não exibe nenhum item
    #     cart_icon = self.driver.find_element("class name", "shopping_cart_badge")
    #     self.assertEqual("", cart_icon.text)

    # def test_campos_obrigatorios_durante_checkout(self):
    #     # CT007 | Campos obrigatórios durante o checkout
    #     checkout_button = self.driver.find_element("xpath", "//a[text()='CHECKOUT']")
    #     checkout_button.click()

    #     # Adicionar uma pausa de 2 segundos para observar o que acontece após clicar em CHECKOUT
    #     time.sleep(2)

    #     # Continuar sem preencher campos obrigatórios
    #     continue_button = self.driver.find_element("xpath", "//input[@value='CONTINUE']")
    #     continue_button.click()

    #     # Verificar se as mensagens de erro são exibidas corretamente
    #     error_messages = self.driver.find_elements("class name", "error-message-container")
    #     self.assertTrue(len(error_messages) > 0)

    # def test_navegacao_entre_paginas(self):
    #     # CT008 | Navegação entre páginas
    #     # (Assumindo que existem links de navegação para diferentes seções do site)
    #     product_link = self.driver.find_element("xpath", "//a[text()='Products']")
    #     product_link.click()

    #     # Adicionar uma pausa de 2 segundos para observar o que acontece após clicar em Products
    #     time.sleep(2)

    #     # Verificar se a navegação para a página de produtos ocorreu
    #     self.assertEqual("https://www.saucedemo.com/inventory.html", self.driver.current_url)

    # def test_pesquisar_por_um_produto(self):
    #     # CT009 | Pesquisar por um produto
    #     search_box = self.driver.find_element("class name", "search_input")
    #     search_box.send_keys("Nome do Produto")  # Substitua com o termo de pesquisa desejado
    #     search_box.send_keys(Keys.RETURN)

    #     # Adicionar uma pausa de 2 segundos para observar os resultados da pesquisa
    #     time.sleep(2)

    #     # Verificar se os resultados da pesquisa são exibidos corretamente
    #     search_results = self.driver.find_elements("class name", "inventory_item_name")
    #     self.assertTrue(len(search_results) > 0)

    # def test_verificar_funcionalidade_de_ordenacao(self):
    #     # CT010 | Verificar funcionalidade de ordenação
    #     # (Assumindo que existem opções de ordenação como por preço, por nome, etc.)
    #     sort_dropdown = self.driver.find_element("class name", "product_sort_container")
    #     sort_dropdown.click()

    #     # Selecionar uma opção de ordenação (por exemplo, 'Name (A to Z)')
    #     option_name_ascending = self.driver.find_element("xpath", "//option[text()='Name (A to Z)']")
    #     option_name_ascending.click()

    #     # Adicionar uma pausa de 2 segundos para observar a ordenação
    #     time.sleep(2)

    #     # Verificar se a lista de produtos está ordenada corretamente
    #     sorted_products = self.driver.find_elements("class name", "inventory_item_name")
    #     names = [product.text for product in sorted_products]
    #     self.assertEqual(sorted(names), names)

if __name__ == "__main__":
    unittest.main()
