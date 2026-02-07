frase = input('Escreva uma frase: ')
print(f'sua frase possui essa quantidade de "A": {frase.count("a")} unidades')
print(f'O primeiro A, aparece na posição: {frase.find("a")+1}')
print(f'O ultimo A, aparece na posição {frase.rfind("a")+1}')