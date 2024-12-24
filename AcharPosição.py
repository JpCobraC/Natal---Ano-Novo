import pyautogui
import time

print("Posicione o mouse sobre a barra de pesquisa no WhatsApp.")
time.sleep(5)
posicao = pyautogui.position()
print(f"A posição da barra de pesquisa é: {posicao}")
