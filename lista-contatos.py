def cadastrar_contato(id):

  global lista_contatos
  # Dicionário que vai receber os contatos que serão copiados para a lista de contatos.
  contato = { 'id': [],'nome': [],'atividade':[],'telefone' : []}

  nome = input('Por favor entre com o nome do contato: ')
  atividade = input('Por favor entre com a atividade do contato: ')
  telefone = input('Por favor entre com o telefone do contato: ')

  contato['id'].append(id)
  contato['nome'].append(nome)
  contato['atividade'].append(atividade)
  contato['telefone'].append(telefone)
  lista_contatos.append(contato.copy())
  print('\nContato cadastrado com sucesso.')
  print('-'*50)

  return lista_contatos

# Função para consultar contatos #
def consultar_contatos():
  while True:
    print('-'*56)
    print('-'*16, 'MENU CONSULTAR CONTATOS','-'*16)
    print('Escolha a opção desejada:')
    print('1 - Consultar Todos os Contatos')
    print('2 - Consultar Contato por Id')
    print('3 - Consultar Contatos por Atividade')
    print('4 - Retornar ao menu')

    try:
      # Identificando a opção escolhida pelo usuário.
      op = int(input('>> '))
      if(op != 1 and op != 2 and op != 3 and op != 4):
        print('Você selecionou uma opção inválida. Por favor tente novamente.')
      else:
        # Opção 1 - Consultar Todos
        if(op == 1):
          print('-'*20)
          for contato in lista_contatos:
            for chave, valores in contato.items() :
              print(f'{chave} : {valores[0]}', end = '\n')
            print('')
          print('-'*20)

        # Opção 2 - Consultar por Id
        elif(op == 2):

          id_desejado = int(input('Digite o id do contato: '))
          contato_encontrado = None

          # Procurando na lista de contatos, o contato com o id informado:
          for contato in lista_contatos:
            if(id_desejado in contato['id']):
              posicao = contato['id'].index(id_desejado)
              contato_encontrado = {} # Armazendando os dados do contato em um novo dicionário.
              for chave in contato:
                contato_encontrado[chave] = contato[chave][posicao]
              break
          if contato_encontrado: # Imprimindo o contato encontrado.
            print('-'*20)
            for chave, valores in contato_encontrado.items() :
                print(f'{chave} : {valores}', end = '\n')
            print('')
            print('-'*20)
            print('-'*50)
          else:
              print('Contato não encontrado!')

        # Opcao 3 == Consultar por atividade
        elif(op == 3):
          atividade_desejada = input('Digite a Atividade do(s) Contato(s): ')
          contatos_com_atividade = []

          # Procurando os contas com a atividade desejada e armazenando-os na lista contatos_com_atividades.
          for contato in lista_contatos:
            if(atividade_desejada in contato['atividade']):
              contatos_com_atividade.append(contato)
          if contatos_com_atividade:
            print('-'*20)
            for contato in contatos_com_atividade:
              for chave, valores in contato.items() :
                print(f'{chave} : {valores[0]}', end = '\n')
              print('')
            print('-'*20)
          else:
            print('Nenhum contato encontrado com essa atividade.')

        # Opção 4 - Retornar ao menu
        elif(op == 4):
          print('Retornando ao menu...')
          break

    except ValueError:
      print('Vocé digitou um valor inválido. Por favor tente novamente')

# Função para remover um contato
def remover_contato():
  while True:
    print('-'*56)
    print('-'*16, 'MENU REMOVER CONTATO','-'*16)
    id_remover = int(input('Digite o id do contato a ser removido: '))
    # Procurando na lista de contatos a posição do contato que possuo o id informado.
    for i in range(len(lista_contatos)):
      contato = lista_contatos[i]
      if(id_remover in contato['id']):
        #Removendo o contato
        lista_contatos.pop(i)
        print('Contato removido com sucesso.')
        print('')
        print('-'*50)
        return

    print('Contato não encontrado.')




# CÓDIGO PRINCIPAL

# Variáveis
id_global = 1
lista_contatos = []


#Menu
while True:

  print('Bem-vindo a lista de contatos da Rayane dos Santos')
  print('-'*56)
  print('-'* 20, 'MENU PRINCIPAL', '-'*20)
  print('Escolha a opção desejada:')
  print('1 - Cadastrar Contatos')
  print('2 - Consultar Contatos(s)')
  print('3 - Remover Contato')
  print('4 - Sair')

  try:
    op = int(input('>> '))
    if( op != 1 and op != 2 and op != 3 and op != 4):
      # Opção escolhida diferente de 1/2/3/4:
      print('Você selecionou uma opção inválida. Por favor tente novamente.')
    else:
      # Opção 1 - Menu cadastrar contato
      if(op == 1):
        id_global += 1
        print('-'*56)
        print('-'*16, 'MENU CADASTRAR CONTATO','-'*16)
        print(f'Id do contato: {id_global}')
        cadastrar_contato(id_global)
        print('')

      # Opção 2 - Menu consultar contatos
      elif(op == 2):
        consultar_contatos()

      # Opção 3 - Remover Contato
      elif(op == 3):
        remover_contato()

      # Opção 4 - Sair do Programa
      elif(op == 4):
        print('Encerrando programa...')
        break

  except ValueError:
      print('Vocé digitou um valor inválido. Por favor tente novamente')
#FIM