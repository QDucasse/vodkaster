# -*- coding: utf-8 -*-
# Included in:
# vodkaster
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

import tkinter as tk
from tkinter import *
from vodkaster.writer  import *
from vodkaster.scraper import *


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Vodkaster Scraper")

        self.label_url = tk.Label(self.window, text="URL").grid(row=0)

        self.entry_url = tk.Entry(self.window)
        self.entry_url.grid(row=0, column=1)

        self.label_result = tk.Label(self.window, text="Résultat").grid(row=2)

        self.entry_result = tk.Entry(self.window)
        self.entry_result.grid(row=2, column=1)

        self.button = tk.Button(self.window, text="ZEBI", command=self.process_url)
        self.button.grid(row=1, column=1)

        self.window.mainloop()

    def process_url(self):
        url = self.entry_url.get()
        # Scrape
        soup = create_soup(url)
        title = get_title(soup)
        # og_title = get_og_title(soup)
        year = get_year(soup)
        director = get_director(soup)
        duration = get_duration(soup)
        genre = get_genre(soup)
        country = get_country(soup)
        # Write
        client = set_env()
        sheet = open_sheet(client)
        res = add_row(sheet,year,title,director,country,genre,duration)
        if res:
            self.entry_result.delete(0,END)
            self.entry_result.insert(0,"Film ajouté!")
        else:
            self.entry_result.delete(0,END)
            self.entry_result.insert(0,"Film déjà dans la liste!")

if __name__ == "__main__":
    gui = GUI()
