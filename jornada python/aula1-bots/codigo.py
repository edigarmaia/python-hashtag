# Passo a passo do projeto

# Passo 1 - entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time

# abrir o navegador

pyautogui.press("win")
time.sleep(2)

pyautogui.write("chrome")
pyautogui.press("enter")   
time.sleep(3)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2 - fazer login
time.sleep(3)
# posição do campo e-mailhttps://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.click(x=-1771, y=557)
pyautogui.write("edigarmaia@gmail.com")
pyautogui.press("tab")
# posição do campo senha
pyautogui.click(x=-1720, y=710)
pyautogui.write("edigarmaia@gmail.com")
# clicar no botão de logaredigarmaia@gmail.com

pyautogui.press("enter")

# tempo para carregar a página
time.sleep(3)

# Passo 3 - importar base de dados
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 - cadastrar um produto
# laço de repetição
for linha in tabela.index:
    # clicar no primeiro campo
    pyautogui.click(x=-1797, y=390)
    # codigo produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"] )
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"] )
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna():
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# Passo 5 - repetir o processo de cadastrar até acabar
