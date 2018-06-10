import tkinter as tk


class Gui(tk.Tk):

	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		self.title("Tic Tac Toe")
		self.config(bg ="white")
		container = tk.Frame(self)
		container.pack()

		self.frames = {}

		for f in (Main_menu_page,Info_player_page,Grid_size,Draw_grid):
			frame = f(container,self)
			self.frames[f]= frame
			frame.grid(row=0,column=0,sticky="nsew")

		self.show_frame(Main_menu_page)

	def show_frame(self, context):

		frame = self.frames[context]
		frame.tkraise()
		
class Main_menu_page(tk.Frame) :

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		logo_canvas = tk.Canvas(self,width = 477, height = 329)
		self.logo = tk.PhotoImage(file = "Morpion.gif")
		logo_canvas.create_image(239,165,image=self.logo)
		logo_canvas.grid(row = 0,column = 0,columnspan=5)

		one_Player_button = tk.Button(self,text = "1 Player",command= lambda:controller.show_frame(Info_player_page))
		one_Player_button.grid(row = 1, column = 2,sticky="ew")

		two_Player_button = tk.Button(self,text = "2 Player",command=lambda:controller.show_frame(Info_player_page))
		two_Player_button.grid(row = 2, column = 2,sticky ="ew")

		quit_button = tk.Button(self,text = "Quit",command=quit)
		quit_button.grid(row = 3,column = 4)

class Info_player_page(tk.Frame):

		def __init__(self,parent,controller):

			tk.Frame.__init__(self,parent)
			back_button = tk.Button(self,text = "< Back",command = lambda:controller.show_frame(Main_menu_page)) 
			quit_button = tk.Button(self,text = "quit", command = quit)

			tk.Label(self,text="Name : ").grid(row = 0,column=0)
			playerName = tk.StringVar()
			EntryName = tk.Entry(self,textvariable=playerName)
			EntryName.grid(row = 0,column = 1)

			tk.Label(self,text= "sign : ").grid(row = 1, column = 0)
			choice_X = tk.Button(self,text="X",command = lambda: controller.show_frame(Grid_size))
			choice_X.grid(row = 1,column = 1,sticky="w")
			
			choice_O = tk.Button(self,text="O",command = lambda: controller.show_frame(Grid_size))
			choice_O.grid(row = 1, column = 1,sticky = "e")
			
			back_button.grid(row = 2, column = 0)
			quit_button.grid(row = 2, column = 1)

class Grid_size(tk.Frame):	

	def __init__(self,parent,controller):
		
		tk.Frame.__init__(self,parent)
		back_button = tk.Button(self,text = "< Back",command = lambda:controller.show_frame(Info_player_page)) 
		quit_button = tk.Button(self,text = "quit", command = quit)

		size9_buttton = tk.Button(self,text = "3x3",command = lambda: controller.show_frame(Draw_grid))
		size15_button = tk.Button(self,text = "3x5",command = lambda: controller.show_frame(Draw_grid)) 
		size16_button = tk.Button(self,text = "4x4",command = lambda: controller.show_frame(Draw_grid))

		size9_buttton.grid(row = 0, column = 1)
		size15_button.grid(row = 1, column = 1)
		size16_button.grid(row = 2, column = 1)
		back_button.grid(row = 3, column = 0)
		quit_button.grid(row = 3, column = 2)

class Draw_grid(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		quit_button = tk.Button(self,text = "quit", command = quit)
		quit_button.grid(row = 5, column = 4 )

		tk.Label(self,text="Player 1").grid(row = 0, column = 0)
		tk.Label(self,text="Player 2").grid(row = 0, column = 4)

		for i in range(1,4):
			for j in range (1,4):
				tk.Button(self).grid(row = i , column = j)	

