from rich.console import Console
from rich.panel import Panel

from helpers import limpar_tela
from tabuada_funcao import calcular_tabuada

console = Console()


def mostrar_menu():
    limpar_tela()
    """Mostra o menu de opções."""
    MENU = f'''
    [bold green][1][/bold green]: -> Tabuada de 1 a 9
    [bold green][2][/bold green]: -> Adição (+)
    [bold green][3][/bold green]: -> Subtração (-)
    [bold green][4][/bold green]: -> Multiplicação (*)
    [bold green][5][/bold green]: -> Divisão (/)
    [bold green][0][/bold green]: -> Sair
'''
    console.print(MENU)
    return ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

console.print(f'[bold green]Bem-vindo ao programa de Tabuada![/bold green]')
options_menu = mostrar_menu()
operadores = ['+', '-', '*', '/']
operacao = ''
OP = ''
while OP != '0':
    try:
        OP = console.input(f'Informe a tabuada desejada: ') 
        if OP in options_menu:
            if OP == '0':
                console.print(f'[bold red]Saindo do programa...[/bold red]')
                break
            else:
                numero = int(OP)
                operacao = console.input(f'Informe a operação desejada (+, -, *, /): ')
                if operacao not in operadores:
                    console.print(f'[bold red]Operação inválida! Use +, -, * ou /.[/bold red]')
                    continue
                table = calcular_tabuada(numero, operacao)
                panel = Panel(table, title='Tabuada', expand=False)
                console.print(panel)

        else:
            console.print(f'[bold red]Tabuada inválida! Tente novamente.[/bold red]')
        continuar = input(f'Deseja continuar? (s/n): ').strip().lower()
        if continuar != 's':
            limpar_tela()
            console.print(f'[bold red]Saindo do programa...[/bold red]')
            break

    except ValueError:
        console.print(f'[bold red]Por favor, insira um número válido.[/bold red]')
