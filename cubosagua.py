import sys

"""Clase donde se juega con los cubos"""


class juegoCubos:
    pasos = 0
    aguaEnCubos = {'8': 0, '5': 0, '3': 0}

    def __init__(self, fobjetivo):
        """
        Constructor de los cubos
        :param fobjetivo:int
        """
        self.objetivo = fobjetivo

    def genStrCubos(self):
        """Generador de la estructura de los cubos"""
        caracterAgua = '~'
        visualizadorCubos = []

        for i in range(1, 9):
            if self.aguaEnCubos['8'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        for i in range(1, 6):
            if self.aguaEnCubos['5'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        for i in range(1, 4):
            if self.aguaEnCubos['3'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        # Devuelve una cadena con los cubos y su contenido de agua
        return '''
        8|{7}|
        7|{6}|
        6|{5}|
        5|{4}|  5|{12}|
        4|{3}|  4|{11}|
        3|{2}|  3|{10}|  3|{15}|
        2|{1}|  2|{9}|  2|{14}|
        1|{0}|  1|{8}|  1|{13}|
         +------+   +------+   +------+
            8L         5L         3L
        '''.format(*visualizadorCubos)

    def mostrarEstadoCubos(self):
        """Dibuja la estructura"""
        print()
        print('Intenta conseguir ' + str(self.objetivo) + ' litros de agua en uno de estos cubos')
        print(self.genStrCubos())

    def checkObjetivo(self):
        """Comprueba si uno de los cubos ha conseguido el objetivo"""
        for cantidadAgua in self.aguaEnCubos.values():
            if cantidadAgua == self.objetivo:
                print('Bien hecho! Lo has resuelto en', self.pasos, 'pasos!')
                sys.exit()

    def selecOpcion(self):
        """Selección de una opción"""
        print('Elige una opción:')
        print('  (L)lenar un cubo')
        print('  (V)aciar un cubo')
        print('  (M)over el agua de un cubo a otro')
        print('  (B)uidar Cubos')
        print('  (T)odos los cubos llenos')
        print('  (S)alir')

        while True:
            move = input('> ').upper()
            if move == 'SALIR' or move == 'S':
                print('Gracias por jugar!')
                sys.exit()

            if move in ('L', 'V', 'M', 'T','B'):
                return move

    def selecCubo(self, mensaje):
        """
        Selecciona uno de los 3 cubos
        :param mensaje: str
        :return: str
        """
        while True:
            print(mensaje)
            cuboOrigen = input('> ').upper()

            if cuboOrigen in ('8', '5', '3'):
                return cuboOrigen

    def VaciarTodos(self):
        """Vacia todos los cubos de agua"""
        self.aguaEnCubos = {'8': 0, '5': 0, '3': 0}

    def llenarTodos(self):
        """Llena todos los cubos de agua"""
        self.aguaEnCubos = {'8': 8, '5': 5, '3': 3}

    def llenarCubo(self, cuboOrigen):
        """
        Llena el cubo seleccionado
        :param cuboOrigen: str
        """
        cuboOrigenTam = int(cuboOrigen)
        self.aguaEnCubos[cuboOrigen] = cuboOrigenTam
        self.pasos += 1

    def vaciarCubo(self, cuboOrigen):
        """
        Vacia el cubo seleccionado
        :param cuboOrigen: str
        """
        self.aguaEnCubos[cuboOrigen] = 0
        self.pasos += 1

    def moverCubo(self, cuboOrigen, cuboDestino):
        """
        Mueve el agua de un cubo a otro
        :param cuboOrigen: str
        :param cuboDestino: str
        :return:
        """
        cuboDestinoTam = int(cuboDestino)
        espacioVacioCuboDestino = cuboDestinoTam - self.aguaEnCubos[cuboDestino]
        aguaEnCuboOrigen = self.aguaEnCubos[cuboOrigen]
        cantidadAMover = min(espacioVacioCuboDestino, aguaEnCuboOrigen)

        # Saco el agua de este cubo
        self.aguaEnCubos[cuboOrigen] -= cantidadAMover

        # Introduzco el agua en este cubo
        self.aguaEnCubos[cuboDestino] += cantidadAMover
        self.pasos += 1

    def jugar(self):
        """Comienza el juego"""
        self.mostrarEstadoCubos()
        while True:
            opcion = self.selecOpcion()
            if opcion == 'L':
                cubo = self.selecCubo('Selecciona el cubo 8, 5, 3 o SALIR:')
                self.llenarCubo(cubo)
            elif opcion == "V":
                cubo = self.selecCubo('Selecciona el cubo 8, 5, 3 o SALIR:')
                self.vaciarCubo(cubo)
            elif opcion == "M":
                cuboOrigen = self.selecCubo('Selecciona el cubo ORIGEN 8, 5, 3 o SALIR:')
                cuboDestino = self.selecCubo('Selecciona el cubo DESTINO 8, 5, 3 o SALIR:')
                self.moverCubo(cuboOrigen, cuboDestino)
            elif opcion == "B":
                self.VaciarTodos()
            elif opcion == "T":
                self.llenarTodos()
            self.mostrarEstadoCubos()
            self.checkObjetivo()


if __name__ == "__main__":

    juego = juegoCubos(4)
    juego.jugar()
