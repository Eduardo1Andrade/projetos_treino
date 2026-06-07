''' aqui é o código principal'''
import functions
import dados
import utils

logo = "Sistema de Gerenciamento de Registro"
print("Sistema de Gerenciamento de Registro de Vendas Modas São Jõao")

def main(): #função principal
    while True:
        print(logo[0] + logo[11] + logo[-8])
        print("digite a função que deseja utilizar")
        comando = input('''opções:
            Criar Registro[1],
            Editar Registro[2],
            Excluir Registro[3],
            Listar Registro[4],
            Buscar Registro[5],
            Fazer Relátorio de Vendas[6]
            Listar Produdo[7]
            Gerar tamanhos[8]
            Sair[8]
            
            : ''')

        if comando == "1":
            print("você escolheu Criar Registro!!")
            functions.criar_novo_registro()

        elif comando == "2":
            print("você escolheu Editar Registro!!")
            functions.editar_registro()
        elif comando == "3":
            print("você escolheu Excluir Registro!!")
            functions.excluir_registro()
        
        elif comando == "4":
            print("você escolheu Listar Registros!!!")
            functions.listar_registro()

        elif comando == "5":
            print("você escolheu Buscar Registro!!")
            functions.buscar_registro()

        elif comando == "6":
            functions.gerar_relatorio()

        elif comando == "7":
            utils.listar_produtos()

        elif comando == "8":
            tamanho = utils.gerar_tamanho(3)
            print(next(tamanho))
            print(next(tamanho))
            print(next(tamanho))
            
        elif comando == "9":
            print("você escolheu sair!!")
            return 0

        else:
            print("digite um comando valido!!!")
            pass
main()
