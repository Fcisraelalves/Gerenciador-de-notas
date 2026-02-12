from useful import Validator
from getpass import getpass
from auth import Auth
from database import DBLauncher
from crud import DatabaseManager

class App:
    
    def __init__(self, db_manager : DatabaseManager):
        self.db_manager = db_manager
        self.session_user = None

    def run(self):
        DBLauncher.create_tables()
        while True:
            self.print_main_menu()
            option = Validator.validate_option('Insira a opção correspondente: ', 3)
            print()
            if option == 1:
                while True:
                    user = str(input('Insira o seu usuário: '))
                    password = str(getpass('Insira a sua senha: '))
                    login_response = Auth.login(self.db_manager, user, password)
                    if login_response.status:
                        print(f'Login efetuado com sucesso!')
                        self.session_user = self.db_manager.find_user(user)
                        self.run_user_menu()
                    else:
                        print(f'Erro: Dados inválidos, tente novamente...')
            elif option == 2:
                while True:
                    user= str(input('Insira o seu usuário: '))
                    password_1 = str(getpass('Insira a sua senha: '))
                    password_2 = str(getpass('Confirme a sua senha: '))

                    if password_1 != password_2:
                        print(f'ERRO: As senhas não correspondem.')
                        continue
                    else:
                        self.db_manager.new_user(user, password_1)
                        print(f'Registrado com sucesso!')
                        break
            else:
                print(f'Encerrando app...')
                break

    def print_main_menu(self):
        print(f'\nGerenciador de Notas: \n')
        print(f'[1] Login\n[2] Registrar-se\n[3] Sair\n')

    def print_user_menu(self):
        print('\nGerenciador de Notas: ')
        print(f'Olá, {self.session_user.username}!\n')
        print(f'[1] Nova nota\n[2] Listar notas\n[3] Excluir nota\n[4] Logout\n')
    
    def run_user_menu(self):
        while True:
            self.print_user_menu()
            option = Validator.validate_option('Insira a opção correspondente: ', 4)

            if option == 1:
                text = str(input('Insira o texto da nota: '))
                self.db_manager.new_note(self.session_user.id, text)
                print(f'Nota adicionada com sucesso!')
            elif option == 2:
                pass
            elif option == 3:
                pass
            else:
                self.session_user = None
                break
