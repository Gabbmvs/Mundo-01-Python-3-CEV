from random import randint
num =  randint(0, 5)
resposta = int(input('Tente adivinhar o número de 0 a 5: '))
if resposta == num:
  print('Acertou!')
else:
  print('Errou, tente novamente')