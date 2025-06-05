import os 
from rich.console import Console

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')

MENU = f'''[bold green]EXPLORADOR DE ARQUIVOS[/bold green]
[bold green][1][/bold green]: -> Criar Arquivo
[bold green][2][/bold green]: -> Ler Arquivo
[bold green][3][/bold green]: -> Editar Arquivo
[bold green][4][/bold green]: -> Deletar Arquivo
[bold green][5][/bold green]: -> Limpar Tela
[bold green][6][/bold green]: -> Lista Diretório
[bold green][7][/bold green]: -> Mudar Diretório
[bold green][8][/bold green]: -> Localização Atual
[bold green][0][/bold green]: -> Encerrar Script
'''

options_menu = ('1', '2', '3', '4', '5', '6', '7', '8', '0')
OP = ''

while OP != '0':
    try:
        console.print(MENU)
        OP = console.input(f'Informe a opção desejada: ')

        if OP in options_menu:
            if OP == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} CRIANDO ARQUIVOS {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'

                with open(fname, 'x', encoding='utf8') as f:
                    console.print(f'Arquivo {fname.upper()} criado com sucesso')
            
            elif OP == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} LENDO ARQUIVOS {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'

                with open(fname, 'r', encoding='utf8') as f:
                    console.print(f.read())
            
            elif OP == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} EDITANDO ARQUIVOS {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'

                text = console.input('Digite o texto:\n')
                
                with open(fname, 'a', encoding='utf8') as f:
                    f.write(text + '\n')
            
            elif OP == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} EXCLUINDO ARQUIVOS {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'

                if os.path.exists(fname):
                    os.remove(fname)
                    console.print('Arquivo excluído com sucesso!')
                else:
                    console.log('Arquivo não encontrado!')

            elif OP == '5':
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif OP == '6':
                os.system('cls' if os.name == 'nt' else 'clear')
                list_dir = os.listdir()

                for i in list_dir:
                    console.print(i)
            
            elif OP == '7':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} NAVEGANDO ENTRE PASTAS {'#' * 10}')
                destination = os.chdir(console.input('Mudar para pasta: '))
                console.print('PASTA ATUAL:', os.getcwd())
            
            elif OP == '8':
                os.system('cls' if os.name == 'nt' else 'clear')
                current = os.getcwd()
                console.print(f'[blue]DIRETÓRIO CORRENTE[/blue] [underline]{current}[/underline]')

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            console.print('[boldred]Opção inválida, tente novamente![/boldred]')
    except FileExistsError:
        console.print('[boldyellow]O arquivo já existe![/boldyellow]')
    except FileNotFoundError:
        console.print('[boldyellow]Arquivo não encontrado![/boldyellow]')

os.system('cls' if os.name == 'nt' else 'clear')