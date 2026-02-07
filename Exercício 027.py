nome = input('Diga seu nome completo: ')
partes = nome.split()
primeiro_nome = partes[0]
print(f'Seu primeiro nome é: {primeiro_nome}')
print(f'Seu ultimo nome é: {partes[len(partes)-1]}')