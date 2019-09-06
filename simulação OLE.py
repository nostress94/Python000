"""
Simulação e Modelagem
Grupo: Gabriel Correa, Larissa Alves, Raphael Abreu, Tatiane Braga
Professor Ronaldo Abreu
"""

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'pretoebranco': '\033[7;30m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
		 'bluebold':'\033[1;36m'}

print(cores['pretoebranco'], '-=' * 5, 'EFICÁCIA GERAL DO TRABALHO', '=-' * 5, cores['limpa'])

print('Referente a segurança:')

lista = []

R1 = str(input('DDS foi realizado e contém assinaturas? [S/N] ').upper())
lista.append(R1)
R2 = str(input('Não houve incidente? [S/N] ').upper())
lista.append(R2)
R3 = str(input('Não houve acidente? [S/N] ').upper())
lista.append(R3)

seg = lista.count('S') + lista.count('SIM')
segurança = seg / 3
print(cores['bluebold'],'O indicador OLE de segurança é {:.2f}.\033[m'.format(segurança))
if segurança < 0.65:
    print(cores['vermelho'], 'ALERTA!', cores['limpa'])
elif segurança > 0.66 and segurança < 0.79:
    print(cores['amarelo'], 'ATENÇÃO!', cores['limpa'])
elif segurança > 0.80:
    print(cores['azul'], 'PARABÉNS!', cores['limpa'])

print('REFERENTE A 5S')

lista2= []
R4 = str(input('Auditoria foi realizada conforme cronograma? [S/N] ').upper())
lista.append(R4)
lista2.append(R4)
R5 = str(input('A pontuação atingiu a meta? [S/N] ').upper())
lista.append(R5)
lista2.append(R5)

fives = lista2.count('S') + lista2.count('SIM')
cincos = fives / 2

print(cores['bluebold'], 'O indicador OLE de 5S é {:.2f}.\033[m'.format(cincos))
if cincos < 0.65:
    print(cores['vermelho'], 'ALERTA!', cores['limpa'])
elif cincos > 0.66 and cincos < 0.79:
    print(cores['amarelo'], 'ATENÇÃO!', cores['limpa'])
elif cincos > 0.80:
    print(cores['azul'], 'PARABÉNS!', cores['limpa'])

print('REFERENTE A GESTÃO DE ROTINA')

print('Pé de Quadro:')

lista3 = []

R6 = str(input('Participação Operador? [S/N] ').upper())
lista.append(R6)
lista3.append(R6)
R7 = str(input('Participação Padrinho Mecânica? [S/N] ').upper())
lista.append(R7)
lista3.append(R7)
R8 = str(input('Participação Padrinho Elétrica? [S/N] ').upper())
lista.append(R8)
lista3.append(R8)
R9 = str(input('Participação Coordenador/Gerente? [S/N] ').upper())
lista.append(R9)
lista3.append(R9)
R10 = str(input('Participação Qualidade? [S/N] ').upper())
lista.append(R10)
lista3.append(R10)
R11 = str(input('Participação Lider ou Supervisor da Máquina? [S/N] ').upper())
lista.append(R11)
lista3.append(R11)
R12 = str(input('As ACRs foram geradas conforme gatilho? [S/N] ').upper())
lista.append(R12)
lista3.append(R12)
R13 = str(input('Originou ações 24h? [S/N] ').upper())
lista.append(R13)
lista3.append(R13)

pquadro = lista3.count('S') + lista3.count('SIM')
pequadro = pquadro / 8

print(cores['bluebold'], 'O indicador OLE do Pé de quadro é {:.2f}.\033[m'.format(pequadro))
if pequadro < 0.65:
    print(cores['vermelho'], 'ALERTA!', cores['limpa'])
elif pequadro > 0.66 and pequadro < 0.79:
    print(cores['amarelo'], 'ATENÇÃO!', cores['limpa'])
elif pequadro > 0.80:
    print(cores['azul'], 'PARABÉNS!', cores['limpa'])

print('Reunião Técnica:')

lista4 = []

