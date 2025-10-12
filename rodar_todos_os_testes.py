# PROJETO_QUALIDADE_SAUCEDEMO/rodar_todos_os_testes.py

# PROJETO_QUALIDADE_SAUCEDEMO/rodar_todos_os_testes.py

import unittest
import HtmlTestRunner

# Este script agora imita o comando 'python -m unittest discover'
# para garantir que todos os testes sejam encontrados.

# 1. Cria uma "suite de testes" (um pacote de testes) que usa o método 'discover'
#    para encontrar todos os testes na pasta 'testes'.
suite_de_testes = unittest.TestLoader().discover('testes')

# 2. Define a pasta onde queremos salvar os relatórios.
pasta_relatorios = 'testes_resultado'

# 3. Configura o nosso Executor de Testes para gerar o relatório HTML.
executor = HtmlTestRunner.HTMLTestRunner(
    output=pasta_relatorios,
    report_name="RelatorioFinalDeTestes",
    combine_reports=True,
    report_title="Relatorio de Execucao de Testes Automatizados"
)

# 4. Finalmente, executa a suite de testes completa.
print("Iniciando a execucao de TODOS os testes para gerar o relatorio...")
executor.run(suite_de_testes)
print("\nExecucao finalizada com sucesso!")
print(f"O relatorio 'RelatorioFinalDeTestes.html' foi salvo na pasta '{pasta_relatorios}'.")

#rodar o teste no terminal python rodar_todos_os_testes.py