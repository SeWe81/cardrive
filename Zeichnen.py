import tkinter as tk
import pygame, time
from fontTools.ttLib import getSearchRange


class Zeichnen:

    # Construktor
    def __init__ (self):

        # Grundfenster erstellen
        self.fenster = tk.Tk()
        self.fenster.title("RaceGame")
        self.fenster.geometry("900x900")
        self.fenster.configure(bg="black")



        #erste zeichenfläche
        self.canvas = tk.Canvas(self.fenster, width=900, height=900, bg="#708090")
        self.canvas.pack()

        self.draw_car()

        self.drive_mapping = {
                "gerade": "gerade",
                "links_kurve": "links_kurve",
                "rechts_kurve": "rechts_kurve",
                "gas": "gas",
                "bremsen": "bremsen",
        }

    def draw_car(self):
        # Körper
        self.canvas.create_rectangle(350, 600, 550, 900, fill="#FFD700")
        # Spitze
        self.canvas.create_polygon(350, 600, 550, 600, 450, 500, fill="#FFD700")
        # Fahrerkabine
        self.canvas.create_oval(400, 620, 500, 1000, fill="black" )

    # Linker Reifen (schmaler horizontaler Oval)
        self.canvas.create_oval(330, 620, 350, 700, fill="black")

    # Rechter Reifen
        self.canvas.create_oval(550, 620,  570, 700, fill="black")


    #start funktion
    def start(self):
        self.canvas.create_text(150, 100, text="🚗 Ready to race!", font=("Arial", 16), fill="black" )
        self.fenster.mainloop()



