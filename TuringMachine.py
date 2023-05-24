class TuringMachine:
    def __init__(self) -> None:
        self.master_tape = []
        self.pool = []

    def create_tapes(self, cinta1, cinta2):
        # * Crearemos una lista de 11 elementos, donde los primeros 10 serán los elementos de la cinta y el último tendrá solo B's
        len_cinta1 = len(cinta1)
        len_cinta2 = len(cinta2)

        if len_cinta1 < len_cinta2:
            diferencia = len_cinta2 - len_cinta1
            for i in range(diferencia):
                cinta1 = '0' + cinta1

        elif len_cinta2 < len_cinta1:
            diferencia = len_cinta1 - len_cinta2

            for i in range(diferencia):
                cinta2 = '0' + cinta2

        cadena1 = cinta1
        cadena2 = cinta2

        if len(cinta1) < 10:
            difference = 10 - len_cinta1

            for i in range(difference):
                cinta1 = 'B' + cinta1

        if len(cinta2) < 10:

            for i in range(difference):
                cinta2 = 'B' + cinta2

        # * Agrega los elementos de las cintas a la lista
        tape1 = [i for i in cinta1]
        tape2 = [i for i in cinta2]

        last_tape = ['B', 'B', 'B', '-']

        self.master_tape.append(last_tape)

        for i in range(10):
            self.master_tape.append([tape1[i], tape2[i], 'B', '-'])

        """ for item in self.master_tape:
            print(item) """

        self.steps()
        #return self.master_tape, cadena1, cadena2

    def procedure(self, dato, dato2):
        print(dato, dato2)
        matriz = [['B'] * 11 for _ in range(4)]
        # ingresa los datos de la cadena "dato" a la primera lista de la lista de listas
        posicion = len(matriz[0])-1

        for i in range(len(dato)-1, -1, -1):
            matriz[0][posicion] = dato[i]
            posicion -= 1

        # ingresa los deatos de la cadena "dato2" a la segunda lista de la lista de listas
        posicion2 = len(matriz[1])-1
        for i in range(len(dato2)-1, -1, -1):
            matriz[1][posicion2] = dato2[i]
            posicion2 -= 1

        # comienza todo el proceso de la suma con la maquina de turing
        resultado = len(matriz[1])-1

        bandera = True
        
        while resultado >= 0 and bandera == True:
            if matriz[1][resultado] == '0' and matriz[0][resultado] == '0':
                matriz[2][resultado] = '0'
                matriz[3][resultado] = '0'
                resultado -= 1
                self.pool.append(matriz)

            elif matriz[1][resultado] == '0' and matriz[0][resultado] == '1':
                matriz[2][resultado] = '1'
                matriz[3][resultado] = '0'
                resultado -= 1
                self.pool.append(matriz)

            elif matriz[1][resultado] == '1' and matriz[0][resultado] == '0':
                matriz[2][resultado] = '1'
                matriz[3][resultado] = '0'
                resultado -= 1
                self.pool.append(matriz)

            elif matriz[1][resultado] == '1' and matriz[0][resultado] == '1':
                matriz[2][resultado] = '0'
                matriz[3][resultado] = '1'
                resultado -= 1
                self.pool.append(matriz)

                ban = True
                while ban == True:
                    if matriz[1][resultado] == '0' and matriz[0][resultado] == '0':
                        matriz[2][resultado] = '1'
                        matriz[3][resultado] = '1'
                        resultado -= 1
                        self.pool.append(matriz)

                        ban = False
                    elif matriz[1][resultado] == '0' and matriz[0][resultado] == '1':
                        matriz[2][resultado] = '0'
                        matriz[3][resultado] = '1'
                        resultado -= 1
                        self.pool.append(matriz)

                    elif matriz[1][resultado] == '1' and matriz[0][resultado] == '0':
                        matriz[2][resultado] = '0'
                        matriz[3][resultado] = '1'
                        resultado -= 1
                        self.pool.append(matriz)

                    elif matriz[1][resultado] == '1' and matriz[0][resultado] == '1':
                        matriz[2][resultado] = '1'
                        matriz[3][resultado] = '1'
                        resultado -= 1
                        self.pool.append(matriz)

                    elif matriz[1][resultado] == 'B' and matriz[0][resultado] == 'B':
                        matriz[2][resultado] = '1'
                        matriz[3][resultado] = '1'
                        matriz[3][resultado + 1] = '3'
                        resultado -= 1
                        self.pool.append(matriz)

                        ban = False
                        if (len(matriz[1])-1 - resultado > len(dato)):
                            bandera = False
            elif matriz[1][resultado] == 'B' and matriz[0][resultado] == 'B':
                matriz[2][resultado] = 'B'
                matriz[3][resultado] = '0'
                matriz[3][resultado + 1] = '3'
                resultado -= 1
                bandera = False
                self.pool.append(matriz)

    def steps(self):
        #* Iniciamos el recorrido de la máquina de turing asignado el estado inicial a self.master_tape[-1][3]
        self.master_tape[-1][3] = '0'

        pointer = -1
        finish = False
        self.pool.append(self.master_tape)
        
        while not finish:
            #* Extraemos los elementos en la posición del apuntador
            tape_a = self.master_tape[pointer][0]
            tape_b = self.master_tape[pointer][1]
            tape_state = self.master_tape[pointer][3]

            #* Comenzamos a evaluar los estados
            if tape_state == '0':
                if tape_a == '0' and tape_b == '0':
                    self.master_tape[pointer][2] = '0'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '0'
                    copy = self.master_tape
                    self.pool.append(copy)
                
                elif tape_a == '0' and tape_b == '1':
                    self.master_tape[pointer][2] = '1'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '0'
                    copy = self.master_tape
                    self.pool.append(copy)
                
                elif tape_a == '1' and tape_b == '0':
                    self.master_tape[pointer][2] = '1'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '0'
                    copy = self.master_tape
                    self.pool.append(copy)
                
                elif tape_a == '1' and tape_b == '1':
                    self.master_tape[pointer][2] = '0'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '1' #* Declaramos el estado 1
                    copy = self.master_tape
                    self.pool.append(copy)
                
                elif tape_a == 'B' and tape_b == 'B':
                    self.master_tape[pointer][2] = 'B'
                    self.master_tape[pointer][3] = '-'
                    pointer += 1 #* Movemos el apuntador a la derecha
                    self.master_tape[pointer][3] = '3' #* Declaramos el estado 3
                    copy = self.master_tape
                    self.pool.append(copy)
                    finish = True #* Terminamos el ciclo
                
            elif tape_state == '1':
                if tape_a == '0' and tape_b == '0':
                    self.master_tape[pointer][2] = '1'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '0' #* Declaramos el estado 0
                    copy = self.master_tape
                    self.pool.append(copy)
                
                if tape_a == '0' and tape_b == '1':
                    self.master_tape[pointer][2] = '0'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '1' #* Declaramos el estado 1
                    copy = self.master_tape
                    self.pool.append(copy)
                
                if tape_a == '1' and tape_b == '0':
                    self.master_tape[pointer][2] = '0'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '1'
                    copy = self.master_tape
                    self.pool.append(copy)

                if tape_a == '1' and tape_b == '1':
                    self.master_tape[pointer][2] = '1'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    copy = self.master_tape
                    self.pool.append(copy)
                    self.master_tape[pointer][3] = '1'
                
                if tape_a == 'B' and tape_b == 'B':
                    self.master_tape[pointer][2] = 'B'
                    self.master_tape[pointer][3] = '-'
                    pointer += 1 #* Movemos el apuntador a la derecha
                    self.master_tape[pointer][3] = '3' #* Declaramos el estado 3
                    copy = self.master_tape
                    self.pool.append(copy)
                    finish = True #* Terminamos el ciclo
        
        for item in self.pool:
            print('-------------------')
            for subitem in item:
                print(subitem)
if __name__ == '__main__':
    turing = TuringMachine()
    turing.create_tapes('0101010', '1101')
