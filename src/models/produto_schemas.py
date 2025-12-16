from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field

class ProdutoBase(BaseModel):
    nome: str = Field(..., title="Nome do Produto", min_length=3, max_length=100)
    preco: float = Field(..., gt=0, title="Preço do Produto", description="Deve ser maior que zero")
    ativo: bool = Field(default=True, title="Indica se o produto está ativo")


class ProdutoCreate(ProdutoBase):
    """ DTO para criação de um novo produto. """
    pass


class ProdutoUpdate(ProdutoBase):
    """ DTO para atualização de um produto existente. """
    nome: Optional[str] = Field(None, title="Nome do Produto", min_length=3, max_length=100)
    preco: Optional[float] = Field(None, gt=0, title="Preço do Produto", description="Deve ser maior que zero")
    ativo: Optional[bool] = Field(None, title="Indica se o produto está ativo")


class ProdutoRead(ProdutoBase):
    """ DTO para leitura de dados do produto, incluindo o ID. """
    id: int = Field(..., title="ID do Produto")

    class Config:
        from_attributes = True