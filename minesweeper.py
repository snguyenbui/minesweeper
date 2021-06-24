from tkinter import *
import tkinter as tk

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        canvas = tk.Canvas(self)
        canvas.pack()
        self.rows = 3
        self.columns = 4
        self.startGame = tk.Button(canvas, text="Start", background='white', font=("Helvetica"),
                                   command=lambda: self.generate_grid(self.startGame, canvas))
        self.startGame.place(x=150, y=0)

    def generate_grid(self, event, canvas):
      for r in range(self.rows):
        for c in range(self.columns):
            tk.Label(canvas, text='R%s/C%s'%(r,c), borderwidth=1).grid(row=r,column=c,ipadx=8,ipady=14)
            Cell(canvas, r, c)
            canvas.pack()

class Cell():
  def __init__(self, canvas, r, c):
    super().__init__()
    self.cell = tk.Button(canvas, command=lambda: self.hide_me(self.cell))
    self.cell.grid(row=r,column=c,ipadx=20,ipady=10)
    
  def hide_me(self, event):
    event.grid_forget()

if __name__ == "__main__":
    Game().mainloop()