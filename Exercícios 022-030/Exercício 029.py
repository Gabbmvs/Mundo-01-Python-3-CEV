km = int(input('Qual a velocidade do seu carro?: '))
if km > 80:
  multa = km - 80
  print('Você está acima do limite...')
  print(f'Sua multa é de R${multa*7}')
else:
  print('Continue nos limites. 😎👍')