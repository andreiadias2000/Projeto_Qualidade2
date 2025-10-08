# Projeto de Testes Automatizados - Qualidade de Software

Este projeto foi desenvolvido para a disciplina de Qualidade de Software, com o objetivo de demonstrar a aplicação de testes de sistema e testes unitários em uma aplicação web.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Automação de UI (Testes de Sistema):** Playwright
* **Framework de Teste:** Unittest (biblioteca padrão do Python)

---

## 🧪 Testes Implementados

O projeto conta com os seguintes cenários de teste automatizados:

### Testes de Sistema (contra o site `saucedemo.com`)

1.  **Cenário de Login:**
    * `test_login_com_sucesso`: Verifica o login com credenciais válidas.
    * `test_login_com_senha_invalida`: Verifica a mensagem de erro para senhas incorretas.
    * `test_login_com_usuario_bloqueado`: Verifica a mensagem de erro para usuários bloqueados.
    * `test_login_com_usuario_nao_cadastrado`: Verifica a mensagem de erro para usuários inexistentes.

2.  **Cenário de Carrinho de Compras:**
    * `test_1_adiciona_um_item`: Verifica se um item é adicionado ao carrinho com sucesso.
    * `test_2_adiciona_e_remove_item`: Verifica a funcionalidade de adicionar e depois remover um item.
    * `test_3_adiciona_varios_itens`: Verifica se o contador do carrinho funciona para múltiplos itens.

### Testes Unitários

1.  **Cenário de Gerenciador de Tarefas:**
    * `test_1_adicionar_tarefa_valida`: Testa a lógica de adicionar uma tarefa válida.
    * `test_2_nao_adicionar_tarefa_vazia`: Testa a regra de negócio que impede tarefas vazias.
    * `test_3_nao_adicionar_tarefa_com_tipo_errado`: Testa a regra que impede que dados inválidos sejam adicionados.

---

## 🚀 Como Rodar os Testes

Com o ambiente Python e as dependências do `requirements.txt` instaladas, execute os seguintes comandos a partir da pasta raiz do projeto:
## 🚀 Como Rodar os Testes

Com o ambiente Python e as dependências do `requirements.txt` instaladas, execute os seguintes comandos a partir da pasta raiz do projeto:

### Para rodar os testes de login:
python -m unittest testes/testes_de_sistema/test_login_saucedemo.py

### para rodar os testes de carrinho:
python -m unittest testes/testes_de_sistema/test_carrinho_de_compras.py

### para rodar os testes unitarios:
python -m unittest testes/testes_unitarios/test_gerenciador_tarefas.py



