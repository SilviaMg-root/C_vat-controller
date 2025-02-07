'''
controlador C_VAT labeller
'''
import keyboard
import pyautogui
import time
# Coordenadas del sitio donde deseas hacer clic
x, y = 500, 300  # Cambia estos valores a las coordenadas de tu pantalla

# Mensaje informativo
print("Presiona la tecla 'n' para crear un nuevo pológono semiautomatico")
print("Presiona la tecla 'enter' para terminar de crear un pológono semiautomatico")
print("Presiona la tecla 'Left_arrow' para ir a la foto anterior")
print("Presiona la tecla 'Right_arrow' para ir a la siguiente foto")

print("Presiona 'esc' para salir.")




#Definicion coordenadas
xn, yn = (2428, -75) # New
xInt,yInt = (2883, 113) # Interact
xenter, yenter = (2778, -477) # Enter, terminar poligono
xl, yl = (3201, -490) #  Left_arrow
xr, yr = (3279, -477) # Right_arow
xsave, ysave = (2536, -489) # Save

while True:
    try:

    
        # Detecta si se pulsa la tecla 'n'
        if keyboard.is_pressed('n'):
            
            pyautogui.click(xn, yn)  # Nuevo
            print(f"Clic realizado en ({xn}, {yn}).") #pulsa en el icono "magic wand"n
            time.sleep(0.1)#pausa un momento para que pueda salir el panel de opciones
            
            
            pyautogui.click(xInt, yInt)  # Nuevo
            print(f"Clic realizado en ({xInt}, {yInt}).") #pulsa en el boton "Intereact"

        # Enter, termina Poligono
        if keyboard.is_pressed('enter'):
            pyautogui.click(xenter, yenter)  # Finaliza
            print(f"Clic realizado en ({xenter}, {yenter}).") #pulsa en el botón de finalizar
           

        #Flecha Derecha     
        if keyboard.is_pressed('left'):
            pyautogui.click(xl, yl)  # patras
            print(f"Clic realizado en ({xl}, {yl}).")

        #Flecha izquierda
        if keyboard.is_pressed('right'):

            pyautogui.click(xr, yr)  # palante
            print(f"Clic realizado en ({xr}, {yr}).")

        if (keyboard.is_pressed('shift') and keyboard.is_pressed('s')):
            pyautogui.click(xsave, ysave)
            print("click en guardado")

        # Salir del programa al pulsar 'esc'
        if keyboard.is_pressed('esc'):
            print("Programa terminado.")
            breaknn
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break

