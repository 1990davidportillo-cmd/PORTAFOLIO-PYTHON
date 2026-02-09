import time
from datetime import datetime

def tarea():
    print("Tarea ejecutada:", datetime.now())

hora_objetivo = "20:37"

while True:
    hora_actual = datetime.now().strftime("%H:%M")

    if hora_actual == hora_objetivo:
        tarea()
        break

    time.sleep(30)
