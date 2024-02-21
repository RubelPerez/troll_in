import mss
from PIL import Image

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
    for screenshot in screenshots:
        with Image.frombytes('RGB', screenshot.size, screenshot.rgb) as img:
            img.save(f"screenshot.png")
            break

# Captura todas las pantallas
screenshots = capture_all_screens()

# Guarda las capturas de pantalla en archivos individuales
save_screenshots(screenshots)
