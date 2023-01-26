from tela import *

def Ler_Dados():
    while True:
        values = sg.read_all_window()

        email = values['email']

        password = values['senha']

        valor_aposta = values ['ValorAposta']

