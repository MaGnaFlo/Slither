from tkinter import *
from tkinter import ttk 


def start_window():

	window = Tk()
	window.title("Slither")

	frame = ttk.Frame(window, padding=10)
	frame.grid()

	label = ttk.Label(frame, text="Welcome to Sliter!")
	label.grid(column=0, row=0)
	label2 = ttk.Label(frame, text="This game is nothing but a Snake. Enjoy!")
	label2.grid(column=0, row=1)
	button = ttk.Button(frame, text="Start game", command=window.destroy)
	button.grid(column=0, row=2)

	window.mainloop()

def collide_window():
	window = Tk()
	window.title("Slither")

	frame = ttk.Frame(window, padding=10)
	frame.grid()

	label = ttk.Label(frame, text="Ay ay! You lose!")
	label.grid(column=0, row=0)
	label2 = ttk.Label(frame, text="Play again?")
	label2.grid(column=0, row=1)
	button = ttk.Button(frame, text="Start game", command=window.destroy)
	button.grid(column=0, row=2)

	window.mainloop()