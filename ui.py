# ui.py
from service import FinanceService
from persistence import ExcelPersistence


class CLI:
    def __init__(self):
        self._svc = FinanceService()

    def run(self):
        print("=== Finaxis - CLI ===")

        nome = input("Nome do usuário: ").strip() or "Usuário"

        # criar categorias base
        self._svc.create_category('receita', 'Receitas')
        self._svc.create_category('despesa', 'Despesas Fixas')
        self._svc.create_category('despesa', 'Despesas Variáveis')
        self._svc.create_category('investimento', 'Investimentos')

        while True:
            cmd = input('\nComandos: [add, report, save, exit] > ').strip().lower()

            if cmd == 'add':
                nome_cat = input('Categoria (nome exato): ').strip()
                cat = self._svc.find_by_name(nome_cat)

                if not cat:
                    print('Categoria não encontrada. Use exatamente o nome criado.')
                    continue

                desc = input('Descrição: ').strip()
                val = float(input('Valor (use . para decimal): '))
                cat.add_entry(desc, val)

                print('Entrada adicionada.')

            elif cmd == 'report':
                print('\n' + self._svc.report())

            elif cmd == 'save':
                path = input('Caminho do arquivo de saída (ex: finaxis_saida.xlsx): ').strip() or 'finaxis_saida.xlsx'
                pers = ExcelPersistence(path)
                pers.save(self._svc.categories(), nome)

                print(f'Salvo em: {path}')

            elif cmd == 'exit':
                print('Saindo...')
