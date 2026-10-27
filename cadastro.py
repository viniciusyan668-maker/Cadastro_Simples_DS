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
    if (opcao == "1"):
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
            while True:
                print("\nlogin realizado com sucesso!\n")
                print("bem vindo,", nome)
                print("\n======Área do usuario======\n")
                print("1 - ver os dados cadastrados")
                print("2 - voltar para o menu anterior")

                usuario_opcao = input("\nescolha umas das opcoes do menu acima: \n")

                if (usuario_opcao == "1"):
                    print("\n============")
                    print("===dados cadastrados===")
                    print("============\n")
                elif(usuario_opcao == "2"):
                    print("\n  voce esta voltando para o menu anterior!")
                    break
                else:
                    print("\n opcao digitada invalida, use os numeros do menu!")
        
        else:
            print("\nusuario ou senha incorretos\n")

    elif(opcao == "3"):
        print("\nvoce esta saindo do aplicativo, ate mais!\n")
        break 