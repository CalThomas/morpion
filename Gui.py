import tkinter as tk


class Gui():

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Tic Tac Toe")
		self.main_menu()

		self.root.mainloop()

	def main_menu(self):

		self.one_Player_button = tk.Button(self.root,text = "1 Player",command=self.info_player)
		self.one_Player_button.grid(row = 0, column = 0)

		self.two_Player_button = tk.Button(self.root,text = "2 Player",command=self.info_player)
		self.two_Player_button.grid(row = 1, column = 0)

		self.quit_button = tk.Button(self.root,text = "Quit",command=quit)
		self.quit_button.grid(row = 2,column = 1)

	def back_menu(self):

		self.choice_X.grid_forget()
		self.choice_O.grid_forget()
		self.back_button.grid_forget()
		self.quit_button.grid_forget()
		self.one_Player_button.grid_forget()
		self.two_Player_button.grid_forget()
		self.size9_buttton.grid_forget()
		self.size15_button.grid_forget()
		self.size16_button.grid_forget()


		self.main_menu()

	def draw_grid(self):

		self.size9_buttton.grid_forget()
		self.size15_button.grid_forget()
		self.size16_button.grid_forget()
		self.back_button.grid_forget()

		self.quit_button.grid(row = 5, column = 4 )

		tk.Label(text="Player 1").grid(row = 0, column = 0)
		tk.Label(text="Player 2").grid(row = 0, column = 4)

		for i in range(1,4):
			for j in range (1,4):
				tk.Button(self.root).grid(row = i , column = j)	

	def info_player(self):

		self.one_Player_button.grid_forget()
		self.two_Player_button.grid_forget()
		self.back_button = tk.Button(self.root,text = "< Back",command = self.back_menu ) 


		self.choice_X = tk.Button(self.root,text="X",command = self.grid_size)
		self.choice_X.grid(row = 0,column = 0)
		self.choice_O = tk.Button(self.root,text="O",command = self.grid_size)
		self.choice_O.grid(row = 0, column = 1)
		self.back_button.grid(row = 1, column = 0)
		self.quit_button.grid(row = 1, column = 1)

	def grid_size(self):
		self.choice_X.grid_forget()
		self.choice_O.grid_forget()

		self.size9_buttton = tk.Button(self.root,text = "3x3",command = self.draw_grid)
		self.size15_button = tk.Button(self.root,text = "3x5",command = self.draw_grid) 
		self.size16_button = tk.Button(self.root,text = "4x4",command = self.draw_grid)

		self.size9_buttton.grid(row = 0, column = 1)
		self.size15_button.grid(row = 1, column = 1)
		self.size16_button.grid(row = 2, column = 1)
		self.back_button.grid(row = 3, column = 0)
		self.quit_button.grid(row = 3, column = 2)













