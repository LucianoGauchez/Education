class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)
        self._version = cantidad_puertas()

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = 'en_movimiento'   
   
class version:
        def puertas(self, cantidad_puertas(2)):
        if cantidad_puertas == 4:
            self._version('sedan')
        elif cantidad_puertas == 2:
            self._version('coupe')
        else:
            self._version('No encontrada')    
class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo

    
    def inyecta_gasolina(self, cantidad):
        pass
    
