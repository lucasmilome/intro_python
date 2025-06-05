aluno = 'Rodrigo Bastos'
idade = 16
nacionalidade = 'brasileiro'
sexo = 'masculino'

print('O seu nome é', 
      aluno,
      ', você tem', 
      idade, 
      'anos de idade, é', 
      nacionalidade, 'e do sexo', 
      sexo
)

mensagem = 'O seu nome é ' + aluno + ', você tem ' + str(idade) + ' anos de idade, é ' + nacionalidade + ' e do sexo ' + sexo

print(mensagem)

mensagem = f'Seu nome é {aluno}, você tem {idade} anos,' \
f'é {nacionalidade} e do sexo {sexo}.' 

print(mensagem)

mensagem = f'''Seu nome é {aluno}, você tem {idade} anos, é 
{nacionalidade} e do sexo {sexo}.''' 

print(mensagem)