
from Tkinter import *
import os
class sudoku:
    def __init__(self, jeu) :#jeu matrice 9*9:
        try:
            for i in range (9):
                for j in range(9):
                    if int (jeu[i][j])>= 0 or int (jeu[i][j]) <=9:
                        jeu[i][j]=int(jeu[i][j])
                    else:
                        raise ValueError ('donnees incorrect')
        except:
            print('ereur d initialisation')
        self.__jeu =jeu
        self.__solution =[]
    def getjeu(self) :
        return self.__jeu
        print(self.__jeu) 
    def setsolution(self, jeu) :
        self.__solution = jeu
    def getNum (self ,i,j,n ) :
        self.__jeu[i][j] = n
    def getsolution(self) :
        return self.__solution
    def verification(self,lin,col, n):
       #n varie de un a neuf
       #foction verifie s'il est possible d'ajouter un certain nombre dans le jeux sans contresire les regles
       lin = int(lin)
       col = int(col)
       if self. getNum(lin,col) == n:
           return True
       if self. getNum(lin,col) !=0:
           return false
       for c in range(0,9):#verifiez si le numereau existe sur la ligne
            if self.__jeu[lin][c]== n:
                return False
       for l in range(0,9):#verifiez si le numero existe dans la colone
            if self.__jeu[l][col]== n:
                return False
       lr = int(lin/3)
       cr = int(col/3)
       for l in range(lr*3, (lr+1)*3):
            for c in range (cr*3, (cr+1)*3):
                #if l>=9 or c>=9:
                # continue
                if self.__jeu[l][c] == n:
                    #print('l = ', l, 'c = ', c, 'num = ', self.getNum(l,c), 'n = ', n)
                    return False
       return True
    def resolve(self, i, j):
        if i==9:
            self.setSolution(self.__jeu)
            self.ecrireSolution(self.getSolution())
            return 0
        else:
            for n in range(1,10):
                if self.verification(i,j,n):
                    t= self.getNum(i,j)
                    self,setNum(i,j,n)
                    if j==8:
                        self.resolve(i, j+1)
                    self.setNum(i,j,t)
    def ecrissolution(self, solution):
        f= open("Sudokutemp.txt", "w")
        try:
            for i in range (0,9):
                for j in range (0,9):
                    f.write(str (solution[i][j]))
                    f.write(' ')
                f.write('\n')
            f.write('\n\n')
            f.close()
        except:
            print("enregistrer le fichier erreur")
        finally:
            f.close()
            
