import psycopg2
from psycopg2 import sql

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

    def adicionar_contato(conn, nome, email, telefone):
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""
                    INSERT INTO Contato (nome, email, telefone) VALUES {nome}, {email}, {telefone}
                """)
                conn.commit()
                print("Dados inseridos com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")