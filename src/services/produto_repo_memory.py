from __future__ import annotations
from typing import List, Optional, Dict

from src.models.produto import Produto
from src.services.produto_repo_base import ProdutoRepoBase

class ProdutoRepoMemory(ProdutoRepoBase):
    """Implementação em memória do repositório de produtos."""

    def __init__(self) -> None:
        self._produtos: Dict[int, Produto] = {}
        self._proximo_id: int = 1

    def adicionar(self, produto: Produto) -> None:
        produto._id = self._proximo_id  # Atribui o próximo ID disponível
        self._produtos[self._proximo_id] = produto
        self._proximo_id += 1

    def obter_por_id(self, id_: int) -> Optional[Produto]:
        return self._produtos.get(id_)

    def listar_todos(self) -> List[Produto]:
        return list(self._produtos.values())

    def atualizar(self, produto: Produto) -> None:
        if produto.id in self._produtos:
            self._produtos[produto.id] = produto
        else:
            raise ValueError(f"Produto com ID {produto.id} não encontrado.")

    def remover(self, id_: int) -> None:
        if id_ in self._produtos:
            del self._produtos[id_]
        else:
            raise ValueError(f"Produto com ID {id_} não encontrado.")