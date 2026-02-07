l1 = float(input('Diga o lado 1: '))
l2 = float(input('Diga o lado 2: '))
l3 = float(input('Diga o lado 3: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
  print('Pode formar um triangulo! ▲ ')
else:
  print('Nao pode formar um triangulo! ')