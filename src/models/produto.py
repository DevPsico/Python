
# src/models/produto.py

from __future__ import annotations

class Produto:
    def __init__(self, id_: int, nome: str, preco: float, ativo: bool = True) -> None:
        self._id: int = id_
        self.nome: str = nome
        self._preco: float = preco
        self.ativo: bool = ativo

    def __str__(self) -> str:
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco:.2f}, ativo={self.ativo})"

    @property
    def id(self) -> int:
        """ID somente leitura."""
        return self._id

    @property
    def preco(self) -> float:
        """Getter para preço."""
        return self._preco

    @preco.setter
    def preco(self, valor: float) -> None:
        """Setter para preço (com validação)."""
        if valor < 0:
            raise ValueError("preco não pode ser negativo")
        self._preco = valor

    def aplicar_desconto(self, percentual: float) -> None:
        """
        Aplica um desconto percentual ao preço do produto.
        Ex.: percentual=10 -> reduz 10% do preço atual.
        """
        if percentual < 0 or percentual > 100:
            raise ValueError("percentual deve estar entre 0 e 100")

        desconto = self.preco * (percentual / 100)
        self.preco -= desconto


# Executa apenas quando este arquivo for rodado diretamente
if __name__ == "__main__":
    # Teste 1: imprimir produto
    produto = Produto(2, "Caneta", 2.50)
    print(produto)  # Produto(id=2, nome='Caneta', preco=2.50, ativo=True)

    # Teste 2: aplicar desconto e imprimir
    p1 = Produto(1, "Caderno", 15.00)
    p1.aplicar_desconto(10)  # Aplica 10% de desconto
