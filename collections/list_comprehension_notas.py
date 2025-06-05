notas = [10.0, 8.5, 9.4, 5.5, 10.0, 4.7, 6.9, 3.0, 7.0, 7.8, 8.3]

# Aprovados se nota for maior ou igual a 7.0

aprovados = [nota for nota in notas if nota >= 7.0]
reprovados = [nota for nota in notas if nota < 7.0]

print(aprovados)
print(reprovados)