from models import Income, Expense, Investment, AccountCategory
from typing import List


class FinanceService:
	def __init__(self):
		# Mantemos as categorias como objetos, separação de responsabilidades
		self._categories: List[AccountCategory] = []

	def create_category(self, tipo: str, nome: str) -> AccountCategory:
		tipo_map = {
			'receita': Income,
			'despesa': Expense,
			'investimento': Investment,
		}
		cls = tipo_map.get(tipo.lower())
		if cls is None:
			raise ValueError(f"Tipo desconhecido: {tipo}")
		cat = cls(nome)
		self._categories.append(cat)
		return cat

	def categories(self) -> List[AccountCategory]:
		return list(self._categories)

	def total_balance(self) -> float:
		total_receitas = sum(c.total() for c in self._categories if isinstance(c, Income))
		total_despesas = sum(c.total() for c in self._categories if isinstance(c, Expense))
		# investimentos considerados neutros para saldo (exemplo)
		return total_receitas - total_despesas

	def find_by_name(self, nome: str):
		for c in self._categories:
			if c.nome.lower() == nome.lower():
				return c
		return None

	def report(self) -> str:
		lines = [c.report_line() for c in self._categories]
		lines.append(f"Saldo estimado: R$ {self.total_balance():.2f}")
		return "\n".join(lines)