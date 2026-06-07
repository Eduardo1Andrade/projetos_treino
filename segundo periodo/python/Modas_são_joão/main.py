''' aqui é o código principal'''
import functions
import dados

print("Sistema de Gerenciamento de Registro de Vendas Modas São Jõao")

def main():
    while True:
        print("digite a função que deseja utilizar")
        comando = input('''opções:
            Criar Registro[1],
            Editar Registro[2],
            Excluir Registro[3],
            Listar Registro[4],
            Buscar Registro[5],
            Fazer Relátorio de Vendas[6]
            Sair[7]
            : ''')

        if comando == "1":
            print("você escolheu Criar Registro!!")
            functions.criar_novo_registro()
            print(dados.dicionario_registros)
        elif comando == "2":
            print("você escolheu Editar Registro!!")
            functions.editar_registro()
            print(dados.dicionario_registros)
        elif comando == "3":
            print("você escolheu Excluir Registro!!")
            functions.excluir_registro()
            print(dados.dicionario_registros)

        elif comando == "7":
            return 0

main()
