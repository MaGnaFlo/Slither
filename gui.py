from tkinter import *
from tkinter import ttk 

class Bool:
	def __init__(self, b):
		self.b = b

def start_window():
	set_active = Bool(True)

	window = Tk()
	window.title("Slither")
	window.geometry("700x350+300+300")
	window.grid_columnconfigure(0, weight=1)

	frame = ttk.Frame(window, padding=10)
	frame.grid()

	label = ttk.Label(frame, text="Welcome to Slither!")
	label.grid(column=0, row=0)
	label2 = ttk.Label(frame, text="This game is nothing but a Snake. Enjoy!")
	label2.grid(column=0, row=1)

	def start_game():
		set_active.b = True
		window.destroy()

	button = ttk.Button(frame, text="Play!", command=start_game)
	button.grid(column=0, row=2)

	def exit_game():
		set_active.b = False
		window.destroy()

	window.protocol("WM_DELETE_WINDOW", exit_game)

	window.mainloop()

	return set_active.b

def collide_window():
	keep_active = Bool(True)

	window = Tk()
	window.title("Slither")
	window.geometry("700x350+300+300")
	window.grid_columnconfigure(0, weight=1)

	frame = ttk.Frame(window, padding=10)
	frame.grid()

	label = ttk.Label(frame, text="Ay ay! You lose!")
	label.grid(column=0, row=0)
	label2 = ttk.Label(frame, text="Play again?")
	label2.grid(column=0, row=1)

	button_frame = ttk.Frame(frame, padding=10)
	button_frame.grid(column=0, row=2)

	def start_game():
		keep_active.b = True
		window.destroy()

	def exit_game():
		keep_active.b = False
		window.destroy()

	button_continue = ttk.Button(button_frame, text="Play again", command=start_game)
	button_continue.grid(column=0, row=0)
	button_continue = ttk.Button(button_frame, text="Quit", command=exit_game)
	button_continue.grid(column=1, row=0)


	set_active = window.protocol("WM_DELETE_WINDOW", exit_game)
	window.mainloop()

	return keep_active.b
