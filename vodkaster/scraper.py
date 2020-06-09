# -*- coding: utf-8 -*-
# Included in:
# vodkaster
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

import requests
from bs4 import BeautifulSoup

# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# Get the url content
def create_soup(url):
    req = requests.get(url, headers)
    return BeautifulSoup(req.content, 'html.parser')

# Title
def get_title(soup):
    return soup.find("h1").get_text()

# Original Title
def get_og_title(soup):
    og_title = soup.find("div", class_="details").get_text().split('Titre original :')[1].split('\n')[0].strip()
    if og_title is None:
        return get_title(soup)
    else:
        return og_title

# Year
def get_year(soup):
    return soup.find("span", class_="year").get_text().strip()[1:-1]

# Director
def get_director(soup):
    director = soup.find("div", class_="details").find("a").get_text()
    components = director.split(" ")
    return components[1] + " " + components[0]

# Duration
def get_duration(soup):
    duration_format = soup.find("meta", itemprop="duration").get("content")[2:].split('M')[0] # Outputs PT2H2M40S for 2h02m40s
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
    return soup.find("span", itemprop="genre").get_text()

# Country
def get_country(soup):
    return soup.find("div", class_="details").get_text().split('- ')[0].split('\n')[5].strip()

if __name__ == "__main__":
    soup = create_soup("https://www.vodkaster.com/films/seven/63655")
    print(get_genre(soup))
