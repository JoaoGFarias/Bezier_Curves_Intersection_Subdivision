'''
Created on 07/06/2014

@author: raul
'''
from Tkinter import *
from UI import Bezier


class UI(Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        text = Text(self.master,width=200, height=10)
        text.insert(INSERT, "Description: the user enters via mouse with the control points of one Bezier curve and a line. The number of control points is arbitrary, without limit. The system should draw the figures, curve and line, and present the interpolation parameter values where the line intercepts the Bezier Curve. The approximation intersection method is the subdivision. The user can move, insert and delete points, with the system responding appropriately in real time. The approximation tolerance is adjustable by the user. Assessments should be made compulsory with the De Casteljau algorithm")
        text.insert(END,".\n\n")
        text.insert(INSERT,"Instructions:\n")
        text.insert(INSERT,"1)Clique com botao esquerdo do mouse para criar os pontos de controle.\n")
        text.insert(INSERT,"2)Pressione 'd' para desenhar a curva de bezier.\n")
        text.insert(INSERT,"3)Segure 'r' em cima de um ponto de controle para remove-lo.\n")
        text.insert(INSERT,"4)Segure 'm' em cima de um ponto de controle para move-lo.\n")
        text.insert(INSERT,"5)Mova a trackbar qtd de avaliacoes.Maior valor, maior suavidade.\n")
        text.insert(INSERT,"6)Mova a trackbar R,G,B para mudar as cores dos pontos.\n")
        text.insert(INSERT,"7)Pressione ESC para sair do programa.\n")
        text.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.NEXT = Button(self,command=self.bezier)
        self.NEXT["text"] = "Next"
        self.NEXT.pack({"side": "left"})
        self.pack(side=BOTTOM,padx=100,pady=250)
    
    def bezier(self):
        self.master.destroy()
        b=Bezier()
        b.main()
        
if __name__=="__main__":
    root=Tk()
    root.attributes('-zoomed', True)
    app=UI(master=root)
    app.mainloop()
    