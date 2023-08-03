import pyautogui
import pygetwindow
import time

ok_erro = "Error button image.png"
inject_button_img = "Inject button image.png"

fluxusWindow = pygetwindow.getWindowsWithTitle("MainWindow")[0]
fluxusWindow.restore()
time.sleep(5)
ok_erro_button = pyautogui.locateOnScreen(ok_erro, confidence=0.7)

if ok_erro_button:
    pyautogui.click(ok_erro_button)
    time.sleep(2)
    ok_erro_button = pyautogui.locateOnScreen(ok_erro, confidence=0.7)
    pyautogui.click(ok_erro_button)
    time.sleep(2)
    inject_button = pyautogui.locateOnScreen(inject_button_img, confidence=0.7)
    pyautogui.click(inject_button)
    time.sleep(5)
    fluxusWindow.minimize()
    print("FLUXUS INJETADO E ERRO FECHADO")
else:
    inject_button = pyautogui.locateOnScreen(inject_button_img, confidence=0.7)
    pyautogui.click(inject_button)
    time.sleep(5)
    fluxusWindow.minimize()
    print("FLUXUS INJETADO")
