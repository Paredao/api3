from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    ip: int

class ProdutoResponse(BaseModel):
    ip: int

    class Config:
        orm_mode=True

