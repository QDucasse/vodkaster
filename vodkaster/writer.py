# -*- coding: utf-8 -*-
# Included in:
# vodkaster
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
def set_env():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    return gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
def open_sheet(client):
    return client.open("Films/séries").sheet1

def already_in(sheet,title):
    res=False
    rows = sheet.get_all_values()
    for row in rows:
        res = (row[1] == title)
    return(res)

def add_row(sheet,year,title,director,country,genre,duration):
    if not(already_in(sheet,title)):
        row = [year,title,director,country,genre,duration]
        new_line = len(sheet.get_all_values()) + 1
        sheet.insert_row(row,new_line)
        return True
    else:
        return False
