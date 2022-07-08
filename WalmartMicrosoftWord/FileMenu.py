import MainScript
from tkinter import *
from tkinter import END
from tkinter import filedialog
#import win32api

global title_status
title_status=False

def new_file():
    MainScript.main_text.delete("1.0", END)
    MainScript.Ui.title("New File - Unnamed")
    MainScript.status_label.configure(text="New File Created!")

    global title_status
    title_status=False
    replace_stat = False


def open_file():
    #Replace title
    text_file = filedialog.askopenfilename(initialdir='C:/This PC', title = "Open File", filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
    if text_file:
        global title_status
        title_status = text_file
    count = 0
    string = ''
    num = 0
    stall = 0
    for x in range(0, len(text_file)):
        if(text_file[x] == '/'):
            count += 1
    for x in range(0, len(text_file)):
        if(text_file[x] == '/'):
            num += 1
        if num == count:
            stall += 1
        if stall >=2:
            string += text_file[x]
    MainScript.Ui.title(string)
    #Open File
    text_file = open(text_file, 'r')
    read = text_file.read()
    #Replace previous file contents
    MainScript.main_text.delete("1.0", END)
    #add file to text box
    MainScript.main_text.insert(END, read)
    MainScript.status_label.configure(text="  File Opened!  ")

def save_file():
    #Save
    global title_status
    if title_status:
        text_file = open(title_status, 'w')
        text_file.write(MainScript.main_text.get('1.0', END))
        MainScript.status_label.configure(text="  File Saved!  ")
        text_file.close()
    else:
        save_as_file()
# WHOEVER USES THIS IS A RETARD
#FUCKKKKKKKK
def save_as_file():
    #Save
    global save_update
    global title_status
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/This PC/", title = "Save File,", filetypes = (("Text File", "*.txt"), ("Word File", "*.docx"), ("PDF", "*.pdf")))
    file = open(text_file, "w")
    file.write(MainScript.main_text.get('1.0', END))
    title_status = True
    count = 0
    string = ''
    num = 0
    stall = 0
    for x in range(0, len(text_file)):
        if(text_file[x] == '/'):
            count += 1
    for x in range(0, len(text_file)):
        if(text_file[x] == '/'):
            num += 1
        if num == count:
            stall += 1
        if stall >= 2:
            string += text_file[x]
    MainScript.Ui.title(string)
    #Update Status:
    MainScript.status_label.configure(text="  File Saved!  ")
    save_update

'''def print():
    # Ask for file (Which you want to print)
    file_to_print = filedialog.askopenfilename(
      initialdir="C:/This PC", title="Select file", 
      filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
      
    if file_to_print:
        
        # Print Hard Copy of File
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)'''