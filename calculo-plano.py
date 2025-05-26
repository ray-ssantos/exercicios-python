print('Sistema desenvolvido por Rayane dos Santos')

valorBase = float(input("Informe o valor base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))

valorMensal = 0
porcentagem = 0

# Fazendo o tratamento da idade do cliente
if(idade >= 59):
  porcentagem = 600

elif(idade >= 49):
  porcentagem = 350

elif(idade >= 39):
  porcentagem = 240

elif( idade >= 29):
  porcentagem = 225

elif( idade >= 19):
   porcentagem = 150

elif ((idade >= 0) and (idade < 19)):
  porcentagem = 100

# Caso a idade seja menor do que 0.
else:
  print("A idade informada é inválida.")

""" Após o tratamento da idade, temos o valor da porcentagem.
    Caso a idade seja inválida (menor do que zero), a porcentagem mantém o valor 0 atribuído no ínicio.
    Portanto, só damos continuidade ao cáculo do valor mensal, se a porcentagem for diferente de 0"""

if(porcentagem != 0):
  valorMensal = valorBase * porcentagem/100
  print(f"O valor mensal do plano é de: R$ {valorMensal}")
else:
  print("Tente novamente.")
