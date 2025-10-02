from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.post("/Produtos/", response_model=schemas.ProdutoResponse)
def create_produto(produto:schemas.ProdutoCreate, db:Session=Depends(get_db)):
    db_produto=crud.get_produto(db, ip=produto.ip)
    if db_produto:
        raise HTTPException(status_code=400, detail="IP já cadastrado.")
    return crud.create_produto(db=db, produto=produto)

@app.get("/Produtos/{produto_ip}", response_model=schemas.ProdutoResponse)
def read_produto(produto_ip:int, db:Session=Depends(get_db)):
    db_produto=crud.get_produto(db, produto_ip=produto_ip)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="IP não encontrado.")
    return db_produto

@app.delete("/Produtos/{produto_ip}")
def delete_produto(produto_ip:int, db:Session=Depends(get_db)):
    db_produto=crud.get_produto(db, produto_ip=produto_ip)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="IP não encontrado.")
    crud.delete_produto(db=db, produto_ip=produto_ip)
    return{"message": "Ip deletado com sucesso."}
