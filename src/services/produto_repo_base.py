from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional

from src.models.produto import Produto

class ProdutoRepoBase(ABC):
    """Interface base para repositórios de produtos."""

    @abstractmethod
    def adicionar(self, produto: Produto) -> None:
        """Adiciona um novo produto ao repositório."""
        raise NotImplementedError
        pass

    @abstractmethod
    def obter_por_id(self, id_: int) -> Optional[Produto]:
        """Obtém um produto pelo seu ID."""
        raise NotImplementedError
        pass

    @abstractmethod
    def listar_todos(self) -> List[Produto]:
        """Lista todos os produtos no repositório."""
        raise NotImplementedError
        pass

    @abstractmethod
    def atualizar(self, produto: Produto) -> None:
        """Atualiza um produto existente no repositório."""
        raise NotImplementedError
        pass

    @abstractmethod
    def remover(self, id_: int) -> None:
        """Remove um produto do repositório pelo seu ID."""
        raise NotImplementedError
        pass
