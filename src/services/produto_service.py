from __future__ import annotations
from typing import List, Optional

from src.models.produto import Produto
from src.services.produto_repo_base import ProdutoRepoBase

class ProdutoService:
    """Serviço para gerenciar produtos."""

    def __init__(self, repo: ProdutoRepoBase) -> None:
        self._repo = repo

    def criar_produto(self, nome: str, preco: float, ativo: bool = True) -> Produto:
        """Cria e adiciona um novo produto."""
        novo_id = self._gerar_novo_id()
        produto = Produto(novo_id, nome, preco, ativo)
        self._repo.adicionar(produto)
        return produto

    def obter_produto(self, id_: int) -> Optional[Produto]:
        """Obtém um produto pelo ID."""
        return self._repo.obter_por_id(id_)

    def listar_produtos(self) -> List[Produto]:
        """Lista todos os produtos."""
        return self._repo.listar_todos()

    def atualizar_produto(self, id_: int, nome: Optional[str] = None,
                          preco: Optional[float] = None,
                          ativo: Optional[bool] = None) -> Optional[Produto]:
        """Atualiza os dados de um produto existente."""
        produto = self._repo.obter_por_id(id_)
        if not produto:
            return None

        if nome is not None:
            produto.nome = nome
        if preco is not None:
            produto.preco = preco
        if ativo is not None:
            produto.ativo = ativo

        self._repo.atualizar(produto)
        return produto

    def remover_produto(self, id_: int) -> bool:
        """Remove um produto pelo ID."""
        produto = self._repo.obter_por_id(id_)
        if not produto:
            return False

        self._repo.remover(id_)
        return True

    def _gerar_novo_id(self) -> int:
        """Gera um novo ID para o produto."""
        produtos = self._repo.listar_todos()
        if not produtos:
            return 1
        return max(produto.id for produto in produtos) + 1