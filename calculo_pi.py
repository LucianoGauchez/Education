import random
import math
from estadisticas import desviacion_estandar, media
def tirar_agujas(numero_de_agujas):
    adentro_del_circulo = 0
    
    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1

    return (4* adentro_del_circulo) / numero_de_agujas

def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = tirar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Estimado = {round(media_estimados, 5)}, Sigma = {round(sigma, 5)}, agujas = {numero_de_agujas}')

    return (media_estimados, sigma)

def estimar_pi(precision, numero_de_intentos):
    numero_de_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2

    return media

if __name__ == "__main__":
    estimar_pi(0.01, 1000)

'''
Estimado = 3.13846, Sigma = 0.05226, agujas = 1000
Estimado = 3.14127, Sigma = 0.03809, agujas = 2000
Estimado = 3.14138, Sigma = 0.02652, agujas = 4000
Estimado = 3.14122, Sigma = 0.01802, agujas = 8000
Estimado = 3.14086, Sigma = 0.01314, agujas = 16000
Estimado = 3.14137, Sigma = 0.00965, agujas = 32000
Estimado = 3.14199, Sigma = 0.00622, agujas = 64000
Estimado = 3.14179, Sigma = 0.00467, agujas = 128000
'''