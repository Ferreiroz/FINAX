Finaxis – Sistema de Gestão Financeira (CLI)

Um sistema de controle financeiro pessoal desenvolvido em Python, aplicando POO (Programação Orientada a Objetos) com abstração, herança, polimorfismo e encapsulamento, além de separação clara de camadas (UI, Models, Services e Persistence).

O projeto permite registrar receitas, despesas e investimentos, gerar relatórios e exportar os dados para uma planilha Excel.

📂 Arquitetura do Projeto
Finaxis/
│── main.py
│── ui.py
│── models.py
│── service.py
│── persistence.py
│── utils.py  (opcional – ex: format_currency)
│── README.md

✔ Separação de responsabilidades
Arquivo	Responsabilidade
models.py	Classes de domínio (Entry, Categoria, Receita, Despesa, Investimento).
service.py	Regras de negócio (cadastro, cálculo, relatórios).
persistence.py	Persistência em planilha Excel usando openpyxl.
ui.py	Interface de linha de comando (CLI).
main.py	Ponto de entrada da aplicação.
🧠 Princípios de POO utilizados
✔ Abstração

A classe abstrata AccountCategory define a interface comum para Receitas, Despesas e Investimentos.

✔ Herança

Income, Expense e Investment herdam de AccountCategory.

✔ Polimorfismo

Cada categoria implementa seu próprio método report_line().

✔ Encapsulamento

Atributos internos (_entries, _nome, etc.) protegidos com propriedades.

🛠 Funcionalidades

Cadastro de categorias financeiras (receitas, despesas, investimentos)

Inserção de transações

Relatório formatado no terminal

Cálculo automático de saldo

Exportação para arquivo Excel (.xlsx)

Carregamento posterior dos dados (via Excel)

Interface simples de texto (CLI)

▶️ Como executar
1. Instale as dependências
pip install openpyxl

2. Execute o programa
python main.py

📌 Comandos disponíveis no CLI
Adicionar uma transação
add


O sistema pedirá:

Categoria

Descrição

Valor

Exibir relatório
report


Mostra receitas, despesas, investimentos e saldo estimado.

Salvar em Excel
save


Gera um arquivo .xlsx com todas as entradas.

Encerrar
exit

📊 Exemplo de relatório
Receitas: +R$ 3200.00
Despesas Fixas: -R$ 1500.00
Despesas Variáveis: -R$ 820.50
Investimentos (Investimento): R$ 500.00
Saldo estimado: R$ 879.50

📁 Exportação para Excel

O arquivo gerado inclui:

Nome do usuário

Data e hora da criação

Lista completa de transações

As colunas são:

Categoria

Descrição

Valor (R$)

🧩 Tecnologias utilizadas

Python 3.10+

openpyxl (para manipulação de Excel)

Princípios de POO e Clean Architecture

🏆 Objetivo do Projeto

Demonstrar uma aplicação organizada, modular e orientada a objetos, ideal para:

estudos de boas práticas em Python

projetos acadêmicos

demonstração de domínio de POO

fundamentação para aplicações maiores (REST API, GUI, etc.)

📄 Licença

Este projeto é de uso livre para fins educacionais.
