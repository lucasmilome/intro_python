import os
from rich import print
from atividades.imcfunction import imc

os.system('cls')

peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))

calc_imc, status = imc(peso, altura)

print(f'O IMC é: {round(calc_imc, 2)}. O status do seu IMC é: {status}')