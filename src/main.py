from __future__ import annotations
from typing import List
from fastapi import FastAPI, HTTPException, status

from src.models.produto_schemas import ProdutoCreate, ProdutoRead, ProdutoUpdate
from src.services.produto_repo_memory import ProdutoRepoMemory
from src.services.produto_service import ProdutoService

app = FastAPI(
    title="API de Gestão de Produtos",
    version="1.0.0",
    description="Uma API simples para gerenciar produtos usando FastAPI."
    )

# Instanciar o serviço de produtos
repo = ProdutoRepoMemory()
service = ProdutoService(repo)

"""Endpoints para CADASTRAR produtos."""
@app.post("/produtos/", response_model=ProdutoRead, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreate) -> ProdutoRead:
    novo_produto = service.criar_produto(
        nome=produto.nome,
        preco=produto.preco,
        ativo=produto.ativo
    )
    return ProdutoRead.from_orm(novo_produto)

"""Endpoints para PEGAR 1 produto."""
@app.get("/produtos/{produto_id}", response_model=ProdutoRead, tags=["healthcheck"])
def obter_produto(produto_id: int) -> ProdutoRead:
    produto = service.obter_produto(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return ProdutoRead.from_orm(produto)

"""Endpoints para LISTAR produtos."""
@app.get("/produtos/", response_model=List[ProdutoRead])
def listar_produtos() -> List[ProdutoRead]:
    produtos = service.listar_produtos()
    return [ProdutoRead.from_orm(produto) for produto in produtos]

"""Endpoints para ATUALIZAR produtos."""
@app.put("/produtos/{produto_id}", response_model=ProdutoRead)
def atualizar_produto(produto_id: int, produto_atualizado: ProdutoUpdate) -> ProdutoRead:
    produto = service.atualizar_produto(
        produto_id,
        nome=produto_atualizado.nome,
        preco=produto_atualizado.preco,
        ativo=produto_atualizado.ativo
    )
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return ProdutoRead.from_orm(produto)

"""Endpoints para DELETAR produtos."""
@app.delete("/produtos/{produto_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def deletar_produto(produto_id: int) -> None:
    sucesso = service.deletar_produto(produto_id)
    if not sucesso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")