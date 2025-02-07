import pyautogui
import time as tme

print("Mueve el ratón y observa las coordenadas en tiempo real. Pulsa 'Ctrl + C' para salir.")

try:
    while True:
        # Obtén las coordenadas del cursor
        x, y = pyautogui.position()
        # Imprime las coordenadas en el mismo lugar de la consola
        print(f"Posición del ratón: X = {x}, Y = {y}", end="\r", flush=True)
        tme.sleep(0.1)  # Actualiza cada 0.1 segundos
except KeyboardInterrupt:
    print("\nPrograma terminado.")