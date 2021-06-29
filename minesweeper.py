import tkinter as tk
from tkinter import *
import random

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        menu = tk.Canvas(self, height=30)
        game_area = tk.Canvas(self)
        menu.pack(side=TOP)
        game_area.pack()
        self.rows = 10
        self.columns = 10
        self.list = []
        self.startGame = tk.Button(menu, text="Start", background='white', font=("Helvetica"),
                                   command=lambda: self.generate_grid(self.startGame, game_area))
        self.startGame.place(x=150, y=0)

    def generate_grid(self, event, canvas):
      for r in range(self.rows):
        row = []
        for c in range(self.columns):
          if random.random() < 0.5:
            row.append([False,0])
            # tk.Label(canvas, text='R%s/C%s'%(r,c), borderwidth=1).grid(row=r, column=c, ipadx=8, ipady=14)
          else: 
            row.append([True,0])
            # tk.Label(canvas, text='X', borderwidth=1).grid(row=r, column=c, ipadx=20, ipady=14)
          # Cell(canvas, r, c)
          # canvas.pack()
        self.list.append(row)
      self.count_bombs(self)

    def count_bombs(self, event):
      for r in range(self.rows):
        for c in range(self.columns):
          if self.list[r][c][0] == True:
            self.list[r][c][1] += 1
            print(self.list[r][c])
      print(self.list)

class Cell():
  def __init__(self, canvas, r, c):
    super().__init__()
    self.cell = tk.Button(canvas, command=lambda: self.hide_me(self.cell))
    self.cell.grid(row=r,column=c,ipadx=20,ipady=10)
    
  def hide_me(self, event):
    event.grid_forget()

if __name__ == "__main__":
    Game().mainloop()