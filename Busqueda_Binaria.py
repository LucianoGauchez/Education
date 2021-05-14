import random
contador = 0

def busqueda_binaria(lista, comienzo, final, objetivo): 
    global contador
    contador += 1
    
    print(f'se hizo  {contador}  pasos ')
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')

    if comienzo > final:      
        return False
        
    medio = (comienzo + final) //2 #division de enteros no importan los desimales

    if lista[medio] == objetivo:  
        return True
    
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
        
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
   
    

        
if __name__ == '__main__':

    tamano_de_lista = int(input('de que tamano sera la lista? '))
    objetivo = int(input('que numero queres encontrar?'))

    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta"if encontrado else "no esta"} en la lista')

    

