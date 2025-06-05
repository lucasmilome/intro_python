senac = 'SERVIÇO NACIONAL DE APRENDIZAGEM COMERCIAL'
print(senac)

# Cada palavra inicia com a letra maiúscula
senac = senac.title()
print(senac)

# Retorna a string com todos os caracteres em caixa alta
senac = senac.upper()
print(senac)

# Retorna a string com todos os caracteres em caixa baixa
senac = senac.lower()
print(senac)

# Retorna a string capitalizada
senac = senac.capitalize()
print(senac)

# Remove espaços antes e depois da string
print(senac.strip())
print(senac)

# Substitui partes de uma string
senac = senac.replace('comercial', 'COMERCIAL')
print(senac)

senac = senac.replace(' ', ' | ')
print(senac)

# Divide uma string mediante um separador
lista_senac = senac.split(' | ')
print(lista_senac)

for palavra in lista_senac:
    print(palavra)