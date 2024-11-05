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

    elif opcao == 2:
        id_contato = int(input("Digite o ID do contato para ler: "))                        
        
        if conn:
            contatos = conn.ler_contato(id_contato)
            for informacao in contatos:
                print(informacao)
    
    elif opcao == 3:
        id_contato = int(input("Digite o ID do contato que deseja atualizar: ")) 

        nome = input("Digite o novo nome do contato: ")
        email = input("Digite o novo email do contato: ")
        telefone = input("Digite o novo telefone do contato: ")
        
        contato = Contato(id_contato ,nome, email, telefone)

        if conn:
            contato = conn.atualizar_contato(conn, contato)
        
    elif opcao == 4:
        id_contato = int(input("Digite o ID do contato que deseja deletar: "))  

        if conn.conexao:
            conn.deletar_contato(id_contato)
    
    # SAIR
    elif opcao == 0:
        break

