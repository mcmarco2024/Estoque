import estoque

def menu():
    print ('______MENU_________' )
    print ('1.INSERIR PRODUTO '  )
    print ('2.ATUALIZAR PRODUTO' )
    print ('3.DELETAR PRODUTO '  )
    print ('4.BUSCAR PRODUTO' )
    print ('5. LISTAR PRODUTO'   )
    print ('6. SAIR'             )
    return int(input('Escolha uma opção: '))
    # Função para inserir um novo produto
def inserir_produto():
    nome = input('Nome:')
    quantidade = int(input('Quantidade:'))
    preco = input('Valor:')
    estoque.inserir_produto(nome, quantidade, preco)
    print('Produto Inserido com sucesso')

# Função para listar todos os produtos
def lista_produto():
       produto = estoque.lista_os_produtos()
       print ('Lista de Produtos:')
       for produto in produto:
          print(produto)

# Função para atualizar os dados de um produto

def atualizar_produto():
     ID_produto = int(input('ID do Produto: '))
     nome = input('Nome: ')
     quantidade = int(input('Quantidade: '))
     preco = input('preco: ')
     estoque.atualizar_produto(ID_produto,nome, quantidade, preco)
     print ('Produto atualizado com sucesso!')

def deletar_produto():
     ID_produto = int(input ('ID do produto: '))
     estoque.deletar_produto('id_produto')
     print ('Produto deletado com sucesso')
     lista_produto()

# Função para pesquisar uma produto pelo nome

def pesquisar_produto():
 nome = input ('Nome: ')
#  resultado = database.pesquisar_produto(nome)
#  for linha in resultado:
#               print (f' {linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}')

def main():
    estoque.conectar()
    while True:
        opcao = menu()
        if opcao == 1:
            inserir_produto()
        elif opcao ==2:
            atualizar_produto()
        elif opcao == 3:
            deletar_produto()
        elif opcao == 4:
            pesquisar_produto()
        elif opcao == 5:
            lista_produto()
        elif opcao == 6:
            break
        else:
            print('Opção Inválida')
# Verifica se o arquivo está sendo executado diretamente
if __name__=="__main__":
    main()
     # chamar a função principal para inicializar o programa


