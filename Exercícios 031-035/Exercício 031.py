distancia = float(input('Diga a distância da sua viagem: '))
if distancia < 200:
  print(f'Sua passagem tem o valor de R${distancia *0.50}')
else:
  print(f'Sua passagem tem o valor de R${distancia * 0.45}')