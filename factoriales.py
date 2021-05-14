def factorial(n):
    """
    Calcula el factorial de n.

    n int > 0
    returns n!

    """
    print(n) 
    if n == 1:
        return 1
    return n * factorial(n - 1)

def main():    
    n = int(input('escribe un entero:  '))
    factorial(n)
    n - 1
    print(factorial)
    print(n)
    
if __name__ == '__main__':
    main()


  