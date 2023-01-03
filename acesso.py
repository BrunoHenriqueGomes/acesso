def acesso (*args):

    senha = 1234
    nome = "bruno"
    tentativas = 5  

    while tentativas > 0 :
        tentativas = tentativas - 1

        usuario = input("por favor digite seu nome : ")
        acesso = int(input("agora digite a senha : "))

        if nome == usuario and senha == acesso :
            print("seja bem vindo" , nome )
            break

        else:
            print("ACESSO NEGADO usuário ou senha incorreto !")

        if tentativas == 0 :
            print("EXECESSO DE TENTATIVAS VOCÊ FOI BLOQUEADO !")
        
acesso()