import random

def repartir_cartas(numero_de_repartos):
    secuencia_de_repartos = []

    for _ in range(numero_de_repartos):
        primera_carta = random.choice(['a', 'j', 'k', 'q', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'j', 'k', 'q', 1, 2, 3, 4, 5, 6, 7, 8, 9])
        segunda_carta = random.choice(['a', 'j', 'k', 'q', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'j', 'k', 'q', 1, 2, 3, 4, 5, 6, 7, 8, 9])
        secuencia_de_repartos.append(primera_carta)
        secuencia_de_repartos.append(segunda_carta)
        #print(secuencia_de_repartos)

    return secuencia_de_repartos

def main(numero_de_repartos, numero_de_intentos):
    reparto = []
    for _ in range(numero_de_intentos):
        secuencia_de_repartos = repartir_cartas(numero_de_repartos)
        reparto.append(secuencia_de_repartos)
    
    repartos_con_21 = 0
    for tiro in reparto:
        if (('a') and ('j' or 'q' or 'k')) in tiro:
            #print('salio 21')
            repartos_con_21 += 1

    probabilidad_repartos_con_21 = repartos_con_21 / numero_de_intentos
    print(f'Probabilidad de obtener al menos un 21 en {numero_de_repartos} repartos = {probabilidad_repartos_con_21}]')

if __name__ == '__main__':
    numero_de_repartos = int(input('Cuantas manos: '))
    numero_de_intentos = int(input('Cuantas veces queres correr la simulacion: '))

    main(numero_de_repartos, numero_de_intentos)

    #---------------------------------------------------------RESULTADOS---------------------------------------------------------------------#
    '''
    PROBABILIDAD DE OBTENER 21 EN UNA MANO = 14,80%
    PROBABILIDAD DE OBTENER 21 EN 2 MANOS =  27,38%
    
    
    '''