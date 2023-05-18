import tkinter as tk
from tkinter import messagebox as MessageBox
import time
class maquina:
    def turing(self,dato,dato2):
        bandera_dato = True
        bandera_dato2 = True
        for o in range (len(dato)):
            if dato[o] != '0' and dato[o] != '1':
                bandera_dato = False
        for p in range (len(dato2)):
            if dato2[p] != '0' and dato2[p] != '1':
                bandera_dato2 = False
       

        if len(dato) == len(dato2) and len(dato) <= 10 and len(dato2) <= 10 and bandera_dato == True and bandera_dato2 == True:
            # Crear una matriz de 3x10 con la letra "B"
            matriz = [['B'] * 10 for _ in range(4)]
            """ matriz.append([''] * 10)  """

            # Pedir un dato como cadena con un máximo de 10 caracteres123
            """ dato = input("Ingrese numero binario (máximo 10 caracteres): ")[:10] """

            posicion = len(matriz[0])-1
            for i in range(len(dato)-1, -1, -1):
                matriz[0][posicion] = dato[i]
                posicion -= 1

            """ dato2 = input("Ingrese otro numero binario (máximo 10 caracteres): ")[:10] """

            posicion2 = len(matriz[1])-1
            for i in range(len(dato2)-1, -1, -1):
                matriz[1][posicion2] = dato2[i]
                posicion2 -= 1



            posicion2 = len(matriz[1])-1
            for i in range(len(dato2)-1, -1, -1):
                matriz[1][posicion2] = dato2[i]
                posicion2 -= 1

            """ matriz[3][len(matriz[3])-1] = 'aqui' """

            """ # Imprimir la matriz
            for fila in matriz:
                print(fila) """

        
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
                            if (len(matriz[1])-1 - resultado  > len(dato)):
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
          
        else:
            MessageBox.showinfo("Alerta", "Los datos deben contener menos de 10 caracteres (0,1) y ser de igual longitud ") # título, mensaje



        
           
        