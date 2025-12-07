from abc import ABC, abstractmethod
from typing import List


class Entry:
    """Representa uma linha financeira (categoria, descrição, valor)."""

    def __init__(self, categoria: str, descricao: str, valor: float):
        self._categoria = categoria
        self._descricao = descricao
        self._valor = float(valor)

    @property
    def categoria(self):
        return self._categoria

    @property
    def descricao(self):
        return self._descricao

    @property
    def valor(self):
        return self._valor

    def __repr__(self):
        return (
            f"Entry(categoria={self._categoria!r}, "
            f"descricao={self._descricao!r}, valor={self._valor})"
        )


class AccountCategory(ABC):
    """Classe abstrata que define a interface para categorias financeiras."""

    def __init__(self, nome: str):
        self._nome = nome
        self._entries: List[Entry] = []

    @property
    def nome(self) -> str:
        return self._nome

    def add_entry(self, descricao: str, valor: float):
        if not isinstance(valor, (int, float)):
            raise TypeError("Valor deve ser numérico")

        entry = Entry(self._nome, descricao, valor)
        self._entries.append(entry)
        return entry

    def entries(self) -> List[Entry]:
        return list(self._entries)  # cópia para proteção (encapsulamento)

    @abstractmethod
    def total(self) -> float:
        pass

    @abstractmethod
    def report_line(self) -> str:
        pass


class Income(AccountCategory):
    def total(self) -> float:
        return sum(e.valor for e in self._entries)

    def report_line(self) -> str:
        return f"{self._nome}: +R$ {self.total():.2f}"


class Expense(AccountCategory):
    def total(self) -> float:
        return sum(e.valor for e in self._entries)

    def report_line(self) -> str:
        return f"{self._nome}: -R$ {self.total():.2f}"


class Investment(AccountCategory):
    def total(self) -> float:
        return sum(e.valor for e in self._entries)

    def report_line(self) -> str:
        return f"{self._nome} (Investimento): R$ {self.total():.2f}"
