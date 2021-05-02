import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([0, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 00, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1]) #negro/0
        #tiro_2 = random.choice([00, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) #rojo/00
        secuencia_de_tiros.append(tiro)
        #ecuencia_de_tiros.append(tiro_2)
        #print(secuencia_de_tiros)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
    
    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Probabilidad de obtener un negro en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}]')

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos giros de la ruleta: '))
    numero_de_intentos = int(input('Cuantas veces queres correr la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)