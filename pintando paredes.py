larg = float(input('Qual a largura da parede(m)? '))
alt = float(input('Qual a altura da parede(m)? '))
area = alt * larg
tinta = area / 2
print('Tendo a parede com dimensão {:.2f}x{:.2f} e área é igual a {:.2f}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta'.format(tinta))