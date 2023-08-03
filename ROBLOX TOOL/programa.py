import pyautogui
import pygetwindow
import psutil
import time
import threading
import colorama
import datetime
import cv2
import ctypes
import sys
from ctypes import wintypes as wts

colorama.init(convert=True)

título = """
    __________  ____  __   
   /_  __/ __ \/ __ \/ /   
    / / / / / / / / / /    
   / / / /_/ / /_/ / /___  
  /_/  \____/\____/_____/  
                           
"""

print(colorama.Back.CYAN + colorama.Fore.WHITE + título + colorama.Back.RESET + colorama.Fore.RESET)
print()

def print_with_timestamp(msg):
    timestamp = datetime.datetime.now().strftime("%H:%M")
    print(f"{timestamp} | {msg}")

processo_roblox = "Windows10Universal.exe"
processo_cmd = "cmd.exe"
ok_erro = "Error button image.png"
inject_button_img = "Inject button image.png"
limite_de_processos_abertos = int(input("DEFINA QUANTAS INSTÂNCIAS ABERTAS PARA COMEÇAR ARRUMAR AS JANELAS E INJETAR O FLUXUS: "))
print()
delay = int(10800)

def Arrumar_janelas_e_injetar_fluxus(processo_roblox, limite_de_processos_abertos):
    while True:
        def count_processes_by_name(processo_roblox):
            count = 0
            for process in psutil.process_iter(['name']):
                if process.info['name'] == processo_roblox:
                    count += 1
            return count

        current_count = count_processes_by_name(processo_roblox)

        if current_count >= limite_de_processos_abertos:    
            time.sleep(5)
            user32 = ctypes.WinDLL("user32.dll")

            HWND = wts.HWND
            UINT = wts.UINT

            hwnd_desktop = user32.GetDesktopWindow()
            user32.TileWindows(hwnd_desktop, 0x0001, None, 0, None)
            user32.TileWindows(hwnd_desktop, 0x0002, None, 0, None)

            fluxusWindow = pygetwindow.getWindowsWithTitle("MainWindow")
            if fluxusWindow:
                fluxusWindow = fluxusWindow[0]
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
                print_with_timestamp ("FLUXUS INJETADO E ERROS FECHADOS")
            else:
                inject_button = pyautogui.locateOnScreen(inject_button_img, confidence=0.7)
                pyautogui.click(inject_button)
                time.sleep(5)
                fluxusWindow.minimize()
                print_with_timestamp ("FLUXUS INJETADO")

            for process in psutil.process_iter(['name']):
                if process.info['name'] == processo_cmd:
                    process.kill()
                    print_with_timestamp ("CMD'S FECHADOS")
                    print()
                else:
                    print_with_timestamp ("SEM CMD'S")
                    print()
                    
            time.sleep(60)

def Printar_quantas_janelas_estão_abertas(processo_roblox):
    while True:
        def count_processes_by_name(processo_roblox):
            count = 0
            for process in psutil.process_iter(['name']):
                if process.info['name'] == processo_roblox:
                    count += 1
            return count

        current_count = count_processes_by_name(processo_roblox)

        if current_count == 0:
            print_with_timestamp ("NENHUMA INSTÂNCIA ESTÁ ABERTA")
            print ()
            time.sleep(5)
        else:
            if current_count == 1:
                print_with_timestamp (f"{current_count} INSTÂNCIA ESTÁ ABERTA")
                print ()
                time.sleep(5)
            else:
                print_with_timestamp (f"{current_count} INSTÂNCIAS ESTÃO ABERTAS")
                print ()
                time.sleep(5)

def Fechar_todas_instâncias_a_cada_determinado_tempo(delay):
    while True:
        for process in psutil.process_iter(['name']):
            if process.info['name'] == processo_roblox:
                process.kill()
                print_with_timestamp ("TODAS INSTÂNCIAS FORAM FECHADAS")
                print()
        time.sleep(delay)

thread1 = threading.Thread(target=Arrumar_janelas_e_injetar_fluxus, args=(processo_roblox, limite_de_processos_abertos))
thread2 = threading.Thread(target=Fechar_todas_instâncias_a_cada_determinado_tempo, args=(delay,))
thread3 = threading.Thread(target=Printar_quantas_janelas_estão_abertas, args=(processo_roblox,))

thread2.start()
time.sleep(5)
thread3.start()
thread1.start()