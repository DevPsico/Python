from __future__ import annotations
from typing import List, Optional

from sqlalchemy.orm import Session

from src.models.produto import Produto
from src.models.produto_db import ProdutoDB
from src.services.produto_repo_base import ProdutoRepoBase
from src.mappers.produto_mapper import ProdutoMapper

class ProdutoRepoSQLAlchemy(ProdutoRepoBase):
    """Implementação do repositório de produtos usando SQLAlchemy."""

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def criar_produto(self, nome: str, preco: float, ativo: bool = True) -> Produto:
        novo_produto_db = ProdutoDB(nome=nome, preco=preco, ativo=ativo)
        self.db_session.add(novo_produto_db)
        self.db_session.commit()
        self.db_session.refresh(novo_produto_db)
        return ProdutoMapper.to_entity(novo_produto_db)

    def obter_produto_por_id(self, produto_id: int) -> Optional[Produto]:
        produto_db = self.db_session.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        return ProdutoMapper.to_entity(produto_db) if produto_db else None

    def listar_produtos(self) -> List[Produto]:
        produtos_db = self.db_session.query(ProdutoDB).all()
        return ProdutoMapper.to_entities(produtos_db)

    def atualizar_produto(self, produto_id: int, nome: Optional[str] = None,
                          preco: Optional[float] = None, ativo: Optional[bool] = None) -> Optional[Produto]:
        produto_db = self.db_session.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        if not produto_db:
            return None
        if nome is not None:
            produto_db.nome = nome
        if preco is not None:
            produto_db.preco = preco
        if ativo is not None:
            produto_db.ativo = ativo
        self.db_session.commit()
        self.db_session.refresh(produto_db)
        return ProdutoMapper.to_entity(produto_db)

    def deletar_produto(self, produto_id: int) -> bool:
        produto_db = self.db_session.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        if not produto_db:
            return False
        self.db_session.delete(produto_db)
        self.db_session.commit()
        return True
