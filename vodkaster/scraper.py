# -*- coding: utf-8 -*-
# Included in:
# vodkaster
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

import requests
from bs4 import BeautifulSoup

from vodkaster.writer  import *
from vodkaster.scraper import *

# Get the url content
def create_soup(url):
    # Set headers
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    req = requests.get(url, headers)
    return BeautifulSoup(req.content, 'html.parser')

# Title
def get_title(soup):
    '''Scape the page for the title, if not found return an empty string'''
    title = soup.find("h1").get_text()
    if title is None:
        title = ""
    return title

# Original Title
def get_og_title(soup):
    '''Scrape the page for the original title, if not found return the title'''
    og_title = soup.find("div", class_="details").get_text().split('Titre original :')[1].split('\n')[0].strip()
    if og_title is None:
        return get_title(soup)
    else:
        return og_title

# Year
def get_year(soup):
    '''Scape the page for the year, if not found return an empty string'''
    year = soup.find("span", class_="year").get_text().strip()[1:-1]
    if year is None:
        year = ""
    return year

# Director
def get_director(soup):
    '''Scape the page for the director, if not found return an empty string'''
    director = soup.find("div", class_="details").find("a").get_text()
    if director is None:
        director = ""
        return director
    # No first name e.g. Costa-Gravas
    elif len(director.split(" ", 1)) == 1:
        return director
    else:
        components = director.split(" ", 1)
        # Places family name then first name
        return components[1] + " " + components[0]

# Duration
def get_duration(soup):
    '''Scape the page for the duration, if not found return an empty string'''
    duration_format = soup.find("meta", itemprop="duration").get("content")[2:].split('M')[0] # Outputs PT2H2M40S for 2h02m40s
    if duration_format is None:
        duration_format = ""
        return duration_format
    else:
        if 'H' in duration_format:
            components      = duration_format.split('H')
            hours           = components[0]
            minutes         = components[1] if len(components[1]) == 2 else '0' + components[1]
        else:
            hours = '0'
            minutes = duration_format
        return hours + 'h' + minutes

# Film Genre
def get_genre(soup):
    '''Scape the page for the genre, if not found return an empty string'''
    genre = soup.find("span", itemprop="genre").get_text()
    if genre is None:
        genre = ""
    return genre

# Country
def get_country(soup):
    '''Scape the page for the director, if not found return an empty string'''
    country = soup.find("div", class_="details").get_text().split('- ')[0].split('\n')[5].strip()
    if country is None:
        country = ""
    return country

if __name__ == "__main__":
    # soup = create_soup("https://www.vodkaster.com/films/seven/63655")
    # print(get_genre(soup))

    str = "Costa-Gravas"
    print(str.split(" ",1))
