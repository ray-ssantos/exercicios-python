# FUNÇÕES

# Função para retornar o valor do tipo de mandeira.
def escolha_tipo():

  # Declarando variaval global para utilizar no código principal.
  global tipoMadeira

  while True:
    op = (input('>> '))
    if(not op or (op != 'PIN' and op != 'PER' and op != 'MOG' and op != 'IPE' and op!= 'IMB')):
      print('Escolha inválida. Entre com o tipo novamente.')
    else:
      if(op == 'PIN'):
        tipoMadeira = 150.40
      elif(op == 'PER'):
        tipoMadeira = 170.20
      elif(op == 'MOG'):
        tipoMadeira = 190.90
      elif(op == 'IPE'):
        tipoMadeira = 210.10
      elif(op == 'IMB'):
         tipoMadeira = 220.70
      break

  return tipoMadeira

# Função para solicitar a quantidade de toras e calcular o desconto.
def qtd_toras():

# Declarando ambas variavéis global para utilizar no código principal.
  global desconto
  global qtdToras

  while True:

    try: # Valindo valor digitado pelo usuário, tem que ser numérico.

      qtdToras = int(input('\nEntre com a quantidade de toras (m3): '))
      if(qtdToras > 2000):
        print('Não aceitamos pedidos com essa quantidade de toras.')
        print('Por favor, entre novamente com a quantidade de toras.')
      else:
        if(qtdToras >= 1000):
          desconto = 16/100
        elif(qtdToras >= 500):
          desconto = 9/100
        elif(qtdToras >= 100):
          desconto = 4/100
        else:
          desconto = 0
        break
    except ValueError:
      print('Valor inválido. Tente novamente.')

  return qtdToras,desconto

# Função que retorna valor do transporte.
def transporte():

  # Declarando variaval global para utilizar no código principal.
  global valorTransporte

  while True:
   try: #Validando valor digitado pelo usuário, tem que ser numérico.
     op = int(input('>> '))
     if(op != 1 and op != 2 and op != 3):
       print('Selecione um número válido.')
     else:
        if(op == 1):
          valorTransporte = 1000.00
        elif(op == 2):
          valorTransporte = 2000.00
        elif(op == 3):
          valorTransporte = 2500.00
        break
        return valorTransporte

   except ValueError:
      print('Valor inválido. Tente novamente.')




# CÓDIGO PRINCIPAL

# Declarando váriaveis, seus valores serão alterados dentro das funções.
total = 0
tipoMadeira = 0
desconto = 0
qtdToras = 0
valorTransporte = 0

# Menu tipo de madeira
print('Bem vindo a madeireira - feito por Rayane dos Santos')
print('Entre com o tipo de madeira desejado:')
print('PIN - Tora de Pinho')
print('PER - Tora de Peroba')
print('MOG - Tora de Mogno')
print('IPE - Tora de Ipê')
print('IMB - Tora de Imbuia')

# Chamando a função para escolher tipo de madeira
escolha_tipo()

# Chamando a função para selecionar a quantidade de toras
qtd_toras()

#Menu transportes
print('\nEscolha o tipo de transporte:')
print('1 - Transporte Rodoviário - R$ 1.000,00')
print('2 - Transporte Ferroviário -R$ 2.000,00')
print('3 - Transporte Hidroviário - R$ 2.500,00')

# Chamando a função para escolher o tipo de transporte
transporte()

# Calculando o valor total do pedido e imprimindo na tela
total = ((tipoMadeira * qtdToras) * (1-desconto)) + valorTransporte
print(f'\n Total: R$ {total}')