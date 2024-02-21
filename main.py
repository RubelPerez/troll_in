import time
import mss
import win32api
from PIL import Image
import pyautogui
import win32gui
import win32con
import os
import struct
import ctypes
import getpass

pyautogui.hotkey('winleft', 'm')
time.sleep(1)

SPI_SETDESKWALLPAPER = 20


def changeBG(path):
    """Change background depending on bit size"""
    ctypes.windll.user32.SystemParametersInfoW(0x14, 0, path, 0x2)


def capture_all_screens():
    with mss.mss() as sct:
        # Captura todas las pantallas
        monitors = sct.monitors

        screenshots = []
        for monitor in monitors:
            screenshot = sct.grab(monitor)
            screenshots.append(screenshot)

        return screenshots


def save_screenshots(screenshots):
    nombre_usuario = getpass.getuser()
    for screenshot in screenshots:
        with Image.frombytes('RGB', screenshot.size, screenshot.rgb) as img:
            image = f"C:\\Users\\{nombre_usuario}\\Pictures\\screenshot.png"
            img.save(image)
            break

    wallpaper_style = 0
    SPI_SETDESKWALLPAPER = 20
    image = ctypes.c_wchar_p(image)

    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)


# Captura todas las pantallas
screenshots = capture_all_screens()

# Guarda las capturas de pantalla en archivos individuales
save_screenshots(screenshots)

pyautogui.moveTo(100, 100)  # Mueve el mouse a la posición (100, 100) durante 0.5 segundos
time.sleep(1)  # Espera un segundo
pyautogui.rightClick()
pyautogui.press('down', presses=1)
pyautogui.press('right', presses=1)
pyautogui.press('up', presses=1)
pyautogui.press('enter')

captura = pyautogui.screenshot()
posicion = pyautogui.locateOnScreen('icono_barra_tareas.png', image=captura)
if posicion is not None:
    centro = pyautogui.center(posicion)
    pyautogui.click(centro.x, centro.y)
else:
    print("No se encontró el ícono en la barra de tareas.")