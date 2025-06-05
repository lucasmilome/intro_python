senac = 'Serviço Nacional de Aprendizagem Comercial'
print('Tamanho da String Senac tem:',len(senac)) #"len" diz quantas letras "strings" tem na variável "senac"

print(senac[0]) #as Strings iniciam no 0
print(senac[1])
print(senac[2])
print(senac[3])
print(senac[4])
print(senac[5])
print(senac[6])

print('-'*40) #multipliquei por 40 as "-"

for i in senac:
    print(i,end='')

termo_pesquisa = 'Comercial'

print()
if termo_pesquisa in senac:
    print('A palavra', termo_pesquisa, 'existe na string senac')

if termo_pesquisa not in senac:
    print('A palavra', termo_pesquisa, 'não existe na string senac')