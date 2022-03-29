import db


def register():
    usuario = dict()
    usuario['nome'] = input('Digite seu nome: ')
    usuario['nick'] = input('Digite seu nick: ')

    registered = db.mod_verifier(usuario['nick'])

    if registered:
        print('Usuário já cadastrado. ')
        return

    usuario['senha'] = input('Digite sua senha: ')
    
    db.insert(usuario["nome"], usuario["nick"], usuario["senha"])

    print(f'Usuário(a) {usuario["nick"]} cadastrado com sucesso. ')


def login():
    current_user = ()
    nick = input('Digite seu nick: ')
    current_user = db.mod_verifier(nick)
    if current_user:
        senha = input('Digite sua senha: ')
        if senha == current_user[2]:
            print(f'Bem vindo(a) {current_user[0]}')
        else:
            print('Usuário ou senha incorreto. ')
    else:
        print('Usuário não cadastrado. ')


def main():
    opcao = int(input(
        "Digite a opção:\n* 1 - Login\n* 2 - Cadastro\n* 3 - Sair\n-> "
    ))

    if opcao == 1:
        login()
        main()

    elif opcao == 2:
        register()
        main()

    else:
        print("Saindo!")


if __name__ == '__main__':
    main()
