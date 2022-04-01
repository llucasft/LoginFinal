from multiprocessing.dummy import current_process
import db


def register():
    usuario = dict()
    usuario['nome'] = input('Digite seu nome: ')
    usuario['nick'] = input('Digite seu nick: ')

    registered = db.get_user(usuario['nick'])

    if registered:
        print('Usuário já cadastrado. ')
        return

    usuario['senha'] = input('Digite sua senha: ')
    
    db.insert(usuario["nome"], usuario["nick"], usuario["senha"])

    print(f'Usuário(a) {usuario["nick"]} cadastrado com sucesso. ')


def login():
    exist_user = False
    nick = input('Digite seu nick: ')
    exist_user = db.get_user(nick)

    if not exist_user:
        print('Usuário não cadastrado. ')
        return
    
    senha = input('Digite sua senha: ')
     
    if senha == exist_user[2]:
        print(f'Bem vindo(a) {exist_user[0]}')

    else:
        print('Usuário ou senha incorreto. ')


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
        db.close_conn()
        print("Saindo!")


if __name__ == '__main__':
    main()
