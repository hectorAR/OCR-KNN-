# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:47:16 2016

@author: Hector HP
"""
from PIL import Image
import csv
import os
import matplotlib.image as mpimg
cont = 0
class DataSet():
    
    op = open('dataset.csv','a',newline='')
    escribir = csv.writer(op,delimiter=';')
    
    def Conjunto(ruta,clase):
        global cont
        #abrimos imagen
        imgPrincipal = Image.open(ruta)
        img = mpimg.imread(ruta)
        columnas, filas = imgPrincipal.size
        data=[]#arreglo para insertar en el data
        data.append(DataSet.Propiedad_1(filas,columnas))
        data.append(DataSet.Propiedad_2(img,filas,columnas))
        data.append(DataSet.Propiedad_3(img,filas,columnas))
        data.append(DataSet.Propiedad_4(img,filas,columnas))
        data.append(DataSet.Propiedad_5(img,filas,columnas))
        data.append(DataSet.Propiedad_6(img,filas,columnas))
        data.append(DataSet.Propiedad_7(img,filas,columnas))
        data.append(DataSet.Propiedad_8(img,filas,columnas))
        data.append(DataSet.Propiedad_9(img,filas,columnas))
        data.append(DataSet.Propiedad_10(img,filas,columnas))
        data.append(DataSet.Propiedad_11(img,filas,columnas))
        data.append(DataSet.Propiedad_12(img,filas,columnas))
        data.append(DataSet.Propiedad_13(img,filas,columnas))
        data.append(DataSet.Propiedad_14(img,filas,columnas))
        data.append(clase)
        data.append(cont)
        DataSet.escribir.writerow(data)#se escribe en el data
        cont += 1
        
    def Propiedad_1(filas,columnas):
        P_1=columnas/filas
        return P_1
    
    def Propiedad_2(img,filas,columnas):
        numunos=0
        for a in range(filas):
            for b in range(columnas):
                nu=(int(img[a][b]))
                if nu==1:
                    numunos=numunos+1
        unos=numunos/(filas*columnas)
        
        return unos
    
    def Propiedad_3(img,filas,columnas):
        numunos=0
        b=int(columnas/2)
        for a in range (filas):            
             nu=(int(img[a][b]))
             if nu==1:
                 numunos=numunos+1
        p3=numunos/filas
        
        return p3
    
    def Propiedad_4(img,filas,columnas):
        numunos=0
        for a in range (filas):
             b=int(columnas/4)             
             nu=(int(img[a][b]))             
             if nu==1:
                 numunos=numunos+1
        p4=numunos/filas
        
        return p4
    
    def Propiedad_5(img,filas,columnas):
        numunos=0
        for a in range (filas):
             b=int(3*(columnas/4))
             nu=(int(img[a][b]))             
             if nu==1:
                 numunos=numunos+1
        p5=numunos/filas
        
        return p5
    
    def Propiedad_6(img,filas,columnas):
        numunos=0
        numceros=0
        a=int(filas/2)
        for b in range(columnas):            
             nu=(int(img[a][b]))             
             if nu==1:
                 numunos=numunos+1
             else:
                numceros=numceros+1
        p6=numunos/columnas
        
        return p6
    
    def Propiedad_7(img,filas,columnas):
        numunos=0
        numceros=0
        a=int(filas/4)
        for b in range(columnas):             
             nu=(int(img[a][b]))             
             if nu==1:
                 numunos=numunos+1
             else:
                numceros=numceros+1
        p7=numunos/columnas
        
        return p7
    
    def Propiedad_8(img,filas,columnas):
        numunos=0
        numceros=0
        a=int(3*(filas/4))
        for b in range(columnas):
            nu=(int(img[a][b]))             
            if nu==1:
                numunos=numunos+1
            else:
                numceros=numceros+1
        p8=numunos/columnas
        
        return p8
    
    def Propiedad_9(img,filas,columnas):
        nc_1=0
        b=int(columnas/2)
        for a in range (filas):
            if (img[a][b] != img[a-1][b] and a != filas-2 and a != 0):
                nc_1+=1
            if (a==0 or a==(filas-1)):
                if (img[a][b] == 1):
                    nc_1+=1
            
        return nc_1
    
    def Propiedad_10(img,filas,columnas):
        nc=0
        b=int(columnas/4)
        for a in range (filas):
            if (img[a][b] != img[a-1][b] and a != filas-2 and a != 0):
                nc+=1
            if (a==0 or a==(filas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
    
    def Propiedad_11(img,filas,columnas):
        nc=0
        a=int(3*(filas/4))
        for b in range (columnas):
            if (img[a][b] != img[a][b-1] and b != columnas-1):
                nc+=1
            if (b==0 or b==(columnas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
        
    def Propiedad_12(img,filas,columnas):
        nc=0
        a=int(filas/2)
        for b in range (columnas):
            if (img[a][b] != img[a][b-1] and b != columnas-1 and b!=0):
                nc+=1
            if (b==0 or b==(columnas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
    
    def Propiedad_13(img,filas,columnas):
        nc=0
        a=int(filas/4)
        for b in range (columnas):
            if (img[a][b] != img[a][b-1] and b != columnas-1 and b!=0):
                nc+=1
            if (b==0 or b==(columnas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
    
    def Propiedad_14(img,filas,columnas):
        nc=0
        a=int(3*(filas/4))
        for b in range (columnas):
            if (img[a][b] != img[a][b-1] and b != columnas-1 and b!=0):
                nc+=1
            if (b==0 or b==(columnas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
        
    
    def main(self):
        rootDir='arialSegmented'
        cont=0
        
        for base, dirs, files in os.walk(rootDir):
            if cont > 0:
                print("Obteniendo caracteristicas de: " + str(base[len(base)-1]))
                for name in files:
                    DataSet.Conjunto((str(base)+'/'+name),base[len(base)-1])
            cont += 1
        print ("Numero de imagenes examinados: 14,914")
        print ("clases: 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z")
        DataSet.op.close()#se cierra la escritura
        print("     Proceso finalizado!")
        
        def __init__(self):
            pass