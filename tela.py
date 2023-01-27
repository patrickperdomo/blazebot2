import selenium
import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import requests
import json

# PRIMEIRA JANELA


def janela_instrucoes():
    sg.theme('Reddit')

    layout = [

        [sg.Text('FAÇA O LOGIN COM SUA CONTA DA BLAZE PARA CONTINUAR COM SUAS ESTRATEGIAS', size=(35, 5))],

        [sg.Text('email'), sg.Input(size=(15, 0), key='email')],

        [sg.Text('senha'), sg.Input(size=(15, 0), key='senha')],

        [sg.Text('siga o passo a passo abaixo para conseguir usar o bot em sua total utilidade', size=(0, 2))],

        [sg.Text('1)conta de usuario blaze ja cadastrada caso queira trocar informar ao admin.', size=(0, 2))],

        [sg.Text('2)Lembresse de estar sempre conectado a internet.', size=(0, 2))],

        [sg.Text('3)qualquer duvida contate o admin.', size=(0, 2))],

        [sg.Button('Continuar'), sg.Button('parar bot')]

    ]

    return sg.Window('INSTRUÇÕES', layout=layout, finalize=True)

# SEGUNDA JANELA


def tela_aposta():

    layout = [
        [sg.Text('ATENÇÃO BOT JA CONFIGURADO PARA APOSTA AUTOMATICA')],

        [sg.Text('coloque o valor da aposta aqui'),
         sg.Input(size=(15, 0), key='valor')],

        [sg.Text(
            'clique no botao iniciar para fazer a aposta')],

        [sg.Button('Apostar'), sg.Button('parar bot'), sg.Button('Voltar')]
    ]
    return sg.Window('apostar', layout=layout, finalize=True)


janela1, janela2, = janela_instrucoes(), None

# FUNÇAO DE INICIA O BOT


def Start():

    print("Starting Bot")

    global BASE_URL
    BASE_URL = 'https://blaze.com/pt/games/double'

    global driver

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1300,1000")
    chrome_options.add_experimental_option("detach", True)

    chrome_options.add_argument("--log-level=3")
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_position(500, 0, windowHandle="current")
    driver.get(BASE_URL)

    print("Bot started")

# REALIZA O LOGIN NA BLAZE


def Login():
    email = values['email']

    password = values['senha']

    wait = WebDriverWait(driver, 10)

    LOGIN_BUTTON = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="header"]/div[2]/div/div[2]/div/div/div[1]/a')))
    LOGIN_BUTTON.click()

    time.sleep(1)
    EMAIL_INPUT = driver.find_elements(
        By.CLASS_NAME, 'input-wrapper')[0].find_element(By.TAG_NAME, 'input')
    EMAIL_INPUT.send_keys(email)

    PASSWORD_INPUT = driver.find_elements(
        By.CLASS_NAME, 'input-wrapper')[1].find_element(By.TAG_NAME, 'input')
    PASSWORD_INPUT.send_keys(password)

    SUBMIT_BUTTON = driver.find_element(By.CLASS_NAME, 'submit')
    SUBMIT_BUTTON.click()

# PEGA OS RESULTADOS DA ROLETA


def pegar_dados():
    while True:
        time.sleep(3)
        pegardados = driver.find_element(
            By.XPATH, '//*[@id="roulette-recent"]').text

        tfg = pegardados.split()

        print(tfg)
        pd = tfg[0:16]
        mapeando = (QualNum, pd)
        mapeando2 = (QualCor, pd)

        finalnum = list(mapeando)
        finalcor = list(mapeando2)

        mapeando = (QualNum, pd)
        mapeando2 = (QualCor, pd)

        finalnum = list(mapeando)
        finalcor = list(mapeando2)

        print(finalnum)


def Apostar():
    valor = values['valor']
    VALOR_APOSTA = driver.find_element(
        By.XPATH, '//*[@id="roulette-controller"]/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(valor)


# VERIFICAR AS CORES

def Verificar(finalcor):
    if finalcor == ['vermelho', 'vermelho', 'preto', 'preto', 'vermelho', 'vermelho', 'preto', 'preto']:
        return Login()

# RETORNAR OS NUMEROS E CORES


def QualCor(x):
    if x == '1':
        return 'vermelho'

    if x == '2':
        return 'vermelho'

    if x == '3':
        return 'vermelho'

    if x == '4':
        return 'vermelho'

    if x == '5':
        return 'vermelho'

    if x == '6':
        return 'vermelho'

    if x == '7':
        return 'vermelho'

    if x == '8':
        return 'preto'

    if x == '9':
        return 'preto'

    if x == '10':
        return 'preto'

    if x == '11':
        return 'preto'

    if x == '12':
        return 'preto'

    if x == '13':
        return 'preto'

    if x == '14':
        return 'preto'

# RETORNA O NUMERO


def QualNum(x):

    if x == '1':
        return '1'

    if x == '2':
        return '2'

    if x == '3':
        return '3'

    if x == '4':
        return '4'

    if x == '5':
        return '5'

    if x == '6':
        return '6'

    if x == '7':
        return '7'

    if x == '8':
        return '8'

    if x == '9':
        return '9'

    if x == '10':
        return '10'

    if x == '11':
        return '11'

    if x == '12':
        return '12'

    if x == '13':
        return '13'

    if x == '14':
        return '14'


# FICA LENDO AS AÇOES DOS BOTOES


while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == "parar bot":
        break

    if window == janela1 and event == 'Continuar':

        Start()
        time.sleep(3)

        Login()

        janela2 = tela_aposta()

        janela1.hide()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    #if window == janela2 and event == 'Apostar':
    
