class Validator:

    @classmethod
    def validar_option(cls, message : str, max : int, min : int = 1):
        option = int(input(message))
        while option < min or option > max:
            print(f'ERRO: selecione uma opção válida.')
            option = int(input(message))
        return option
    