from validator import Validator

class App:

    def run(self):
        while True:
            self.print_main_menu()
            opcao = Validator.validar_opcao('Insira a opção correspondente: ', 3)
            print()
            if opcao == 1:
                pass
            elif opcao == 2:
                pass
            else:
                pass

    def print_main_menu(self):
       print(f'Gerenciador de Notas: \n')
       print(f'[1] Login\n[2] Registrar-se\n[3] Sair\n')

    