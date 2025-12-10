
# src/models/produto.py

class Produto:
    def __init__(self, id: int, nome: str, preco: float, ativo: bool = True) -> None:
        self.id: int = id
        self.nome: str = nome
        self.preco: float = preco
        self.ativo: bool = ativo

    def __str__(self) -> str:
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco}, ativo={self.ativo})"

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
    print(produto)

    # Teste 2: aplicar desconto e imprimir
    p1 = Produto(1, "Caderno", 15.00)
    p1.aplicar_desconto(10)
    print(p1)  # Deve mostrar o preço com 10% de desconto
