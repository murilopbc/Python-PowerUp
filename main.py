
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")   
pyautogui.click(x=1287, y=462)
pyautogui.hotkey("ctrl", "t")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=609, y=475)
pyautogui.write("murilo@example.com")

time.sleep(3)
pyautogui.click(x=610, y=595)
pyautogui.write("123")

pyautogui.press("tab")
pyautogui.press("enter") 
time.sleep(3)

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    
    pyautogui.click(x=1119, y=306)
    
    codigo = tabela.loc[linha, "codigo"]
  
    pyautogui.write(str(codigo))
   
    pyautogui.press("tab")
  
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)
   
