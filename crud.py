from sqlalchemy.orm import Session
from .models import Produto
from .schemas import ProdutoCreate

def get_produto(db:Session, produto_ip:int):
    return db.query(Produto).filter(Produto.ip==produto_ip).first()

def create_produto(db:Session, produto:ProdutoCreate):
    db_produto=Produto(name=produto.name)
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def delete_produto(db:Session, produto_ip:int):
    produto=db.query(Produto).filter(Produto.ip==produto_ip).first()
    db.delete(produto)
    db.commit
