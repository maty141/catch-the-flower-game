import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import random

okno = tk.Tk()
okno.title("Chyť kytku!")

chnapani = tk.Canvas(okno, height=1000, width=5000, bg="Light Green")
chnapani.pack()
okno.focus_set()

kytka = chnapani.create_oval(650, 350, 750, 450, outline="black", fill="yellow")

barvy = ["yellow", "blue", "red", "green", "purple", "orange", "pink"]

def priprava(event=None):
    a=sd.askstring('Jména hráčů', 'Jméno (přezdívka) 1. hráče')
    b=sd.askstring('Jména hráčů', 'Jméno (přezdívka) 2. hráče')

priprava()

def chytnout(event=None):
    global kytka
    chnapani.delete(kytka)
    okno.after(1000, restart_kytka)

def restart_kytka():
    global kytka
    nahodna_barva = random.choice(barvy)
    kytka = chnapani.create_oval(650, 350, 750, 450, outline="black", fill=nahodna_barva)

chnapani.bind("<KeyPress-space>", chytnout)
chnapani.focus_set()

okno.mainloop()
