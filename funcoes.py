import os

def limparTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
