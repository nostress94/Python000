print('EFICÁCIA GERAL DO TRABALHO')

print('REFERENTE A SEGURANÇA')

lista = []

R1 = str(input('DDS foi realizado e contém assinaturas? [S/N] ').upper())
lista.append(R1)
R2 = str(input('Não houve incidente? [S/N] ').upper())
lista.append(R2)
R3 = str(input('Não houve acidente? [S/N] ').upper())
lista.append(R3)

print('REFERENTE A 5S')

R4 = str(input('Auditoria foi realizada conforme cronograma? [S/N] ').upper())
lista.append(R4)
R5 = str(input('A pontuação atingiu a meta? [S/N] ').upper())
lista.append(R5)
print('REFERENTE A GESTÃO DE ROTINA')
print('Pé de Quadro:')

R6 = str(input('Participação Operador? [S/N] ').upper())
lista.append(R6)
R7 = str(input('Participação Padrinho Mecânica? [S/N] ').upper())
lista.append(R7)
R8 = str(input('Participação Padrinho Elétrica? [S/N] ').upper())
lista.append(R8)
R9 = str(input('Participação Coordenador/Gerente? [S/N] ').upper())
lista.append(R9)
R10 = str(input('Participação Qualidade? [S/N] ').upper())
lista.append(R10)
R11 = str(input('Participação Lider ou Supervisor da Máquina? [S/N] ').upper())
lista.append(R11)
R12 = str(input('As ACRs foram geradas conforme gatilho? [S/N] ').upper())
lista.append(R12)
R13 = str(input('Originou ações 24h? [S/N] ').upper())
lista.append(R13)

print('Reunião Técnica:')

R14 = str(input('Participação Supervisor/Gerente da Área? [S/N] ').upper())
lista.append(R14)
R15 = str(input('Participação Trainee? [S/N] ').upper())
lista.append(R15)
R16 = str(input('Participação Supervisor/Gerente de manutenção? [S/N] ').upper())
lista.append(R16)
print(lista)
print('A quantidade de S é igual a {}.'.format(lista.count("S")))
print('A quantidade de N é igual a {}.'.format(lista.count("N")))