alunos = ['Fernanda', 'Marcos', 'Bruna', 'Merinda', 'Thiago', 'Alessandra']

novos_alunos = alunos.copy()
alunos_ref = alunos

print(novos_alunos)
print(alunos is novos_alunos)
print(alunos is alunos_ref)

alunos_ref[0] = 'Marta'

print(alunos)
print(alunos_ref)