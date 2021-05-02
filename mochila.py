
def mochila(tamano_mochila, lista_pesos, lista_valores, n): #declaro todos los parametros
    print(f'n= {n}')
    print('------------------resultado nuevo--------------------')
    
    if n == 0 or tamano_mochila == 0: #si la lista de valores(n) es 0 o ya no hay espacio en la mochila entramos
         return 0
    if lista_pesos[n - 1] > tamano_mochila:
        return mochila(tamano_mochila, lista_pesos, lista_valores, n - 1)

    print(f'n= {n}')

    return max(lista_valores[n - 1] + mochila(tamano_mochila - lista_pesos[n-1], lista_pesos, lista_valores, n - 1),
              mochila(tamano_mochila, lista_pesos, lista_valores, n - 1))

if __name__ == '__main__':
        objetos = int(input('Ingrese la cantidad de objetos: '))
        lista_valores = []
        lista_pesos = []
        for x in range(objetos):
            valor = int(input('introduce el valor del objeto: '))
            pesos = int(input('Introduce el peso del objetos: '))
            lista_pesos.append(pesos)
            lista_valores.append(valor)
 
        tamano_mochila = int(input('Ingrese el tamaño de la mochila: '))
        
        n = len(lista_valores)

        resultado = mochila(tamano_mochila, lista_pesos, lista_valores, n)
        print(f'lista pesos {lista_pesos}')
        print('-' *50)
        print(f'lista de valores {lista_valores}')
        print('-' *50)
        print(f'tamaño mochila {tamano_mochila}')
        print('-' *50)
        print(f'El valor total que podemos juntar en la mochila es: {resultado}')