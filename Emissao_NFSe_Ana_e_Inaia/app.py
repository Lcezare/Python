import pyautogui as ag
import keyboard
from time import sleep as zz
import requests
import pyperclip


def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                novo_arquivo.write(resposta.content)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

# INSTRUÇÕES:
# • Abra o chrome, maximize a janela e feche


# zz(2)
# ag.hotkey('win', 'r')
# zz(1)
# ag.write('chrome')
# zz(1)
# ag.press('enter')
# zz(1)
# ag.hotkey('ctrl', 'shift', 'n')
# zz(1)
# ag.write('https://portalprestador.hbsaude.com.br/')
# zz(1)
# ag.press('enter')
# zz(25)

# zz(2)
# ag.click(x=676,y=313)
# ag.write('358113')

# ag.press('tab')

# ag.write('350810130')
# zz(2)
# ag.click(x=579,y=436)
# zz(2)
# ag.tripleClick(x=584,y=50)
# ag.hotkey('ctrl', 'c')
zz(1)

file_url = pyperclip.paste()
print(file_url)
diretorio = 'C:\\Users\\Leonardo\\Downloads'

baixar_arquivo(file_url, diretorio)











ag.mouseInfo()