nombre_1 = str(input('Ingresa tu nombre: '))
num_1 = int(input('Ingresa tu edad: '))
nombre_2 = str(input('Ingresa el nombre de la otra persona: '))
num_2 = int(input('Ingresa la edad de la otra persona: '))
if   num_1<num_2:
    print(nombre_1,' es menor que ',nombre_2)
elif num_1>num_2:
    print(nombre_1,' es mayor que ',nombre_2)
else: 
    print(nombre_1,'y',nombre_2,'tienen la misma edad')
