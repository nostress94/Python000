valor = float(input('Qual o preço do produto? R$ '))
valor2 = valor - (valor * 0.05)
print('O produto que custava R$ {:.2f}, com desconto de 5% vai custar R$ {:.2f}'.format(valor, valor2))