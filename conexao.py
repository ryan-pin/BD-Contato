import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError

from modelos.Contato import Contato

class Conexao:
    
    def __init__(self, nome_db, usuario, senha, host, porta):
        self.nome_db = nome_db
        self.usuario = usuario
        self.senha = senha
        self.host = host
        self.porta = porta
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                database=self.nome_db,
                user=self.usuario,
                password=self.senha,
                host=self.host,
                port=self.porta
            )
            print("Conexão ao banco de dados PostgreSQL realizada com sucesso")
        except OperationalError as e:
            print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")

    # Funções de CRUD

    def adicionar_contato(self, conn, contato):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return    
        
        try:
            cursor = self.conexao.cursor()
            query = f"""
                INSERT INTO Contato (nome, email, telefone) 
                VALUES ({contato.nome}, {contato.email}, {contato.telefone})
            """
            cursor.execute(query, (contato.nome, contato.email, contato.telefone))
            conn.commit()
            print("Dados inseridos com sucesso.")
        except OperationalError as e:
            print(f"Ocorreu um erro ao criar um novo contato: {e}")
            return
