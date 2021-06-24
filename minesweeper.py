from tkinter import *
import tkinter as tk

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        canvas = tk.Canvas(self)
        canvas.pack()
        self.startGame = tk.Button(canvas, text="Start", background='white', font=("Helvetica"),
                                   command=lambda: self.generate_grid(self.startGame, canvas))
        self.startGame.place(x=150, y=0)

    def hide_me(self, event):
        print('hide me')
        event.grid_forget()

    def generate_grid(self, event, canvas):
      for r in range(3):
        for c in range(4):
          cell = tk.Button(canvas, command=lambda: self.hide_me(cell)).grid(row=r,column=c)
          canvas.pack()

if __name__ == "__main__":
    Game().mainloop()