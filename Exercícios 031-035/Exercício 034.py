salario = float(input('Diga seu salário em R$:'))
if salario > 1250:
  print(f'Você teve um aumento de 10%! seu salário de R${salario} foi para R${salario + (salario*0.1)}')

else:
  print(f'Você teve um aumento de 10%! seu salário de R${salario} foi para R${salario + (salario*0.15)}')
