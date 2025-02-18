import pyautogui
import time
import random


for i in range(99999, 101000):  # Agora inclui vários números
    pyautogui.write(str(i))
    pyautogui.press('enter')
    time.sleep(0.1)  # Pequeno delay para evitar problemas
