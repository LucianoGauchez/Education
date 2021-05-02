import random

def insercion(lista):
    for i in range(1,len(lista)):
        temp = lista[i]
        j = i - 1
        while j>=0 and lista[j]>temp:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1]=temp
    return lista


if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamano sera la lista?   '))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = insercion(lista)
    print(lista_ordenada)