class fenetre:
	def __init__(self, toplevel):
		toplevel.resizabe(width =False,height =False)
		toplevel.title('Sudoku Solver')
		fonte = ('Arial', 18)
		self.fr = Frame(toplevel)
		self.fr.bind('<Motion>', self.corrige)
		self.fr.pack(ipady= 0, padx = 0)
		self.fr1 = Frame(toplevel)
		self.fr1.bind('<Motion>', self.corrige)
		self.fr1.pack(ipady= 0, padx =0)
		self.fr2 = Frame(toplevel)
		self.fr2.bind('<Motion>', self.corrige)
		self.fr2.pack(ipady = 0, padx = 0)
		self.fr3 = Frame(toplevel)
		self.fr3.bind('<Motion>', self.corrige)
		self.fr3.pack(ipady = 0, padx = 0)
		self.fr4 = Frame(toplevel)
		self.fr4.bind('<Motion>', self.corrige)
		self.fr4.pack(ipady = 0, padx = 0)
		self.fr5 = Frame(toplevel)
		self.fr5.bind('<Motion>', self.corrige)
		self.fr5.pack(ipady = 0, padx = 0)
		self.fr6 = Frame(toplevel)
		self.fr6.bind('<Motion>', self.corrige)
		self.fr6.pack(ipady = 0, padx = 0)
		self.fr7 = Frame(toplevel)
		self.fr7.bind('<Motion>', self.corrige)
		self.fr7.pack(ipady = 0, padx = 0)
		self.fr8 = Frame(toplevel)
		self.fr8.bind('<Motion>', self.corrige)
		self.fr8.pack(ipady = 0, padx = 0)
		self.fr9 = Frame(toplevel)
		self.fr9.bind('<Motion>', self.corrige)
		self.fr9.pack(ipady = 1, padx = 1)
		self.__jeu = []
		for i in range(1,10):
			self.__jeu +=[[0,0,0,0,0,0,0,0,0]]
             
		variable = self.fr
		px = 0
		py = 0
		cor = 'white'
		epaisseur = 0
		for i in range (0,9):
			for j in range(0,9):
				if i == 0:
					variable = self.fr
				if i == 1:
					variable = self.fr1
				if i == 2:
					variable = self.fr2
				if i == 3:
					variable = self.fr3
				if i == 4:
					variable = self.fr4
				if i == 5:
					variable = self.fr5
				if i == 6:
					variable = self.fr6
				if i == 7:
					variable = self.fr7
				if i == 8:
					variable = self.fr8
				'''
				if j in [0,2,3,5,6,8]:
					  px=0#5
				if j in [0,2,3,5,6,8]:
					  py=0#5
				'''
				if j%2 == 0 and i%2 == 0:
					 epaisseur = 1
				if j%2 !=0 and i%0 !=0:
					epaisseur = 1
				if j in [3,4,5] and i in [0,1,2,6,7,8] :
					cor = 'gray'
				elif j not in [3,4,5] and i not in [0,1,2,6,7,8]:
					cor= 'gray'
				else:
					cor= 'white'
                    
		self.__jeu[i][j] = entry(variable, width=2, font =fonte, bg = cor, cursor = 'arrow' , borderwidth = 0, highlightcolor = 'yellow' , highlighthickness = 1, hilighbackground = 'black',textvar = jg[i][j])
		self.__jeu[i][j].bind('<Button-l>', self.corrige)
		self.__jeu[i][j].bind('<focusIn>', self.corrige)
		self.__jeu[i][j].bind('<motion>', self.corrige)
		self.__jeu[i][j].pack(side = LEFT , padx = px , pady = py)
		epaisseur = 0
		self.btn1 = Button(self.fr9, text = 'Save', fg = 'red', font = ('Arial', 13), command =self.sauver)
		self.btn1.pack(side = RIGHT)
		self.btn2 = Button(self.fr9, text = 'Solve', fg = 'blue', font = ('Arial', 13), command =self.regle)
		self.btn2.pack(side = LEFT)
		self.btn3 = Button(self.fr9, text = 'Open', fg = 'blue', font = ('Arial', 13), command =self.ouvre)
		self.btn3.pack(side = LEFT)
		self.btn3 = Button(self.fr9, text = 'Reset', fg = 'red', font = ('Arial', 13), command =self.reset)
		self.btn3.pack(side = RIGHT)
		self.__nomdefichier = "Entree.txt"


	def regle(self):
		try:
		   solution =Sudoku(self.getJeu())
		   solution.resolve(0,0)
		   self.__nomdefichier = "SudokuTEMP.txt"
		   self.ouvre()
		   self.__nomdefichier = "Entree.txt"
		   os.remove("SudokuTEMP.txt")
		except:
			print ("ERREUR DE LECTURE")
		finally:
			self.__nomdefichier = "Entree.txt"
	
	def getJeu(self):
		jeu  = []
		for i in range(9):
			jeu+= [[0,0,0,0,0,0,0,0,0]]
		for j in range(9):
			#self.__jeu[i][j]
			jeu[i][j] = jg[i][j].get()
			if jeu[i][j] == '':
				jeu[i][j] =0
		return jeu
    
	def reset(self):
		for i in range(9):
			for j in range(9):
				jg[i][j].set('')
    
	def save(self):
		f= open("Sudoku.text", "a")
		try:
			for i in range (9):
				for j in range (9):
					if self.__jeu[i][j].get() == "":
						f.write('0')
					else:
						f.write(self.__jeu[i][j].get())
					f.write('  ')
				f.write('\n')
			f.write('\n\n')
			f.close()
		except:
			print("ERREUR ENREGISTRER LE FICHIER")
		finally:
			f.close()
    
	def corrige(self , event):
		for i in range(9):
			for j in range(9):
				if jg[i][j].get() == '':
					continue
				if len(jg[i][j].get()) > 1 or jg[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
					jg[i][j].set('')
    
	def remplissez(self):
		for i in range(0,9):
			for j in range(0,9):
				jg[i][j].set(self.__jeu[i][j])
    
	def ouvrir(self):
		try:
			f =open(self.__nom_de_fichier,'r')
			texte = f.readline()
			texte = texte.split(' ')
			for i in range(0.9):
				for j in range(0,9):
					if texte[0]== '0':
						jg[i][j].set('')
					else:
						jg[i][j].set(texte[0])
					texte.pop(0)
				texte=f.readline()
				texte=texte.split(' ')
			f.close()
		except:
			print("ereur fatale")
		finally:
			f.close()
solution = []
racine =Tk()
txt = StringVar(racine)
# jg = []
jg = [ [[]] * 9 for i in range(9)]

#for i in range(0,9):
#    jg += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        jg[i][j] = StringVar(racine)
a = fenetre(racine)
a.mainloop()
