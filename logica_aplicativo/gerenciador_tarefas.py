# logica_aplicativo/gerenciador_tarefas.py


class GerenciadorDeTarefas:
    """
    Classe responsável pela lógica de negócio de uma lista de tarefas.
    """
    
    def __init__(self):
        # 1. Cria uma lista vazia chamada 'tarefas' dentro do objeto. 
        self.tarefas = []
        
        # 2. Cria um contador interno para os IDs, começando em 1.
        #    garante que cada tarefa terá um número de identificação único.
        self._proximo_id = 1

    # Esta é a função que adiciona uma nova tarefa. 
    # Ela recebe a 'descricao' da tarefa como um argumento.
    def adicionar_tarefa(self, descricao):
        """Adiciona uma nova tarefa à lista."""
        
        # --- REGRA IMPORTANTE ---
        # Esta linha verifica duas coisas:
        # 1. 'isinstance(descricao, str)': A descrição é um texto (string)?
        # 2. 'descricao.strip()': Se eu remover os espaços do início e do fim, sobra alguma coisa?
        # 'if not... or not...': Se a descrição NÃO for um texto OU se estiver vazia...
        if not isinstance(descricao, str) or not descricao.strip():
            # ...então, o programa deve levantar um erro
            # para impedir que dados inválidos entrem no sistema.
            raise ValueError("Descrição não pode ser vazia ou inválida.")
        
        # Se a descrição passou pela barreira , cria um "dicionário".
        # pra guardar dados com rótulos (chaves).
        nova_tarefa = {
            'id': self._proximo_id,          # O ID será o número atual do nosso contador.
            'descricao': descricao,         # A descrição é o texto que recebemos.
            'concluida': False              # Toda nova tarefa começa como "não concluída".
        }
        
        # Adiciona o dicionário 'nova_tarefa' na nossa lista principal 'self.tarefas'.
        self.tarefas.append(nova_tarefa)
        
        # Aumenta o contador de ID em +1 para a próxima tarefa.
        self._proximo_id += 1
        
        # Devolve a tarefa que acabou de ser criada.
        return nova_tarefa
    def listar_tarefas(self):
        """Devolve a lista completa de tarefas."""
        return self.tarefas
     
    # (No futuro, poder adicionar mais funções como remover,  etc.)
 

# Substitua o bloco if __name__ == "__main__": antigo por este:

if __name__ == "__main__":
    print("Bem-vindo(a) ao seu Gerenciador de Tarefas de Terminal!")
    meu_gerenciador = GerenciadorDeTarefas()
    
    while True:
       
        print("\n--- MENU ---")
        print("[1] Adicionar Tarefa")
        print("[2] Listar Tarefas")
        print("[3] Sair")
        print("------------")
        
        
        opcao = input("Escolha uma opção: ").strip()
        
       
        if opcao == "1": # Se o usuário digitou "1"
            descricao = input("Digite a descrição da nova tarefa: ")
            try:
                tarefa_adicionada = meu_gerenciador.adicionar_tarefa(descricao)
                print(f"SUCESSO: Tarefa '{tarefa_adicionada['descricao']}' adicionada!")
            except ValueError as e:
                print(f"ERRO: {e}")

        elif opcao == "2": # Se o usuário digitou "2"
            tarefas = meu_gerenciador.listar_tarefas()
            if not tarefas:
                print(">> Sua lista de tarefas está vazia.")
            else:
                print("\n--- Sua Lista de Tarefas ---")
                for t in tarefas:
                    status = "Concluída" if t['concluida'] else "Pendente"
                    
                    print(f"ID: {t['id']} | Descrição: {t['descricao']} | Status: {status}")
                print("--------------------------")

        elif opcao == "3": # Se o usuário digitou "3"
            print("Até logo!")
            break 
            
        else:
            print("ERRO: Opção inválida. Por favor, digite 1, 2 ou 3.")