class Validator:

    @classmethod
    def validar_opcao(cls, mensagem : str, max : int, min : int = 1):
        opcao = int(input(mensagem))
        while opcao < min or opcao > max:
            print(f'ERRO: selecione uma opção válida.')
            opcao = int(input(mensagem))
        return opcao
    