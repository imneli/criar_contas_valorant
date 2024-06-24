# Valorant Account Creator

Este repositório contém um script em Python que automatiza a criação de contas no jogo Valorant utilizando a biblioteca `pyautogui` para simular ações do usuário.

## Descrição

O script realiza as seguintes tarefas:

1. Abre o navegador Chrome em modo anônimo.
2. Navega até o site de criação de contas do Valorant.
3. Preenche os campos de e-mail, data de nascimento, nome de usuário e senha.
4. Realiza as etapas necessárias para concluir a criação da conta no site.
5. Abre o jogo Valorant e faz login com a nova conta.
6. Configura o nome e hashtag in-game.

## Requisitos

- Python 3.x
- Biblioteca `pyautogui`
- Jogo Valorant instalado no sistema

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/imneli/valorant-account-creator.git
    cd valorant-account-creator
    ```

2. Instale a biblioteca `pyautogui`:
    ```bash
    pip install pyautogui
    ```

## Uso

Execute o script e siga as instruções na tela para criar uma nova conta Valorant:
```bash
python create_account.py
```

## Explicação do Código

<li>Importação das Bibliotecas:</li>

```py
import pyautogui
import time
```
<li>Configuração Inicial:</li>

```py
pyautogui.PAUSE = 0.7
```
<li>Coleta de Dados do Usuário:</li>

```py
email = input("Digite o e-mail da conta: ")
data = input("Digite a data da conta no modelo ddmmyyyy: ")
user = input("Digite o user de login da conta: ")
senha = input('Digite a senha da conta: ')
ingame = input('Digite o nick ingame da conta: ')
hash = input('Digite a hashtag da conta: ')
```
<li>Abertura do Navegador e Acesso ao Site:</li>

```py
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'shift', 'n')
pyautogui.write('https://playvalorant.com/pt-br/')
pyautogui.press('enter')
```

<li>Preenchimento do Formulário de Criação de Conta:</li>

```py
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
```

<li>Interação com o Jogo Valorant:</li>

```py
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
```

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests. Todas as contribuições são bem-vindas!



