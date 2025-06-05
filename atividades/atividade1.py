import os
os.system('cls')
import datetime
data = datetime.date.today()

try:
    nome = input('Informe seu nome completo: ')
    anoNascimento = input('Informe seu ANO de nascimento: ')
    mesNascimento = input('Informe sua MES de nascimento: ')
    dataNascimento = input('Informe sua DIA de nascimento: ')

    anoNascimento = int(anoNascimento)
    mesNascimento = int(mesNascimento)
    dataNascimento = int(dataNascimento)

    if anoNascimento < data.year:
        idade = data.year - anoNascimento
    else:
        idade = 0
    if mesNascimento > data.month:
        idade -= 1
    elif dataNascimento > data.day:
        idade -= 1

    print(f'Seu nome é {nome} e você tem {idade} anos')
except:
    print('Data inválida! Tente novamente')