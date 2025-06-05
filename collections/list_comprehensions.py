fabricantes = [
    'Samsung',
    'LG',
    'Apple',
    'Motorola',
    'Apple',
    'Xiaomi'
]

print(fabricantes)

fabricantes = [fabricante for fabricante in fabricantes if fabricante != 'Apple']

print(fabricantes)