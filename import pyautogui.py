import pyautogui
import time

# Define a posição do clique
x = 256
y = 500

# Define o intervalo entre os cliques em segundos
intervalo = 1

# Define a tecla que irá parar o processo (no caso, a tecla 'q')
tecla_para_parar = 'q'

# Loop principal
while True:
  # Realiza o clique
  pyautogui.click(x, y)
  
  # Aguarda o intervalo definido
  time.sleep(intervalo)
  
  # Verifica se a tecla para parar foi pressionada
  if pyautogui.press(tecla_para_parar):
      break