from useful import Validator, SystemMessages, Encryptor, Response
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
                        print(SystemMessages.SUCCESSFUL_LOGIN)
                        self.session_user = self.db_manager.find_user(user)
                        self.run_user_menu()
                        break
                    print(f'Erro: {login_response.error}')
            elif option == 2:
                while True:
                    user_response = Validator.validate_user(self.db_manager)
                    if not user_response.status:
                        print(f'ERRO: {user_response.error}')
                        continue
                    response = Validator.validate_two_passwords()
                    if response.status:
                        password_hash = Encryptor.to_hash(response.data['password'])
                        self.db_manager.new_user(user_response.data['username'], password_hash)
                        print(SystemMessages.SUCCESFUL_REGISTER)
                        break
                    print(f'ERRO: {response.error}')
            else:
                print(SystemMessages.EXIT_APP)
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
                print(SystemMessages.SUCCESSFUL_CREATED_NOTE)
            elif option == 2:
               response = self.view_notes()
               if not response.status:
                   print(f'    {response.data["message"]}')
            elif option == 3:
                response = self.view_notes()
                if response.status:
                    note_id = self.select_note()
                    self.db_manager.delete_note(note_id)
                    print(SystemMessages.SUCCESSFUL_EXCLUDED_NOTE)
                else:
                    print(f'    {response.data["message"]}')
            else:
                self.session_user = None
                break
    
    def view_notes(self):
        notes = self.db_manager.list_notes(self.session_user.id)
        if notes:
            for i, note in enumerate(notes, start=1):
                print(f'    {i} | {note.text}')
            return Response(status=True)
        else:
            return Response(status=False, data={'message' : SystemMessages.NOTHING_TO_VIEW})
        
    def select_note(self):
        notes = self.db_manager.list_notes(self.session_user.id)
        option = Validator.validate_option('Selecione o id tarefa que deseja excluir: ', len(notes))
        return notes[option-1].id
    
