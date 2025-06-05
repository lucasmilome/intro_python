import os

os.system('cls')

nome_aluno = input('Informe o nome do(a) aluno(a): ')
media = input('Informe a média do(a) aluno(a): ')

# Converte a representação textual de um número para um float
media = float(media)

if media >= 7.0:
    print(f'Aluno(a) {nome_aluno} aprovado(a) com média {media}')
else:
    print(f'Aluno(a) {nome_aluno} reprovado(a) com média {media}')
    