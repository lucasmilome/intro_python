def imc(peso, altura):
    calc_imc = peso / altura ** 2
    if calc_imc >= 40.0:
        status = '[bold red]Obesidade grau III[/bold red]'
    elif calc_imc >= 35.0 and calc_imc <= 39.9:
        status = '[bold red]Obesidade grau II[/bold red]'
    elif calc_imc >= 30.0 and calc_imc <= 34.9:
        status = '[bold red]Obesidade grau I[/bold red]'
    elif calc_imc >= 25.0 and calc_imc <= 29.9:
        status = '[bold red]Sobrepeso[/bold red]'
    elif calc_imc >= 18.6 and calc_imc <= 24.9:
        status = '[bold red]Normal[/bold red]'
    elif calc_imc >= 18.5:
        status = '[bold red]Abaixo do normal[/bold red]'
   
    return calc_imc, status