import MainScript
from tkinter import *

global select
select = False

def delete_all_text():
    MainScript.main_text.delete('1.0', END)

def cut_text(e):
    global select
    select = MainScript.main_text.selection_get()
    if select:
        #Grab selected text
        MainScript.main_text.selection_get()
        #Delete selection
        MainScript.main_text.delete('sel.first', 'sel.last')


def copy_text(e):
    global select
    #Grab selected text
    select = MainScript.main_text.selection_get()

def paste_text(e):
    #Checking if anything was copied/cut in the first place
    if select:
        #Getting the position of the cursor
        position = MainScript.main_text.index(INSERT)
        #Pasting the selection that was recently copied/cut
        MainScript.main_text.insert(position , select)