''' aqui é o código principal'''
import functions
print("Sistema de Gerenciamento de Registro de Vendas Modas São Jõao")


idade = input()
idade = int(idade)
def main():
    while True:
        print("digite a função que deseja utilizar")
        comando = input('''opções:
            Criar Registro[1],
            Editar Registro[2],
            Excluir Registro[3],
            Listar Registro[4],
            Buscar Registro[5],
            Fazer Relátorio de Vendas[6]: ''')

        if comando == "1":
            print("você escolheu Criar Registro!!")


main()
