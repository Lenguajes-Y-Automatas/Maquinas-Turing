import tkinter as tk
from tkinter import messagebox as MessageBox
import time

class maquina:
    def turing(self, dato, dato2):

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
                elif matriz[1][resultado] == '0' and matriz[0][resultado] == '1':
                    matriz[2][resultado] = '1'
                    matriz[3][resultado] = '0'
                    resultado -= 1
                elif matriz[1][resultado] == '1' and matriz[0][resultado] == '0':
                    matriz[2][resultado] = '1'
                    matriz[3][resultado] = '0'
                    resultado -= 1
                elif matriz[1][resultado] == '1' and matriz[0][resultado] == '1':
                    matriz[2][resultado] = '0'
                    matriz[3][resultado] = '1'
                    resultado -= 1
                    ban = True
                    while ban == True:
                        if matriz[1][resultado] == '0' and matriz[0][resultado] == '0':
                            matriz[2][resultado] = '1'
                            matriz[3][resultado] = '1'
                            resultado -= 1
                            ban = False
                        elif matriz[1][resultado] == '0' and matriz[0][resultado] == '1':
                            matriz[2][resultado] = '0'
                            matriz[3][resultado] = '1'
                            resultado -= 1

                        elif matriz[1][resultado] == '1' and matriz[0][resultado] == '0':
                            matriz[2][resultado] = '0'
                            matriz[3][resultado] = '1'
                            resultado -= 1

                        elif matriz[1][resultado] == '1' and matriz[0][resultado] == '1':
                            matriz[2][resultado] = '1'
                            matriz[3][resultado] = '1'
                            resultado -= 1

                        elif matriz[1][resultado] == 'B' and matriz[0][resultado] == 'B':
                            matriz[2][resultado] = '1'
                            matriz[3][resultado] = '1'
                            matriz[3][resultado + 1] = '3'
                            resultado -= 1
                            ban = False
                            if (len(matriz[1])-1 - resultado > len(dato)):
                                bandera = False
                elif matriz[1][resultado] == 'B' and matriz[0][resultado] == 'B':
                    matriz[2][resultado] = 'B'
                    matriz[3][resultado] = '0'
                    matriz[3][resultado + 1] = '3'
                    resultado -= 1
                    bandera = False

            # Imprimir la matriz
            for fila in matriz:
                print(fila)

if __name__ == "__main__":
    objeto = maquina()
    objeto.turing('010101', '010101')