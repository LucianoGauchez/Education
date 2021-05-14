
def main(cuotas, inflacion_mensual):
    # porcentaje = inflacion_mensual * cuotas
    if cuotas == 3:
        porcentaje = inflacion_mensual * cuotas
        print(f'El porcentaje a cobrar con {cuotas} cuotas es de {porcentaje}% total')
    elif cuotas == 6:
        porcentaje = inflacion_mensual * cuotas
        print(f'El porcentaje a cobrar con {cuotas} cuotas es de {porcentaje}% total')
    elif cuotas == 12:
        porcentaje = inflacion_mensual * cuotas
        print(f'El porcentaje a cobrar con {cuotas} cuotas es de {porcentaje}% total')
    elif cuotas == 18:
        porcentaje = inflacion_mensual * cuotas
        print(f'El porcentaje a cobrar con {cuotas} cuotas es de {porcentaje}% total')
    else:
        print('ingreso una cantidad de cuotas incorrecta')
   


if __name__ == '__main__':
    inflacion_2019 = float(55) / 12
    inflacion_2020 = float(53.8) / 12
    inflacion_mensual = (inflacion_2019 + inflacion_2020) / 2
    cuotas = int(input('ingrese cuantas cuotas quiere: '))
    main(cuotas, inflacion_mensual)
    print(inflacion_mensual)
   