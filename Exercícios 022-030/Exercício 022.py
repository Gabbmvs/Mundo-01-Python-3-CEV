nome = input('Digite seu nome completo: ')

print('Analisando seu nome...')
print(f'Seu nome em  maiusculas é: {nome.upper()}')
print(f'Seu nome em  minusculas é: {nome.lower()}')
print(f'Seu nome tem  {len(nome.replace (" ", ""))} letras') #que merda hein
partes = nome.split()
primeiro_nome = partes[0]
print(f'Seu primeiro nome é: {primeiro_nome}')
