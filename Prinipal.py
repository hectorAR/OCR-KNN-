# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:44:54 2016

@author: Hector HP
"""
from OCR import DataSet
from KNNFinal import knn

Data = DataSet()
KnnFinal = knn()
opc = 0
while(opc != 3):
    print("Menu")
    opc = int(input("1.- Crear Dataset\n2.- Clasificar con KNN\n3.- Salir\n  Opcion:"))
    if(opc == 1):
        Data.main()
    elif(opc == 2):
        print ("entra")
        KnnFinal.main()
    else:
        print("Programa Finalizado")