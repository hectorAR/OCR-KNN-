# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:49:42 2016

@author: Hector HP
"""
import csv
import math
import operator
from PIL import Image
import matplotlib.image as mpimg
from OCR import DataSet

trainingSet=[]#creamos un arreglo
class knn():#creamos una clases 
    def cargarDataset(archivo):#metodo de cargara data set
        global trainingSet#variable de un arreglo
        with open(archivo, newline='') as csvfile:#abre el archivo y recorre linea por lines
            lines = csv.reader(csvfile, delimiter= ';')#se almacena una linea y se cepara por el punto y coma
            dataset = list(lines)#lee linea por linea y lo almacena
            for x in range(len(dataset)-1):#recoere nuestra matriz
                for y in range(13):#recorre nuestra matriz
                    dataset[x][y] = float(dataset[x][y])#se almacena en la matriz dataset 
                trainingSet.append(dataset[x])
        csvfile.close()#se cierra e; archivo csv
        
    def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

    def getNeighbors(testInstance, k):
        global trainingSet
        distances=[]
        valor=0
        neighbors = []
        length = len(testInstance)-1
        for x in range(len(trainingSet)):
            dist = knn.euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))#ordena de menor a mayor
        for x in range(k):
            print("Linea(Instancia): "+str(distances[x][0][15])+ " Clase: "+str(distances[x][0][14])+" Distancia: "+str(distances[x][1]))            
            neighbors.append(distances[x][0])
        return neighbors

    def getResponse(neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-2]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]
    
    def obtenerCaract(self,ruta):#Resive 
        data = []#se declara arreglo para guardar las caaracteristicas
        imgPrincipal = Image.open(ruta) #Abre imagne
        img = mpimg.imread(ruta) #Abre imagen
        columnas, filas = imgPrincipal.size #Se obtienen las filas y columnas
    
        #Se insertan datos en el array data
        data.append(DataSet.Propiedad_1(filas,columnas))#Se acquiere la propiedad 1 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_2(img,filas,columnas))#Se adquiere la propiedad 2 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_3(img,filas,columnas))#Se adquiere la propiedad 3 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_4(img,filas,columnas))#Se adquiere la propiedad 4 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_5(img,filas,columnas))#Se adquiere la propiedad 5 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_6(img,filas,columnas))#Se adquiere la propiedad 6 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_7(img,filas,columnas))#Se adquiere la propiedad 7 de la imagen que se llama a llamar de la clase OCR        
        data.append(DataSet.Propiedad_8(img,filas,columnas))#Se adquiere la propiedad 8 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_9(img,filas,columnas))#Se adquiere la propiedad 9 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_10(img,filas,columnas))#Se adquiere la propiedad 10 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_11(img,filas,columnas))#Se adquiere la propiedad 11 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_12(img,filas,columnas))#Se adquiere la propiedad 12 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_13(img,filas,columnas))#Se adquiere la propiedad 13 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_14(img,filas,columnas))#Se adquiere la propiedad 14 de la imagen que se llama a llamar de la clase OCR

        return data#Retorna el arreglo que se almacenaron las propiedades
        
    def __init__(self):
        pass
    
    def main(self):#metodo main
        global trainingSet#se declara el arreglo que almacena
        knn.cargarDataset('dataset.csv')#abre el data set que deseamos comparar
        #print(trainingSet)
        ruta = 'C:/Users/Hector HP/Desktop/OCR FINAL/comparar/'#Ruta donde estan las imagenes donde se tomaran sus caracteristicas
        ruta += input("Ingresa el nombre de la imagen: ")#Pide el nombre de la imagen con su estancion PNG
        data =knn.obtenerCaract(self,ruta)#Manda a llamar el metodo donde se odtiene las caracteristicas de la imagen
        k = int(input("Ingresa el numero K: "))#ingresa el numero de vecinos que tiene que comparar
        resultado=knn.getResponse(knn.getNeighbors(data,k))#El metodo regresa con la comparacion con los vecinos mas cercanos
        print ("============================================================")
        print("\n   La imagen es un: "+str(resultado))#Imprime la clase que se repitio mas veces
        print ("============================================================")
        del trainingSet[:]
        #print (data)