import pyautogui
import time

pyautogui.PAUSE = 0.7

email = input("Digite o e-mail da conta: ")
data = input("Digite a data da conta no modelo ddmmyyyy: ")
user = input("Digite o user de login da conta: ")
senha = input('Digite a senha da conta: ')
ingame = input('Digite o nick ingame da conta: ')
hash = input('Digite a hashtag da conta: ')
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'shift', 'n')
pyautogui.write('https://playvalorant.com/pt-br/')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(957, 618)
time.sleep(1)
pyautogui.click(793, 646)
time.sleep(2.5)
pyautogui.click(1370, 459)
pyautogui.write(email)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(1348, 442)
time.sleep(0.7)
pyautogui.write(data)
pyautogui.press('enter')
time.sleep(0.6)
pyautogui.write(user)
pyautogui.press('enter')
pyautogui.click(1358, 433)
pyautogui.write(senha)
pyautogui.click(1353, 623)
pyautogui.write(senha)
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(1750, 401)
pyautogui.mouseDown()
pyautogui.moveTo(1752, 793)
pyautogui.mouseUp()
time.sleep(0.8)
pyautogui.click(1311, 793)
pyautogui.click(1530, 844)
pyautogui.press('win')
pyautogui.write('valorant')
pyautogui.press('enter')
time.sleep(5.5)
pyautogui.click(305, 368)
pyautogui.write(user)
pyautogui.click(316, 426)
pyautogui.write(senha)
pyautogui.press('enter')
time.sleep(3.3)
pyautogui.moveTo(1208, 216)
pyautogui.mouseDown()
pyautogui.moveTo(1213, 930)
pyautogui.mouseUp()
time.sleep(1)
pyautogui.click(857, 844)
time.sleep(1)
pyautogui.click(391, 404)
time.sleep(1)
pyautogui.click(815, 573)
pyautogui.write(ingame)
pyautogui.click(1076, 575)
pyautogui.write(hash)
pyautogui.click(859, 731)
time.sleep(2)
pyautogui.click(387, 403)