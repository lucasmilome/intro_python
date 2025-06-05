import os
os.system('cls')

def calculaDesconto(valorCompra, desconto):
    valorDescontado = valorCompra * desconto/100 
    valorCompra -= valorDescontado
    return valorCompra

valorDoProduto = int(input('Informe o valor do produto: '))
percentualdeDesconto = int(input('Informe o percentual de desconto do produto: '))

print(f'O valor do produto com desconto é R${calculaDesconto(valorDoProduto, percentualdeDesconto)}')