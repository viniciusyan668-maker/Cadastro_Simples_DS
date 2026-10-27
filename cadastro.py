#Variaveis para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""

 #variaveis para login
login_usuario = ""
login_usuario = ""

#variaveis de controle
controle_cadastro = ""

#Apenas a tela de Visualização
while True:
    controle_cadastro = "2"
    print("===================")
    print("Sistema de Cadastro")
    print("===================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input("Escolha uma opcaão: ")
    #Funcionalidades
    #Se o usuario digitar o Valor 1, vai ser exebido
    #  a ação abaixo:
    if (opcao == "1"):
         while controle_cadastro != "1" :
            print("==========================")
            print("=====Tela de Cadastro=====")
            print("==========================")
            nome =input("Digite o seu nome: ")
            idade =input("Digite a sua idade: ")
            usuario =input ("Digite o seu usuario: ")
            senha =input("Digite a sua senha  ")

            controle_cadastro = input("\n voce deseja voltar para a tela anterior ? \n 1)-voltar para o menu anterior;\n digite qualquer tecla para refazer o cadastro;\n")

            if(controle_cadastro == "1")
                 print("\n cadastro realizado!\n")
            else:
                 print("valor digitado invalido, faça o  cadastro novamente")
    #Se digititar 2, abre a tela de login
    elif (opcao == "2"):
        print("=========================")
        print("======Tela de Login======")
        print("=========================")
        login_usuario = input("Digite o usuário cadastrado: ")
        login_senha = input("Digite a senha : ")

    #Processamento de usuário e senha 
    if login_usuario == usuario and login_senha == senha  : 
        while True:
            print("\nLogin realiza com sucesso!\n")
            print("bem vindo,", nome)
            print("\n=====Àrea do usuário=====\n")
            print("1 - ver os dados cadastrados")
            print("2- Voltar para o menu anterior")

            usuario_opcao = input("\nEscolha uma das opções do menu a acima")

            if (usuario_opcao == "1"):
                print("\n=====================")
                print("===Dados cadastrados===")
                print("=====================\n")
                #Mostrar dados do usuário
                print("Nome de usuário: ", nome)
                print("Idade do usuário: ", idade)
                print("Senha do usuário: ", senha)
            elif(usuario_opcao == "2"):
                print("\n você está voltando para o menu anterior")
                break
            elif(usuario_opcao == "3"):
                senha = input("\ndigite a nova senha: ")
            else:
                print("\n opção digitada invalida, use os numeros do menu !")

     #Se não estiver correto entra no caso abaixo
        else:
         print("\nUsuário ou senha incorretos\n")

    #Se digitar 3, sai da execução
    elif (opcao == "3"):
        print("Você está saindo do cadastro, até mais!")
        break
        #Se não for nem 1,2 ou 3 mostrar erro e repetir código
else:
         print("Valor digitado inválido, use apenas números inteiros do menu ")
        