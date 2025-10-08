# testes/testes_de_sistema/test_carrinho_de_compras.py

import unittest
from playwright.sync_api import sync_playwright, expect

class TesteCarrinhoDeCompras(unittest.TestCase):

    def setUp(self):
        """
        PREPARAÇÃO: 
        Abrir o navegador, fazer o login antes de cada teste.
        """
        self.playwright = sync_playwright().start()
        self.navegador = self.playwright.chromium.launch(headless=False, slow_mo=1000)
        self.pagina = self.navegador.new_page()
        self.pagina.goto("https://www.saucedemo.com/")

        # --- LOGIN EMBUTIDO NA PREPARAÇÃO ---
        self.pagina.locator("#user-name").fill("standard_user")
        self.pagina.locator("#password").fill("secret_sauce")
        self.pagina.locator("#login-button").click()

        # Garante que a página de produtos carregou antes de prosseguir
        expect(self.pagina.locator(".title")).to_have_text("Products")
        print("\nLogin feito na preparação (setUp).")

    def tearDown(self):
        """LIMPEZA: Roda depois de CADA teste."""
        self.navegador.close()
        self.playwright.stop()

    def teste1_adicionar_um_item_ao_carrinho(self):
        """Caso de Teste 1: Adicionar um item e verificar o ícone do carrinho."""
        print("Executando: teste1_adicionar_um_item_ao_carrinho")

        # AÇÃO: Clica no botão "Add to cart" da mochila
        self.pagina.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

        # VERIFICAÇÃO 1: O ícone do carrinho deve mostrar o número "1"
        icone_carrinho = self.pagina.locator(".shopping_cart_badge")
        expect(icone_carrinho).to_be_visible()
        expect(icone_carrinho).to_have_text("1")

        # VERIFICAÇÃO 2: O botão do produto deve mudar para "Remove"
        botao_remover = self.pagina.locator("[data-test='remove-sauce-labs-backpack']")
        expect(botao_remover).to_be_visible()
        expect(botao_remover).to_have_text("Remove")

        self.pagina.wait_for_timeout(3000)

    def teste2_adicionar_e_remover_um_item(self):
        """Caso de Teste 2: Adicionar um item e depois removê-lo."""
        print("Executando: teste2_adicionar_e_remover_um_item")

        # AÇÃO 1: Adiciona o item
        self.pagina.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        
        # VERIFICAÇÃO: Confere se o item foi adicionado
        icone_carrinho = self.pagina.locator(".shopping_cart_badge")
        expect(icone_carrinho).to_have_text("1")

        # AÇÃO 2: Remove o item
        self.pagina.locator("[data-test='remove-sauce-labs-backpack']").click()

        # VERIFICAÇÃO FINAL: O ícone do carrinho deve desaparecer
        expect(icone_carrinho).to_be_hidden()

        self.pagina.wait_for_timeout(3000)

    def teste3_adicionar_multiplos_itens_ao_carrinho(self):
        """Caso de Teste 3: Adicionar dois itens e verificar o total."""
        print("Executando: teste3_adicionar_multiplos_itens_ao_carrinho")

        # AÇÃO: Adiciona dois produtos diferentes
        self.pagina.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        self.pagina.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
        
        # VERIFICAÇÃO: O ícone do carrinho deve mostrar o número "2"
        icone_carrinho = self.pagina.locator(".shopping_cart_badge")
        expect(icone_carrinho).to_be_visible()
        expect(icone_carrinho).to_have_text("2")

        self.pagina.wait_for_timeout(3000)

if __name__ == "__main__":
    unittest.main()

#python -m unittest testes/testes_de_sistema/test_carrinho_de_compras.py    