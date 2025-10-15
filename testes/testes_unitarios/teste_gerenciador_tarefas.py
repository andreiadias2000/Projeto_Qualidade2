# testes/testes_unitarios/teste_gerenciador_tarefas.py

import unittest
# Importei a classe que quero testar
from logica_aplicativo.gerenciador_tarefas import GerenciadorDeTarefas

class TesteGerenciadorDeTarefas(unittest.TestCase):

    def setUp(self):
        """PREPARAÇÃO: Cria um gerenciador de tarefas novo antes de cada teste."""
        self.gerenciador = GerenciadorDeTarefas()

    def teste_1_adicionar_tarefa_valida(self):
        """Verifica se uma tarefa com nome válido é adicionada."""
        print("\nExecutando teste unitário 1: Adicionar tarefa válida")
        
        # AÇÃO
        self.gerenciador.adicionar_tarefa("Fazer o trabalho de Qualidade Projeto 1")

        # VERIFICAÇÃO
        self.assertEqual(len(self.gerenciador.tarefas), 1)
        self.assertEqual(self.gerenciador.tarefas[0]['descricao'], "Fazer o trabalho de Qualidade Projeto 1")

    def teste_2_nao_adicionar_tarefa_vazia(self):
        """Verifica se o sistema impede a criação de uma tarefa com nome vazio."""
        print("Executando teste unitário 2: Tentar adicionar tarefa vazia")

        # VERIFICAÇÃO
        # Esperamos que um erro do tipo 'ValueError' aconteça. Se acontecer, o teste passa!
        with self.assertRaises(ValueError):
            # AÇÃO
            self.gerenciador.adicionar_tarefa("   ") # Tenta adicionar uma tarefa só com espaços

    def test_3_nao_adicionar_tarefa_com_tipo_errado(self):
        """Verifica se o sistema impede a criação de uma tarefa que não seja texto."""
        print("Executando teste unitário 3: Tentar adicionar tarefa com número")

        # VERIFICAÇÃO
        with self.assertRaises(ValueError):
            # AÇÃO
            self.gerenciador.adicionar_tarefa(123) # Tenta adicionar um número

if __name__ == '__main__':
    unittest.main()




#python -m unittest testes/testes_unitarios/teste_gerenciador_tarefas.py