R14 = str(input('Participação Supervisor/Gerente da Área? [S/N] ').upper())
lista.append(R14)
lista4.append(R14)
R15 = str(input('Participação Trainee? [S/N] ').upper())
lista.append(R15)
lista4.append(R15)
R16 = str(input('Participação Supervisor/Gerente de manutenção? [S/N] ').upper())
lista.append(R16)
lista4.append(R16)
R17 = str(input('Participação do Almoxarifado (1 vez na semana)? [S/N] ').upper())
lista.append(R17)
lista4.append(R17)
R18 = str(input('Participação Supervisor/Inspetor de qualidade? [S/N] ').upper())
lista.append(R18)
lista4.append(R18)
R19 = str(input('Todas as ações do dia foram executadas? [S/N] ').upper())
lista.append(R19)
lista4.append(R19)

reutec = lista4.count('S') + lista4.count('SIM')
reutec1 = reutec / 6

print(cores['bluebold'], 'O indicador OLE da Reunião Técnica é {:.2f}.\033[m'.format(reutec1))
if reutec1 < 0.65:
    print(cores['vermelho'], 'ALERTA!', cores['limpa'])
elif reutec1 > 0.66 and reutec1 < 0.79:
    print(cores['amarelo'], 'ATENÇÃO!', cores['limpa'])
elif reutec1 > 0.80:
    print(cores['azul'], 'PARABÉNS!', cores['limpa'])

print('Reunião SAC:')

lista5 = []

R20 = str(input('Participação Qualidade? [S/N] ').upper())
lista.append(R20)
lista5.append(R20)
R21 = str(input('Participação Produção/Processo? [S/N] ').upper())
lista.append(R21)
lista5.append(R21)
R22 = str(input('Originou Ações? [S/N] ').upper())
lista.append(R22)
lista5.append(R22)

reusac = lista5.count('S') + lista5.count('SIM')
reusac1 = reusac / 3

print(cores['bluebold'], 'O indicador OLE da Reunião SAC é {:.2f}.\033[m'.format(reusac1))
if reusac1 < 0.65:
    print(cores['vermelho'], 'ALERTA!', cores['limpa'])
elif reusac1 > 0.66 and reusac1 < 0.79:
    print(cores['amarelo'], 'ATENÇÃO!', cores['limpa'])
elif reusac1 > 0.80:
    print(cores['azul'], 'PARABÉNS!', cores['limpa'])

print ('Quadro de LIL:')

lista6 = []

R23 = str(input('Nenhum item "Classe A" está faltando no armário da linha? [S/N] ').upper())
lista.append(R23)
lista6.append(R23)
R24 = str(input('Todas as Limpezas da linha foram realizadas? [S/N] ').upper())
lista.append(R24)
lista6.append(R24)
R25 = str(input('A inspeção elétrica foi realizada? [S/N] ').upper())
lista.append(R25)
lista6.append(R25)
R26 = str(input('A inspeção mecânica foi realizada? [S/N] ').upper())
lista.append(R26)
lista6.append(R26)
R27 = str(input('A lubrificação foi realizada? [S/N] ').upper())
lista.append(R27)
lista6.append(R27)
R28 = str(input('A termografia foi relizada? [S/N] ').upper())
lista.append(R28)
lista6.append(R28)
R29 = str(input('A Preditiva foi realizada? [S/N] ').upper())
lista.append(R29)
lista6.append(R29)

lil = lista6.count('S') + lista6.count('SIM')
lil1 = lil / 7

print(cores['bluebold'], 'O indicador OLE do Quadro de LIL é {:.2f}.\033[m'.format(lil1))
if lil1 < 0.65:
    print(cores['vermelho'], 'ALERTA!', cores['limpa'])
elif lil1 > 0.66 and lil1 < 0.79:
    print(cores['amarelo'], 'ATENÇÃO!', cores['limpa'])
elif lil1 > 0.80:
    print(cores['azul'], 'PARABÉNS!', cores['limpa'])


print(lista)
sim = lista.count('S') + lista.count('SIM')
nao = lista.count('N') + lista.count('NÃO') + lista.count('NAO')
print('A quantidade de \033[34mSIM TOTAL\033[m é igual a \033[34m{}\033[m'.format(sim))
print('A quantidade de \033[1;31mNÃO TOTAL\033[m é igual a \033[1;31m{}\033[m.'.format(nao))
total = sim / 29
print(cores['bluebold'], 'O indicador OLE TOTAL é {:.2f}.'.format(total))
if total < 0.65:
    print(cores['vermelho'], 'ALERTA!', cores['limpa'])
elif total > 0.66 and total < 0.79:
    print(cores['amarelo'], 'ATENÇÃO!', cores['limpa'])
elif total > 0.80:
    print(cores['azul'], 'PARABÉNS!', cores['limpa'])
