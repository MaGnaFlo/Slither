from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *

class Bool:
	''' Boolean container just to hold a bool value
		to be passed "as a reference" to functions.
		I know, I know.. it's a lame hack, but it works.
	'''
	def __init__(self, value):
		self.value = value


def center_window(win, size="400x150"):
	"""
    centers a tkinter window
    """
	win.geometry(size)
	win.update_idletasks()

	width = win.winfo_width()
	frm_width = win.winfo_rootx() - win.winfo_x()
	win_width = width + 2 * frm_width

	height = win.winfo_height()
	titlebar_height = win.winfo_rooty() - win.winfo_y()
	win_height = height + titlebar_height + frm_width

	x = win.winfo_screenwidth() // 2 - win_width // 2
	y = win.winfo_screenheight() // 2 - win_height // 2
	win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

	win.deiconify()


def start_window():
	''' Display the start window when the game is launched
		Returns whether or not the player wants to play
		to activate the game.
	'''
	set_active = Bool(True)

	window = Tk()
	window.title("Slither")
	window.grid_columnconfigure(0, weight=1) # allow sub widgets to reize accordindly.
	window.resizable(0,0)
	center_window(window)

	frame = ttk.Frame(window, padding=10)
	frame.grid()

	label = ttk.Label(frame, text="Welcome to Slither!")
	label.grid(column=0, row=0)
	label2 = ttk.Label(frame, text="This game is nothing but a Snake. Enjoy!")
	label2.grid(column=0, row=1)

	def start_game():
		set_active.value = True
		window.destroy()

	button = ttk.Button(frame, text="Play!", command=start_game)
	button.grid(column=0, row=5)
	button.config(width="10")

	def exit_game():
		set_active.value = False
		window.destroy()

	window.protocol("WM_DELETE_WINDOW", exit_game)
	window.mainloop()

	return set_active.value

def collide_window(score: int):
	''' Display the start window when a collision happens.
		Returns whether or not the player wants to keep playing.
	'''
	keep_active = Bool(True)

	window = Tk()
	window.title("Slither")
	window.grid_columnconfigure(0, weight=1)

	center_window(window)

	frame = ttk.Frame(window, padding=10)
	frame.grid()

	label = ttk.Label(frame, text="Woops, you lose!")
	label.grid(column=0, row=0)
	label_score = ttk.Label(frame, text=f"Score: {score}")
	label_score.grid(column=0, row=1)
	label_play_again = ttk.Label(frame, text="Play again?")
	label_play_again.grid(column=0, row=2)

	button_frame = ttk.Frame(frame, padding=10)
	button_frame.grid(column=0, row=2)

	def start_game():
		keep_active.value = True
		window.destroy()

	def exit_game():
		keep_active.value = False
		window.destroy()

	button_continue = ttk.Button(button_frame, text="Play again", command=start_game)
	button_continue.grid(column=0, row=0)
	button_continue = ttk.Button(button_frame, text="Quit", command=exit_game)
	button_continue.grid(column=1, row=0)

	set_active = window.protocol("WM_DELETE_WINDOW", exit_game)
	window.mainloop()

	return keep_active.value
