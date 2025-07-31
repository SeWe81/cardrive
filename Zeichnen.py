import tkinter as tk
import pygame, time
from fontTools.ttLib import getSearchRange


class Zeichnen:

# Construktor
    def __init__ (self):
        self.fenster = tk.Tk()
        self.fenster.title("RaceGame")
        self.fenster.geometry("900x600")
        self.fenster.configure(bg="black")


        self.canvas = tk.Canvas(self.fenster, width=900, height=600, bg="#708090")
        self.canvas.pack()

        self.drive_mapping = {

                "gerade": "gerade",
                "links_kurve": "links_kurve",
                "rechts_kurve": "rechts_kurve",
                "gas": "gas",
                "bremsen": "bremsen",
        }


    def start(self):
        self.canvas.create_text(150, 100, text="🚗 Ready to race!", font=("Arial", 16), fill="black")
        self.fenster.mainloop()



