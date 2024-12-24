import pyautogui
import pyperclip
import time
import schedule
from datetime import datetime

#Insíra os contatos de acordo com o modelo:
contatos = {
    "Nome do contato": "Mensagem do contato",
    "Nome do contato 2": "Mensagem do contato 2"
}

# Encontre a posição logo abaixo da barra de pesquisa em seu computador e insíra aqui
barra_pesquisa_posicao = (213,184)

def enviar_mensagem(contato, mensagem):
    pyautogui.hotkey('ctrl', 'f')  
    time.sleep(1)
    pyperclip.copy(contato)
    pyautogui.hotkey('ctrl', 'v')  
    time.sleep(2)
    pyautogui.click(barra_pesquisa_posicao)
    time.sleep(1)

    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def enviar_mensagens():
    time.sleep(5)
    for contato, mensagem in contatos.items():
        enviar_mensagem(contato, mensagem)

# Primeiro rode por aqui para testar
enviar_mensagens()

# Após testar, remova o '#' da linha de baixo e o time.sleep(5) dentro da função enviar_mensagens().
# schedule.every().day.at("00:00").do(enviar_mensagens)

while True:
    schedule.run_pending()
    time.sleep(1)
