from conexao import Conexao
from modelos.Contato import Contato 

conn = Conexao(
    "Cont", 
    "postgres", 
    "postgres", 
    "localhost", 
    "5432"
    )
conn.conectar()

while(True):
    #Menu com funções
    print("1 - Criar um contato")
    print("2 - Listar um contato específico")
    print("3 - Atualizar um contato")
    print("4 - Remover um contato especifico")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:

        nome = input("Digite o nome do contato: ")
        email = input("Digite o email do contato: ")
        telefone = input("Digite o telefone do contato: ")
        
        contato = Contato(nome, email, telefone)

        if conn:
            contato = conn.adicionar_contato(conn, contato)

    if opcao == 0:
        exit()

