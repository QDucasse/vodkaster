# -*- coding: utf-8 -*-
# Included in:
# vodkaster
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

import sys

from vodkaster.writer  import *
from vodkaster.scraper import *

if __name__ == "__main__":
    url = sys.argv[1]
    # Scrape
    soup = create_soup(url)
    title = get_title(soup)
    og_title = get_og_title(soup)
    year = get_year(soup)
    director = get_director(soup)
    duration = get_duration(soup)
    genre = get_genre(soup)
    country = get_country(soup)
    # Write
    client = set_env()
    sheet = open_sheet(client)
    add_row(sheet,year,title,director,country,genre,duration)
