n1 = int(input('Diga o número 1: '))
n2 = int(input('Diga o número 2: '))
n3 = int(input('Diga o número 3: '))
#parte dos menores
if n1 < n2 and  n1 < n3:
  print(f'Menor valor é {n1}')
if n2 < n1 and  n2 < n3:
  print(f'Menor valor é {n2}')
if n3 < n2 and  n3 < n1:
  print(f'Menor valor é {n3}')

#parte dos maiores

if n1 > n2 and  n1 > n3:
  print(f'Maior valor é {n1}')
if n2 > n3 and  n2 > n1:
  print(f'Maior valor é {n2}')
if n3 > n1 and  n3 > n2:
  print(f'Maior valor é {n3}')
