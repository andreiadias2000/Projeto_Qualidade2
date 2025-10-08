
#teste_login_com_senha_invalida
#teste_login_com_sucesso
#teste_login_com_usuario_bloqueado
#teste_login_com_usuario_nao_cadastrado



import unittest
from playwright.sync_api import sync_playwright, expect

class TesteLoginSauceDemo(unittest.TestCase):

    def setUp(self):
        """PREPARAÇÃO: Roda antes de CADA teste."""
        self.playwright = sync_playwright().start()
        self.navegador = self.playwright.chromium.launch(headless=False) 
        self.pagina = self.navegador.new_page()
        self.pagina.goto("https://www.saucedemo.com/")

    def tearDown(self):
        """LIMPEZA: Roda depois de CADA teste."""
        self.navegador.close()
        self.playwright.stop()

    def teste_login_com_sucesso(self):
        """Caso de Teste 1: Caminho muito Feliz"""
        print("\nExecutando: teste_login_com_sucesso")

        # AÇÃO
        self.pagina.locator("#user-name").fill("standard_user")
        self.pagina.locator("#password").fill("secret_sauce")
        self.pagina.locator("#login-button").click()

        # VERIFICAÇÃO
        titulo_produtos = self.pagina.locator(".title")
        expect(titulo_produtos).to_be_visible()
        expect(titulo_produtos).to_have_text("Products")
        self.pagina.wait_for_timeout(3000)

    def teste_login_com_senha_invalida(self):
        """Caso de Teste 2: Entrada de senha Inválida"""
        print("\nExecutando: teste_login_com_senha_invalida")

        # AÇÃO
        self.pagina.locator("#user-name").fill("standard_user")
        self.pagina.locator("#password").fill("MEUUUDEUSSS")
        self.pagina.locator("#login-button").click()

        # VERIFICAÇÃO
        mensagem_erro = self.pagina.locator("[data-test='error']")
        expect(mensagem_erro).to_be_visible()
        expect(mensagem_erro).to_contain_text("Username and password do not match")
        self.pagina.wait_for_timeout(3000)

    def teste_login_com_usuario_bloqueado(self):
        """Caso de Teste 3: Usuario bloquado"""
        print("\nExecutando: teste_login_com_usuario_bloqueado")

        # AÇÃO
        self.pagina.locator("#user-name").fill("locked_out_user")
        self.pagina.locator("#password").fill("secret_sauce")
        self.pagina.locator("#login-button").click()

        # VERIFICAÇÃO
        mensagem_erro = self.pagina.locator("[data-test='error']")
        expect(mensagem_erro).to_be_visible()
        expect(mensagem_erro).to_contain_text("Sorry, this user has been locked out")
        self.pagina.wait_for_timeout(3000)

    def teste_login_com_usuario_nao_cadastrado(self):
        """Caso de teste 4: Entrada Inválida (Usuário)
        Verifica com um usuário que não existe no cadastro.
        """
        print("\nExecutando: teste_login_com_usuario_nao_cadastrado")

        # AÇÃO
        self.pagina.locator("#user-name").fill("usuario_inexistente")
        self.pagina.locator("#password").fill("qualquer_senha")
        self.pagina.locator("#login-button").click()

        # VERIFICAÇÃO
        mensagem_erro = self.pagina.locator("[data-test='error']")
        expect(mensagem_erro).to_be_visible()
        expect(mensagem_erro).to_contain_text("Username and password do not match")
        self.pagina.wait_for_timeout(3000)

        
if __name__ == "__main__":
    unittest.main()

# python -m unittest testes/testes_de_sistema/teste_login_saucedemo.py    