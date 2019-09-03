nome = str(input('Qual nome do(a) colaborador(a)? '))
sal = float(input('Qual é o salário do colaborador(a) {}? R$ '.format(nome)))
sal2 = sal + (sal * 0.15)
print('O(a) colaborador(a) {} que recebia o salário R$ {:.2f}, com aumento de 15% passa a receber R$ {:.2f}.'.format(nome,sal,sal2))
