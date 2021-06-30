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
      self.startGame = tk.Button(menu, text="Start", background='white', font=("Helvetica"), command=lambda: self.generate_grid(self.startGame, game_area))
      self.startGame.place(x=150, y=0)

  def generate_grid(self, event, canvas):
    self.list = []
    for r in range(self.rows):
      row = []
      for c in range(self.columns):
        if random.random() < 0.9:
          row.append([False,0])
        else: 
          row.append([True,0])
      self.list.append(row)
    self.count_bombs(self)
    self.set_numbers(self, canvas)

  def count_bombs(self, event):
    for r in range(self.rows):
      for c in range(self.columns):
        if self.list[r][c][0] == True:
          # middle 
          if 0 < r < self.rows - 1 and 0 < c < self.columns - 1:
            self.list[r-1][c-1][1] += 1
            self.list[r-1][c][1] += 1
            self.list[r-1][c+1][1] += 1
            self.list[r][c-1][1] += 1
            self.list[r][c+1][1] += 1
            self.list[r+1][c-1][1] += 1
            self.list[r+1][c][1] += 1
            self.list[r+1][c+1][1] += 1
          # top left corner
          if r == 0 and c == 0:
            self.list[r][c+1][1] += 1
            self.list[r+1][c][1] += 1
            self.list[r+1][c+1][1] += 1
          # top right corner
          if r == 0 and c == self.columns - 1:
            self.list[r][c-1][1] += 1
            self.list[r+1][c-1][1] += 1
            self.list[r+1][c][1] += 1
          # top row
          if r == 0 and 0 < c < self.columns - 1:
            self.list[r][c-1][1] += 1
            self.list[r][c+1][1] += 1
            self.list[r+1][c-1][1] += 1
            self.list[r+1][c][1] += 1
            self.list[r+1][c+1][1] += 1
          # bottom left corner
          if r == self.rows - 1 and c == 0 :
              self.list[r][c+1][1] += 1
              self.list[r-1][c][1] += 1
              self.list[r-1][c+1][1] += 1
          # bottom right corner
          if r == self.rows - 1 and c == self.columns - 1:
            self.list[r][c-1][1] += 1
            self.list[r-1][c-1][1] += 1
            self.list[r-1][c][1] += 1
          # bottom row
          if r == self.rows - 1 and 0 < c < self.columns - 1:
            self.list[r][c-1][1] += 1
            self.list[r][c+1][1] += 1
            self.list[r-1][c-1][1] += 1
            self.list[r-1][c][1] += 1
            self.list[r-1][c+1][1] += 1
          # left column
          if c == 0 and 0 < r < self.rows - 1:
            self.list[r-1][c][1] += 1
            self.list[r-1][c+1][1] += 1
            self.list[r][c+1][1] += 1
            self.list[r+1][c][1] += 1
            self.list[r+1][c+1][1] += 1
          # right column
          if c == self.columns - 1 and 0 < r < self.rows - 1:
            self.list[r-1][c-1][1] += 1
            self.list[r-1][c][1] += 1
            self.list[r][c-1][1] += 1
            self.list[r+1][c-1][1] += 1
            self.list[r+1][c][1] += 1

  def set_numbers(self, event, canvas):
    for r in range(self.rows):
      for c in range(self.columns):
        if self.list[r][c][0] == False:
          if self.list[r][c][1] != 0:
            tk.Label(canvas, text=self.list[r][c][1], padx=7, pady=4).grid(row=r, column=c)
          if self.list[r][c][1] == 0:
            tk.Label(canvas, padx=7, pady=4).grid(row=r, column=c)
        if self.list[r][c][0] == True:
          tk.Label(canvas, text="X", padx=7, pady=4).grid(row=r, column=c)
        Cell(canvas, r, c)
        canvas.pack()


class Cell():
  def __init__(self, canvas, r, c):
    super().__init__()
    self.cell = tk.Button(canvas, command=lambda: self.hide_me(self.cell), width=2)
    self.cell.grid(row=r,column=c)
    
  def hide_me(self, event):
    event.grid_forget()

if __name__ == "__main__":
    Game().mainloop()