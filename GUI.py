#do dokończenia

import pygame
from tkinter import *

win = Tk()
pygame.init()

win.title('communicator')

global operator
txt_input = ''

Display = Entry(win, font=('arial', 30), justify='right', textvariable=txt_input)
Display.grid(columnspan=4)

win.mainloop()
