
from tkinter import *


root = Tk()
btn = [""]*9
position = [0]*9

def mov(mo, position, btn, mem):
    temp = 0
    if mo == 1:
        if position[0] != 6 and position[0] != 7 and position[0] != 8:
            temp = position[0]
            for i in range(9):
                if position[i] == position[0]+3:
                    position[0] = position[i]
                    position[i] = temp
                    break
    if mo == 2:
        if position[0] != 0 and position[0] != 1 and position[0] != 2:
            temp = position[0]
            for i in range(9):
                if position[i] == position[0]-3:
                    position[0] = position[i]
                    position[i] = temp
                    break
    if mo == 3:
        if position[0] != 2 and position[0] != 5 and position[0] != 8:
            temp = position[0]
            for i in range(9):
                if position[i] == position[0]+1:
                    position[0] = position[i]
                    position[i] = temp
                    break
    if mo == 4:
        if position[0] != 0 and position[0] != 3 and position[0] != 6:
            temp = position[0]
            for i in range(9):
                if position[i] == position[0]-1:
                    position[0] = position[i]
                    position[i] = temp
                    break
    for i in range(9):
        btn[position[i]].config(text = mem[i])
mem = [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
for i in range(9):
    btn[i] = Button(root, text = mem[i], relief = "ridge", height = 3, width = 5)
    btn[i].grid(row = i//3, column = i%3)
    position[i] = i #i代表 " ", 1, 2, ... ,8 在i
btnup = Button(root, text = "↑", relief = "raised", command = lambda:mov(1, position, btn, mem)).grid(row = 3, column = 1)
btndo = Button(root, text = "↓", relief = "raised", command = lambda:mov(2, position, btn, mem)).grid(row = 5, column = 1)
btnle = Button(root, text = "←", relief = "raised", command = lambda:mov(3, position, btn, mem)).grid(row = 4, column = 0)
btnri = Button(root, text = "→", relief = "raised", command = lambda:mov(4, position, btn, mem)).grid(row = 4, column = 2)

root.mainloop()

