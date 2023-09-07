print("Bem vindo a sistema")

print("Digite 1 se deseja cadastrar")
print("Digite 2 se deseja entrar no sistema")
print("Digite 3 se deseja sair do sistema")
login = ""
senha = ""

while True:
    escolha = int(input("Escolha uma Opção: "))

    if escolha == 1: 
        login = input("Insira o login: ")
        senha = input("Insira o senha: ")
        print("Login e senha salvos conm sucesso!")
        


    elif escolha == 2: 
        cadastro_login = input("Insira o login: ")
        cadastro_senha = input("Insira o senha: ")
    
        if cadastro_login == login and cadastro_senha == senha:
            print("Acesso concedido")
        else:
            print("Usuario ou senha incorretos")

    else:
        print("Logout concluido")
        break
