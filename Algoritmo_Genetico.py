import random

modelo = [1,2,3,4,5,5,4,3,2,1]
largo = 10
num = 20
pressure = 3
mutation_chance = 0.2

#Crea aleatoriamente las caracteristicas (ADN) de cada individuo
def individual(min,max):
    return[random.randint(min, max) for i in range(largo)]

#Genera la poblacion deseada (num)
def crearPoblacion(): 
    return[individual(1,9) for i in range(num)]
    
#Compara cada caracteristica del individuo con su contraparte del modelo y cuenta las coincidencias
def calcularFitness(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1
    return fitness


def selection_and_reproduction(population):
    #lista de tuplas (fitness, individuo)  de todos los individuos
    puntuados = [ (calcularFitness(i), i) for i in population]
    #print('Puntuados:\n{}'.format(puntuados))

    #Lista ordenada de menor a mayor fitness
    puntuados = [i[1] for i in sorted(puntuados)]
    #print('Puntuados2:\n{}'.format(puntuados))
    population = puntuados

    #seleccion de individuos con mejor puntuacion (cantidad = pressure)
    selected = puntuados[(len(puntuados)-pressure):]
    #print('selected:\n{}'.format(selected))
    
    #reproduccion: Por cada elemento restante (poblacion - selected) sucede:
    #1. se seleccionan dos individuos aleatorios entre los seleccionados
    #2. se escoge un numero aleatorio (punto) de caracteristicas del primer individuo (principio)
    #3. se toman las caracteristicas restantes del segundo individuo (final)
    #4. se reemplaza un elemento de la poblacion.
    for i in range(len(population)-pressure):
        punto = random.randint(1,largo-1)
        padre = random.sample(selected, 2)
        
        population[i][:punto] = padre[0][:punto]
        population[i][punto:] = padre[1][punto:]
        
        #print('Punto: {}\nPadres:\n{}\nNuevo individuo:\n{}'.format(punto, padre, population[i]))
    return population
    
def mutation(population):
    for i in range(len(population)-pressure):
        # Se escoge aleatoriamente quien sufre una mutación.
        if random.random() <= mutation_chance:
            #se escoge una posicion aleatoria en la lista de caracteristicas
            punto = random.randint(0,largo-1)
            #se genera una caracteristica nueva de forma aleatoria
            nuevo_valor = random.randint(1,9)

            # Si el valor obtenido es igual al valor existente en el punto de
            # mutacion se generan valores aleatorios hasta que cambie, luego se
            #inserta el nuevo valor.
            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(1,9)
            population[i][punto] = nuevo_valor
        
    return population
    
def main():
    print("\n\Modelo: %s\n"%(modelo))
    population = crearPoblacion()
    print("Población Inicial:\n%s"%(population))

    for i in range(100):
        population = selection_and_reproduction(population)
        population = mutation(population)
        
    print("\nPoblación Final:\n%s"%(population))
    print("\n\n")

if __name__ == '__main__':
    main()
