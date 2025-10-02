# api3 - criar uma api com sqlite para cadastrar, listar e buscar produto pelo id

# no terminal, após a criação de todos os arquivos

python3 -m venv venv source venv/bin/activate #Linux e Mac
venv\Scripts\activate #Windows

pip install -r requirements.txt

# isso instalará as bibliotecas necessárias para rodar a aplicação

# após isso, é só rodar a aplicação

uvicorn main:app --reload
