print('-'*12,'Bem-vindos a pizzaria da Rayane dos Santos', '-'*12)
print('-'*29, 'Cardápio', '-'*29)
print('-'*68)
print('---|   Tamanho   |   Pizza Salgada (PS)   |   Pizza Doce (PD)   |---')
print('---|      P      |        R$ 30,00        |       R$ 34,00      |---')
print('---|      M      |        R$ 45,00        |       R$ 48,00      |---')
print('---|      G      |        R$ 60,00        |       R$ 66,00      |---')
print('-'*68)

# VARIÁVEIS
valor = 0; #Váriavel para identificar o preço da pizza.
valorTotalPedido = 0 #Váriavel para somar o valor do pedido, acumulador.

# LOOPING
while True:
  sabor = input('Entre com o sabor desejado (PS/PD): ')
  if(not sabor or (sabor != "PS") and (sabor != 'PD')):
    print('Sabor inválido. Tente novamente. \n')
  # Enquanto o usuário não selecionar um sabor válido vai repetir a pergunta.
  else:
    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    if(not tamanho or (tamanho != 'P' and tamanho != 'M' and tamanho != 'G')):
      print('Tamanho inválido. Tente novamente. \n')
  #Se o usuário não selecionar um tamanho válido, volta para o início do while.
    else:
  # Sabor e tamanho são ambos válidos, determinar o preço da pizza.
      if(sabor == 'PS' and tamanho == 'P'):
        valor = 30.00
        print(f'Você pediu uma Pizza Salgada no tamanho P: R$ {valor}\n')

      elif( sabor == 'PS' and tamanho == 'M'):
        valor = 45.00
        print(f'Você pediu uma Pizza Salgada no tamanho M: R$ {valor}\n')

      elif( sabor == 'PS' and tamanho == 'G'):
        valor = 60.00
        print(f'Você pediu uma Pizza Salgada no tamanho G: R$ {valor}\n')

      elif( sabor == 'PD' and tamanho == 'P'):
       valor = 34.00
       print(f'Você pediu uma Pizza Doce no tamanho P: R$ {valor}\n')

      elif( sabor == 'PD' and tamanho == 'M'):
        valor = 48.00
        print(f'Você pediu uma Pizza Doce no tamanho M: R$ {valor}\n')

      elif( sabor == 'PD' and tamanho == 'G'):
        valor = 66
        print(f'Você pediu uma Pizza Doce no tamanho G: R$ {valor} \n')

   # Calculado o valor total do pedido.
      valorTotalPedido += valor

   # Determinar se continua ou finaliza o while com base na resposta do usuário.
      continuar = input('Deseja pedir mais alguma coisa (S/N)? ')
      if(continuar == 'S'):
        continue
    # Volta para o início do while.
      else:
       break
    # Fim do loop.

# Fim do loop, print do valor total do pedido.
print(f'\nO valor total a ser pago é: R$ {valorTotalPedido}')
