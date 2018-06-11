from Player import *
import tkinter as tk


class Gui(tk.Tk):
	"""
		Create main window and show good 
	"""
	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		self.title("Tic Tac Toe")
		self.config(bg ="white")
		self.container = tk.Frame(self)
		self.container.pack()

		self.frames = {}
		self.shared_data = {}

		for f in (Main_menu_page,Board_size):
			frame = f(self.container,self)
			self.frames[f]= frame
			frame.grid(row=0,column=0,sticky="nsew")

		self.show_frame(Main_menu_page)

	def show_frame(self, context):
		
		frame = self.frames[context]
		frame.tkraise()

class Main_menu_page(tk.Frame) :
	"""
		Menu Frame : First frame created at beging of App
	"""
	def __init__(self,parent,controller):
		#create for diply button, ...
		tk.Frame.__init__(self,parent)
		self.controller = controller
		#create canvas for show one logo
		logo_canvas = tk.Canvas(self,width = 477, height = 329)
		#load image for logo
		self.logo = tk.PhotoImage(file = "Image/Morpion.gif")
		#display image
		logo_canvas.create_image(239,165,image=self.logo)
		logo_canvas.grid(row = 0,column = 0,columnspan=5)

		#create button for start game with one player
		one_Player_button = tk.Button(self,text = "1 Player",command= lambda:self.show_info_player(1))
		one_Player_button.grid(row = 1, column = 2,sticky="ew")

		#create button for start game with two player
		two_Player_button = tk.Button(self,text = "2 Player",command=lambda:self.show_info_player(2))
		two_Player_button.grid(row = 2, column = 2,sticky ="ew")

		#create quit button
		quit_button = tk.Button(self,text = "Quit",command=quit)
		quit_button.grid(row = 3,column = 4, sticky="ew")

	def show_info_player(self,nbPlayer):
			frame = Info_player_page(self.controller.container,self.controller,nbPlayer)
			self.controller.frames["Info_player1"]= frame
			frame.grid(row=0,column=0,sticky="nsew")

class Info_player_page(tk.Frame):
	"""
		Frame for information about player
	"""
	def __init__(self,parent,controller,nbPlayer):

		#create frame
		tk.Frame.__init__(self,parent)
		self.controller = controller
		self.nb = 1
		#create back and quit button 
		# back button use for comem back to menu
		back_button = tk.Button(self,text = "< Back",command = lambda:controller.show_frame(Main_menu_page)) 
		quit_button = tk.Button(self,text = "quit", command = quit)
		tk.Label(self,text="Player",font= ("Heleviat", 35)).grid(row = 0,column = 0 ,columnspan = 5 )
		#create label and entry for user nickname
		tk.Label(self,text="Name : ").grid(row = 1,column=0)
		self.playerName = tk.StringVar()
		EntryName = tk.Entry(self,textvariable=self.playerName)
		EntryName.grid(row = 1,column = 1, columnspan = 3)
		EntryName.focus()

		#button for choice symbol durin game
		tk.Label(self,text= "sign : ").grid(row = 2, column = 0)
		choice_X = tk.Button(self,text="X",command = lambda: self.create_player("X",nbPlayer))
		choice_X.grid(row = 2,column = 1, sticky="ew")
		
		choice_O = tk.Button(self,text="O",command = lambda: self.create_player("O",nbPlayer))
		choice_O.grid(row = 2, column = 2, sticky="ew")
		
		back_button.grid(row = 3, column = 0, sticky="ew")
		quit_button.grid(row = 3, column = 3, sticky="ew")

	def create_player(self,symbol,nbPlayer):

		if nbPlayer - 1 == 0 :
			player = Player(self.playerName.get(),symbol)
			self.controller.shared_data["player"+str(nbPlayer)]=player
			self.controller.show_frame(Board_size)
		else:
			player = Player(self.playerName.get(),symbol)
			self.controller.shared_data["player"+str(nbPlayer)] =player
			frame = Info_player_page(self.controller.container,self.controller,nbPlayer-1)
			self.controller.frames["Info_player2"]= frame
			frame.grid(row=0,column=0,sticky="nsew")


class Board_size(tk.Frame):	
	"""
		Menu for game size 
	"""
	def __init__(self,parent,controller):
		

		tk.Frame.__init__(self,parent)
		self.controller = controller

		back_button = tk.Button(self,text = "< Back",command = lambda:controller.show_frame(Info_player_page)) 
		quit_button = tk.Button(self,text = "quit", command = quit)

		# create button for differente choice of size
		size9_buttton = tk.Button(self,text = "3x3",command = lambda: self.create_board(3,3))
		size15_button = tk.Button(self,text = "3x5",command = lambda: self.create_board(3,5)) 
		size16_button = tk.Button(self,text = "4x4",command = lambda: self.create_board(4,4))

		size9_buttton.grid(row = 0, column = 1)
		size15_button.grid(row = 1, column = 1)
		size16_button.grid(row = 2, column = 1)
		back_button.grid(row = 3, column = 0, sticky="ew")
		quit_button.grid(row = 3, column = 2, sticky="ew")

	def create_board(self,x,y):
						
		frame = Game_board(self.controller.container,self.controller,x,y)
		self.controller.frames[Game_board]= frame
		frame.grid(row=0,column=0,sticky="nsew")

class Game_board(tk.Frame):

	def __init__(self,parent,controller,x,y):

		tk.Frame.__init__(self,parent)
		self.controller = controller
		quit_button = tk.Button(self,text = "quit", command = quit)
		self.x = x
		self.y = y

		tk.Label(self,text=self.controller.shared_data["player1"].name).grid(row = 0, column = 0)

		for i in range(1,x+1) :
			for j in range (1,y+1):
				tk.Button(self).grid(row = i , column = j)

		quit_button.grid(row = 5, column = 6 , sticky="ew")
		if "player2" in self.controller.shared_data :
			tk.Label(self,text=self.controller.shared_data["player2"].name).grid(row = 0, column = 6)
		else :
			tk.Label(self,text="Ordi").grid(row = 0, column = 6)
