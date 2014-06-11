'''
Created on 23/05/2014

@author: raul
'''
from Geometry.Point import Point2D
from Geometry.Point import ControlPoints
from bezierCurveAlgorithms import deCasteljau


'''Imports openCV library for Python and numpy to create the size of the window'''
import cv2
import numpy as np

ix,iy=0,0

class Bezier(object):
    
    def __init__(self):
        cv2.namedWindow('image',cv2.CV_WINDOW_AUTOSIZE) #nome da janela
        self.img = np.zeros((400,800,3), np.float64) #tamanho da janela 400x800,tipo desejado para o array(float64)
        cv2.setMouseCallback('image', self.createPoint, 0) #metodo que chama a funcao createPoint quando usuario clica com o butao esquedo do mouse
        
        self.numero_de_avaliacao=10 # numero de avaliacao inicial=10
        self.color=(255,0,0) #cor do ponto
        self.points=[] #lista de pontos de controle
        self.line_points=[] #lista com os pontos da reta -Falta implementar uma funcao que desenhe a reta
        
        self.selectedPoint=None #variavel que guarda o ponto selecionado (funciona para remover). Falta implementar para mover
        
        #TrackBars para as cores dos pontos, nao sei porque mas nao consigo colocar cores alem de vermelhor,verde e azul
        cv2.createTrackbar('R', 'image',self.color[0],255,self.setR)
        cv2.createTrackbar('G', 'image',self.color[1],255,self.setG)
        cv2.createTrackbar('B', 'image',self.color[2],255,self.setB)
        
        #trackbar para o usuario ter a liberdade de escolher a quantidade de avaliacoes
        cv2.createTrackbar('Qnte.Avaliacoes', 'image', self.numero_de_avaliacao,1000,self.set_number_avaliation)
        
  
    '''
    Funcoes que setam o valor da tupla color
    '''
    def setR(self,r):
        self.color=list(self.color)
        self.color[0]=r
        self.color=tuple(self.color)
    def setG(self,g):
        self.color=list(self.color)
        self.color[1]=g
        self.color=tuple(self.color)
    def setB(self,b):
        self.color=list(self.color)
        self.color[2]=b
        self.color=tuple(self.color)
    def set_number_avaliation(self,number):
        self.numero_de_avaliacao=number
        self.updateImage(self.points)
    
    '''
    Funcao main
    '''
    def main(self):
        #loop
        while True:  
            cv2.imshow("image",self.img)
            k=cv2.waitKey(0)
            if k==27: #esc
                break
            elif k==100: # 'd' - draw points
                cp=ControlPoints(self.points) #instacia os pontos de controle
                curve=deCasteljau.bezier_curve_generator(cp) #curve eh uma funcao que eh retornada pelo generator
                n=[x * (float(1)/self.numero_de_avaliacao) for x in range(0, self.numero_de_avaliacao+1)] #iteracao 0,....,1
                pointsCurve=[] #lista para os pontos da curva
                for i in n:
                    p=curve(i)
                    pointsCurve.append(p)
                self.drawCurve(pointsCurve) #chama funcao para desenhar a curva
            elif k==114: # 'r' - remove
                cv2.setMouseCallback('image', self.removePoint, 0) #callback para remover o ponto
            elif k==109: # 'm' - move
                #implementar funcao para mover ponto
                cv2.setMouseCallback('image', self.movePoint, 0)
                pass
                
        cv2.destroyWindow("image")
        
    # Funcao que deve ser usada para desenhar uma reta
    def drawLine(self,points):
        for i in range(1,len(points)):
            cv2.line(self.img,(int(points[i-1].X),int(points[i-1].Y)),(int(points[i].X),int(points[i].Y)),(255,255,255),1)
    
    #Funcao que desenha a Curva de Bezier
    def drawCurve(self,points):  
        for i in range(1,len(points)):
            cv2.line(self.img,(int(points[i-1].X),int(points[i-1].Y)),(int(points[i].X),int(points[i].Y)),(255,255,255),1)
    
    #Funcao callback para mover o ponto selecionado em tempo real quando o usuario segura a tecla 'm'
    def movePoint(self,event,x,y,flag=0,param=None):
        if event==cv2.EVENT_LBUTTONDOWN:
            self.selectedPoint=self.findPoint(x,y)
        elif event==cv2.EVENT_MOUSEMOVE and self.selectedPoint!=None:
            self.selectedPoint.move(x,y)
            self.updateImage(self.points)
        elif event==cv2.EVENT_LBUTTONUP and self.selectedPoint!=None:
            self.selectedPoint.move(x,y)
            self.selectedPoint=None
        if self.selectedPoint==None:
            cv2.setMouseCallback('image', self.createPoint, 0) #atualiza o callback
   
            
        
    #Funcao callback para remover o ponto selecionado quando o usuario segura a tecla 'r'
    def removePoint(self,event,x,y,flag=0,param=None):
        self.selectedPoint=self.findPoint(x,y)
        if self.selectedPoint!=None:
            self.points.remove(self.selectedPoint)
            self.updateImage(self.points)
            self.selectedPoint=None
        if self.selectedPoint==None:
            cv2.setMouseCallback('image', self.createPoint, 0) #atualiza o callback
    
    
            
    #Funcao callback para criar ponto de controle quando o usuario preciona 'd'
    def createPoint(self,event,x,y,flag=0,param=None):
        if event==cv2.EVENT_LBUTTONDOWN:
            p = Point2D(x,y)
            self.points.append(p)
            #desenha um ponto de controle na imagem
            cv2.line(self.img,(p.X,p.Y),(p.X,p.Y),self.color,10)
            #chama funcao para atualizar a imagem
            self.updateImage(self.points)
        
        
        
    #Funcao para achar um ponto que o usuario deseja remover ou mover
    def findPoint(self,x,y):
        point=None
        for i in self.points:
            if i.X==x and i.Y==y:
                point=i
                break
        return point
 
    #Funcao para atualizar a imagem
    def updateImage(self,points):
        cv2.namedWindow('image',cv2.CV_WINDOW_AUTOSIZE) #nome da janela
        self.img = np.zeros((400,800,3), np.float64)    
        for point in points:
            cv2.line(self.img,(point.X,point.Y),(point.X,point.Y),self.color,10)
        cv2.imshow('image',self.img)
            

    
  
        

if __name__=="__main__":
    b=Bezier()
    b.main()
