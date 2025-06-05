import datetime

de0a10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

querJogar = 'S'

while querJogar.upper() == 'S':
    print('Tente advinhar um número sortado, você tem 3 tentativas...')

    data = datetime.datetime.now()
    micro = data.microsecond    
    numeroAleatorio = de0a10[micro % 10 - 1]

    i = 0
    while i < 3:
        numeroUsuario = int(input('Insira um número de 1 a 10: '))
        
        if numeroUsuario == numeroAleatorio:
            print('Parabéns, você acertou!!')
            break
        else: 
            print(f'Não foi dessa vez, tente novamente (tentiva {i + 1} de 3)')
            
        if numeroUsuario < numeroAleatorio:
            print('Seu palpite foi maior que o número sorteado')
        else:
            print('Seu palpite foi menor que o número sorteado')

        i += 1
        
    if i == 3:
        print(f'O número sorteado era: {numeroAleatorio}.')

    querJogar = input('Deseja jogar novamente? (S/N): ')