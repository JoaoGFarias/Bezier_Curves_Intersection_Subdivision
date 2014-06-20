'''
Created on 11/06/2014

@author: raul
'''

from Geometry.Point import Point2D
from Geometry.Point import ControlPoints
from bezierCurveAlgorithms import deCasteljau


'''Imports openCV library for Python and numpy to create the size of the window'''
import cv2
import numpy as np
import random

max_points=20
w=792 # x maximo
h=391 # y maximo
class BezierTest(object):
    
    def __init__(self):
        cv2.namedWindow('image',cv2.CV_WINDOW_AUTOSIZE) #nome da janela
        self.img = np.zeros((400,800,3), np.float64) #tamanho da janela 400x800,tipo desejado para o array(float64)
        
        self.points=[]
        self.pos_point=[]
        self.numero_de_avaliacao=10000
        self.selectedPoint=None
        self.color=(255,0,0) #cor do ponto
        for i in range(max_points):
            x=random.randint(1,w)
            y=random.randint(1,h)
            if (x,y) not in self.pos_point:
                p = Point2D(x,y)
                self.points.append(p)
                cv2.line(self.img,(p.X,p.Y),(p.X,p.Y),self.color,10)
                self.pos_point.append((x,y))
        self.updateImage(self.points)
        
            
    def main(self):
        while True:
            cv2.imshow('image',self.img)
            k=cv2.waitKey(1)
            
            if max_points==0 or k==27:
                break
            else:
                choice=random.randint(1,3)
                if choice==1:
                    print "removing point"
                    self.removePoint()
                elif choice==2:
                    print "moving point"
                    self.movePoint()
                elif choice==3 and max_points<20:
                    print "adding point"
                    self.createPoint()
        cv2.destroyWindow("image")
        
    def removePoint(self):
        global max_points
        self.selectedPoint=self.points[random.randint(0,max_points-1)]
        self.points.remove(self.selectedPoint)
        self.selectedPoint=None
        max_points-=1
        self.updateImage(self.points)
    def createPoint(self):
        global max_points
        x=random.randint(1,w)
        y=random.randint(1,h)
        if (x,y) not in self.pos_point:
            p = Point2D(x,y)    
            self.points.append(p)
            #desenha um ponto de controle na imagem
            cv2.line(self.img,(p.X,p.Y),(p.X,p.Y),self.color,10)
            #chama funcao para atualizar a imagem
            self.pos_point.append((x,y))
            self.updateImage(self.points)
            max_points+=1
            
    #Funcao para achar um ponto que o usuario deseja remover ou mover
    def findPoint(self,x,y):
        point=None
        for i in self.points:
            if i.X==x and i.Y==y:
                point=i
                break
        return point
 
    def movePoint(self):
        self.selectedPoint=self.points[random.randint(0,max_points-1)]
        self.pos_point.remove((self.selectedPoint.X,self.selectedPoint.Y))
        x=random.randint(1,w)
        y=random.randint(1,h)
        if (x,y) not in self.pos_point:
            self.selectedPoint.move(x,y)
            self.updateImage(self.points)
            self.pos_point.append((x,y))
      
    #Funcao para atualizar a imagem
    def updateImage(self,points):
        cv2.namedWindow('image',cv2.CV_WINDOW_AUTOSIZE) #nome da janela
        self.img = np.zeros((400,800,3), np.float64)    
        for point in points:
            cv2.line(self.img,(point.X,point.Y),(point.X,point.Y),self.color,10)
        if(len(self.points)>2):
            self.drawCurve()
        cv2.imshow('image',self.img)
    #Funcao que desenha a Curva de Bezier
    def drawCurve(self):
        cp=ControlPoints(self.points) #instacia os pontos de controle
        curve=deCasteljau.bezier_curve_generator(cp) #curve eh uma funcao que eh retornada pelo generator
        n=[x * (float(1)/self.numero_de_avaliacao) for x in range(0, self.numero_de_avaliacao+1)] #iteracao 0,....,1
        pointsCurve=[] #lista para os pontos da curva
        for i in n:
            p=curve(i)
            pointsCurve.append(p)
        for i in range(1,len(pointsCurve)):
            cv2.line(self.img,(int(pointsCurve[i-1].X),int(pointsCurve[i-1].Y)),(int(pointsCurve[i].X),int(pointsCurve[i].Y)),(255,255,255),1)
            

if __name__=="__main__":
    b=BezierTest()
    b.main()
            
            
        
        
        
        
        
        
        
        
        
        