import copy
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

        return self.master_tape

    def steps(self):
        #* Iniciamos el recorrido de la máquina de turing asignado el estado inicial a self.master_tape[-1][3]
        self.master_tape[-1][3] = '0'

        pointer = -1
        finish = False
        self.pool.append(copy.deepcopy(self.master_tape))
        
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
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                
                elif tape_a == '0' and tape_b == '1':
                    self.master_tape[pointer][2] = '1'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '0'
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                
                elif tape_a == '1' and tape_b == '0':
                    self.master_tape[pointer][2] = '1'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '0'
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                
                elif tape_a == '1' and tape_b == '1':
                    self.master_tape[pointer][2] = '0'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '1' #* Declaramos el estado 1
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                
                elif tape_a == 'B' and tape_b == 'B':
                    self.master_tape[pointer][2] = 'B'
                    self.master_tape[pointer][3] = '-'
                    pointer += 1 #* Movemos el apuntador a la derecha
                    self.master_tape[pointer][3] = '3' #* Declaramos el estado 3
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                    finish = True #* Terminamos el ciclo
                
            elif tape_state == '1':
                if tape_a == '0' and tape_b == '0':
                    self.master_tape[pointer][2] = '1'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '0' #* Declaramos el estado 0
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                
                if tape_a == '0' and tape_b == '1':
                    self.master_tape[pointer][2] = '0'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '1' #* Declaramos el estado 1
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                
                if tape_a == '1' and tape_b == '0':
                    self.master_tape[pointer][2] = '0'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '1'
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)

                if tape_a == '1' and tape_b == '1':
                    self.master_tape[pointer][2] = '1'
                    self.master_tape[pointer][3] = '-'
                    pointer -= 1 #* Movemos el apuntador a la izquierda
                    self.master_tape[pointer][3] = '1'
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                
                if tape_a == 'B' and tape_b == 'B':
                    self.master_tape[pointer][2] = 'B'
                    self.master_tape[pointer][3] = '-'
                    pointer += 1 #* Movemos el apuntador a la derecha
                    self.master_tape[pointer][3] = '3' #* Declaramos el estado 3
                    my_other_copy = copy.deepcopy(self.master_tape)
                    self.pool.append(my_other_copy)
                    finish = True #* Terminamos el ciclo

        return self.pool

if __name__ == '__main__':
    turing = TuringMachine()
    turing.create_tapes('10101011', '10101011')