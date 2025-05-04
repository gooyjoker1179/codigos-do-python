import pyautogui
import time

# Coordenadas X e Y da posição onde os cliques vão acontecer
pos_x = 300
pos_y = 500

# Número de cliques que você quer fazer
num_cliques = 1000

# Intervalo entre cliques (em segundos)
intervalo = 0.5

print("O script vai começar em 3 segundos...")
time.sleep(3)

for i in range(1, num_cliques, 1):
    pyautogui.click(x=pos_x, y=pos_y)
    print(f"Clique {i + 1} em ({pos_x}, {pos_y})")
    