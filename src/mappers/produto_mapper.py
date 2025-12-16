"""
Mapper para converter entre modelos ORM e entidades de domínio.
"""

from __future__ import annotations

from src.models.produto import Produto
from src.models.produto_db import ProdutoDB


class ProdutoMapper:
    """Conversor entre ProdutoDB (ORM) e Produto (entidade de domínio)."""

    @staticmethod
    def to_entity(produto_db: ProdutoDB) -> Produto:
        """
        Converte um modelo ORM (ProdutoDB) para entidade de domínio (Produto).
        
        Args:
            produto_db: Modelo ORM do banco de dados
            
        Returns:
            Produto: Entidade de domínio
        """
        return Produto(
            id_=produto_db.id,
            nome=produto_db.nome,
            preco=produto_db.preco,
            ativo=produto_db.ativo
        )

    @staticmethod
    def to_entities(produtos_db: list[ProdutoDB]) -> list[Produto]:
        """
        Converte uma lista de modelos ORM para entidades de domínio.
        
        Args:
            produtos_db: Lista de modelos ORM
            
        Returns:
            list[Produto]: Lista de entidades de domínio
        """
        return [ProdutoMapper.to_entity(produto_db) for produto_db in produtos_db]
