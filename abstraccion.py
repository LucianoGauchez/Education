class Lavadora:

    def __init__(self):
        pass

    def lavar(self,temperatura='caliente'):
        self.__llenar_tanque_de_agua(temperatura)
        self.__anadir_jabon()
        self.__lavar()
        self.__centrifugar()
    
    def __llenar_tanque_de_agua(self, temperatura):
        print(f'llenando el tanque con agua {temperatura}')
    
    def __anadir_jabon(self):
        print('añadiendo jabon')
    
    def __lavar(self):
        print('lavando la ropa')
    
    def __centrifugar(self):
        print('centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
