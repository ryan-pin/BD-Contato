from conexao import Conexao
from modelos import contato 

conn = Conexao(
    "Cont", 
    "postgres", 
    "postgres", 
    "localhost", 
    "5432"
    )
conn.conectar()