import pyautogui
import time

# Coordenadas X e Y da posição onde os cliques vão acontecer
pos_x = 500
pos_y = 300

# Número de cliques que você quer fazer
num_cliques = 10

# Intervalo entre cliques (em segundos)
intervalo = 0.5

print("O script vai começar em 3 segundos...")
time.sleep(3)

for i in range(num_cliques):
    pyautogui.click(x=pos_x, y=pos_y)
    print(f"Clique {i + 1} em ({pos_x}, {pos_y})")
    time.sleep(intervalo)