import pyautogui
import datetime
import os
from dotenv import load_dotenv

# Definindo variáveis de ambiente
load_dotenv()

BROWSER = os.getenv('BROWSER')
LINK = os.getenv('LINK')
CNPJ = os.getenv('CNPJ')
SENHA = os.getenv('SENHA')
CNPJ_CLIENTE = os.getenv('CNPJ_CLIENTE')
EMAIL_CLIENTE = os.getenv('EMAIL_CLIENTE')
CEP_CLIENTE = os.getenv('CEP_CLIENTE')
NUMERO_CLIENTE = os.getenv('NUMERO_CLIENTE')

datetime = datetime.datetime
# Abrindo o navegador com o pyautogui
pyautogui.sleep(1)
pyautogui.press('win')
pyautogui.sleep(1)
pyautogui.write(BROWSER)
pyautogui.press('enter')
pyautogui.sleep(2)

# Abrindo o site do gerador de nota fiscal
pyautogui.write(LINK)
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(2)

# Clicando no botão de emitir nota fiscal
pyautogui.click(1000, 500)
pyautogui.sleep(2)

# Preenchendo os dados e fazendo login
pyautogui.press('tab')
pyautogui.write(CNPJ)
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.write(SENHA)
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.sleep(2)

# Navegando até a aba de emitir nota fiscal
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

# Preenchendo os dados da nota fiscal
pyautogui.sleep(4)
pyautogui.click(213, 410)
pyautogui.sleep(1)
pyautogui.write(
    f'15{"{:02d}".format(datetime.now().month)}{datetime.now().year}')
pyautogui.sleep(1)
pyautogui.scroll(-1000)
pyautogui.sleep(1)

# Preenchendo os dados do cliente
pyautogui.click(181, 427)
pyautogui.sleep(4)
pyautogui.click(181, 427)
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.write(CNPJ_CLIENTE)
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.sleep(1)
pyautogui.write(EMAIL_CLIENTE)
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.sleep(1)
pyautogui.write(CEP_CLIENTE)
pyautogui.sleep(2)
pyautogui.click(507, 848)
pyautogui.sleep(1)
pyautogui.scroll(-1000)
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(NUMERO_CLIENTE)
pyautogui.sleep(2)
pyautogui.click(1747, 744)
pyautogui.mouseInfo()
