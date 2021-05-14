
def primo(n):

    if n == 0 or n == 1:
        return print(f'No es primo')
    else:
        n = n - 1
        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n - 1)

        return print(f'Es primo') if (factorial(n) + 1)%(n+1) == 0 else print(f'No es primo')

if __name__ == '__main__':
    number = int(input('Ingrese un numero: '))
    my_test = primo(number)