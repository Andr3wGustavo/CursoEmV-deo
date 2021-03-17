# Contagem regresive que demora 1 segundo
from time import sleep
for c in range(10, -1, -1):  # faz os fogos estourarem em 10 segundos
    print(c)
    sleep(1)
print('CABUMMM!')

