import random

def generar_contrasena():
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    simbolos = ['!','#','[',']','$','*',':','/','.','-','&','+'] 

    caracteres = mayusculas + minusculas + numeros + simbolos
    
    contrasena = []

    for i in range(16):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = ''.join(contrasena)
    return contrasena

def main():
    contrasena = generar_contrasena()
    print(f'Tu nueva contasena es: {contrasena}')


if __name__ == '__main__':
    main()