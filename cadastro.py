nome = ""
idade = ""
usuario = ""
senha = ""

login_usuario = ""
login_senha = ""

while True:
    print("==============")
    print("sistema de cadastro")
    print("==============")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao =input("EScolha uma opcao: ")
    if (opcao == "1")
        print("=======Tela de Cadastro=======") 
        print("==============================")
        nome = input("digite seu nome: ")
        idade = input("digite sua idade: ")
        usuario = input("digite seu usuario: ")
        senha = input("digite sua senha: ")
        print("\ncadastro realizado!\n")

    elif (opcao == "2"):
        print ("=============================")
        print ("===tela de login===") 
        print("==============================")
        login_usuario = input("digite o usuario cadastrado:  ")
        login_senha = input("digite a senha:  ")
        
        #processamento de usuario e senha
        if login_usuario == usuario and login_senha == senha :
            print("\nlogin realizado com sucesso!\n")
            print("bem vindo,", nome)
        else:
            print("usuario ou senha incorretos")

    elif(opcao == "3"):
        print("voce esta saindo do aplicativo, ate mais!")
        break 
    else:
        print("Valor digitado, invalido, use apenas números inteiros do menu")    
