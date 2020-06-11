# -*- coding: utf-8 -*-
# Included in:
# vodkaster
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

import tkinter as tk
from vodkaster.writer  import *
from vodkaster.scraper import *

window = tk.Tk()
window.title("Vodkaster Scraper")

tk.Label(window, text="URL").grid(row=0)

entry = tk.Entry(window)
entry.grid(row=0, column=1)


def process_url():
    url = entry.get()
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
    add_row(sheet,year,title,director,country,genre,duration)

button = tk.Button(window, text="ZEBI", command=process_url)
button.grid(row=1, column=1)

window.mainloop()
