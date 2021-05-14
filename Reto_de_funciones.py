seleccion = int(input('Desea hacer la busqueda de la raiz de forma: 1-binaria   2-enumeracion exhaustiva  : '))
objetivo = int(input('Escoge un numero: '))
epsilon1 = 0.001
epsilon2 = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta1 = (alto + bajo) / 2
paso = epsilon2**2
respuesta2 = 0.0

if seleccion == 1:

    while abs(respuesta1**2 - objetivo) >= epsilon1:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta1}')
        if respuesta1**2 < objetivo:
             bajo = respuesta1
        else:
             alto = respuesta1

        respuesta1 = (alto + bajo) / 2

        print(f'la raiz cuadrada de {objetivo} es {respuesta1}')

elif seleccion == 2:

     while abs(respuesta2**2 - objetivo) >= epsilon2 and respuesta2 <= objetivo:
         print(abs(respuesta2**2 - objetivo), respuesta2)
         respuesta2 += paso
         if abs(respuesta2**2 - objetivo) >= epsilon2:
              print(f'no se encontro la raiz cuadrada {objetivo}')
         else:
              print(f'La raiz cuadrada de {objetivo} es {respuesta2}')

else:
    print('Seleccion incorrecta, intentelo nuevamente')