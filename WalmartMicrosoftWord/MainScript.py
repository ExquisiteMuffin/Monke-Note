from tkinter import *
from tkinter import font
import EditMenu
from FileMenu import *

#Main UI
Ui = Tk()
#Ui.iconbitmap("C:\\Users\cjmch\OneDrive\Desktop\Code\Python\Projects\WalmartMicrosoftWord\Icon.png")
Ui.iconphoto(True, PhotoImage(file="Images/Icon.png"))
Ui.title("MonkeNote")
Ui.geometry("1300x900")

#Background
bg = PhotoImage(file="Images/bg_dark.png")
bg_label = Label(Ui, image=bg)
bg_label.place(x=0, y=0, relwidth = 1)

#Create Frame
main_frame = Frame(Ui, height = 1000, width = 850)
main_frame.pack(pady = 10)
main_frame.pack_propagate(False)

#Create Text Scrollbar 
y_scroll = Scrollbar(main_frame, bg="#878686")
y_scroll.pack(fill = Y, side = RIGHT)

#Side Bar
sidebar_base = Label(Ui, bg = "#2e2e2e", height = 18, width = 25)
sidebar_base.place(x=0, y=2)

#Fonts/text configurations 
current_fontsize = 11
curr_font = font.Font()
times = font.Font(family ='Times New Roman')
default_font = font.Font(family = 'Calibri')
norm = font.Font(slant = 'roman', underline = 0, weight = 'normal')
italics = font.Font(slant = "italic")
under = font.Font(underline = 1)
bold = font.Font(weight = "bold")

#Main Text
main_text = Text(main_frame, wrap = WORD, 
height = 70, width = 90, padx = 120, pady = 40, bd = 0, 
font = default_font, fg ='#ffffff', yscrollcommand = y_scroll.set, 
bg = "#1f1e1e", undo = True, selectforeground = "black", 
selectbackground = "#4a4949")
main_text.pack_propagate(False)
main_text.pack()

#Config Scroll Bar
y_scroll.config(command = main_text.yview)

#Side Bar Font Size Buttons
add_button = Button(sidebar_base, text = "+", padx = 1, pady = 0, 
bd = 0, bg = "#878787", command = lambda: add_fontsize(True))
sub_button = Button(sidebar_base, text = "--", padx = 1, pady = 0, 
bd = 0, bg = "#878787", command = lambda: sub_fontsize(True))
add_button.place(x = 103 ,y = 38)
sub_button.place(x = 46, y = 39)

#Font Size Display
font_disp = Label(sidebar_base, text = '11', width = 5, height = 1)
font_disp.place(x = 62, y = 38)

#Side Bar Methods
def times_select(pressed):
    global curr_font
    if pressed == True:
        curr_font = times
        curr_font.config(size=current_fontsize)
        main_text.configure(font = curr_font, padx = 120, pady = 42)

def default_select(pressed):
    global curr_font
    if pressed == True:
        curr_font = default_font
        curr_font.config(size=current_fontsize)
        main_text.configure(font = curr_font, padx = 120, pady = 42)
def add_fontsize(pressed):
    global default_font
    global curr_font
    global current_fontsize
    if pressed == True:
        current_fontsize += 1
        curr_str = str(current_fontsize)
        font_disp.config(text = curr_str)
        curr_font.config(size = current_fontsize)
        main_text.configure(font = curr_font)
def sub_fontsize(pressed):
    global default_font
    global curr_font
    global current_fontsize
    if pressed == True:
        if current_fontsize > 11:
            current_fontsize -= 1
            curr_str = str(current_fontsize)
            font_disp.config(text = curr_str)
            curr_font.config(size = current_fontsize)
            main_text.configure(font = curr_font)
        else:
            print("debug")
            # <<< alert message >>>
            
def make_bold():
    global curr_font
    main_text.selection_get()
    curr_font.config(weight = "bold")
            
#Side Bar Options
times_button = Button(sidebar_base, font = ("Times New Roman", 11), 
text="Times New Roman", borderwidth=0, command = lambda: times_select(True))
default_button = Button(sidebar_base, font = ("Calibri", 11), 
text = "Calibri", borderwidth=0, command = lambda: default_select(True))
times_button.place(x = 30, y = 100)
default_button.place(y = 135, x = 30)
bold_button = Button(sidebar_base, font = bold, text = "Bold", command = lambda: make_bold())

#Theme Button Vars
ocean_b = PhotoImage(file = "Images/ocean_button.png")
ocean_bg = PhotoImage(file = 'Images/ocean_bg.png')
coffee_b = PhotoImage(file = "Images/coffee_button.png")
coffee_bg = PhotoImage(file = 'Images/coffee_bg.png')
sup_b = PhotoImage(file='Images/superman_button.png')
sup_bg = PhotoImage(file = "Images/superman_bg.png")

#Theme Cycle
cycle = 0

#Themes
def theme_setting():
    global cycle
    if cycle == 3:
        cycle = 0
    if cycle == 2:
        main_text.configure(bg = '#000000', fg = '#FFD700', insertbackground='#FFD700')
        theme_button.config(image = sup_b)
        bg_label.config(image = sup_bg)
        cycle +=1
    if cycle == 1:
        main_text.configure(bg = '#4a2115', fg = '#996150', insertbackground='#996150')
        theme_button.config(image = coffee_b)
        bg_label.config(image = coffee_bg)
        cycle += 1
    if cycle == 0:
        main_text.configure(bg = '#0a77fc', fg = '#59bdff', insertbackground='#59bdff')
        bg_label.config(image = ocean_bg)
        theme_button.config(image = ocean_b)
        cycle = cycle + 1

#Placeholder button(to be update later)
theme_bg = PhotoImage(file='Images/ThemeSetting_placeholder.png')
theme_button = Button(sidebar_base, image = theme_bg, bd = 0, command = theme_setting)
theme_button.place(x = 103, y = 200)

#Background light/dark modes
light_mode = PhotoImage(file="Images/bg_light.png")
dark_mode = PhotoImage(file="Images/bg_dark.png")
dark_tog = PhotoImage(file = 'Images/dark_mode.png')
light_tog = PhotoImage(file = 'Images/light_mode.png')

#Toggle var
toggle = True

#Toggle Dark/Light
def toggle_mode():
    global light_mode
    global bg_label
    global toggle
    global main_text
    if toggle:
        bg_label.configure(image = light_mode)
        toggle_button.config(image = light_tog)
        main_text.configure(bg = '#ffffff', fg = '#000000', insertbackground="#000000")
        toggle = False
    else:
        bg_label.configure(image = dark_mode)
        toggle_button.config(image = dark_tog)
        main_text.configure(bg = '#1f1e1e', fg = '#ffffff', insertbackground='#ffffff')
        toggle = True

#Toggle Buttons
button_bg = PhotoImage(file='Images/dark_mode.png')
toggle_button = Button(sidebar_base, image=button_bg, bd = 0, command = toggle_mode)
toggle_button.place(x = 4, y = 200)

#Create menu
menu = Menu(Ui)
Ui.config(menu = menu)

#Add File Menu
file_menu = Menu(menu, activebackground = "#ff6529", tearoff = 0)
menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label ="New File", command = lambda: new_file())
file_menu.add_command(label ="Open File", command = lambda: open_file())
file_menu.add_command(label ="Save", command = lambda: save_file())
file_menu.add_command(label ="Save as", command = lambda: save_as_file())
#file_menu.add_separator()
#file_menu.add_command(label='Print', command = lambda: print())
file_menu.add_separator()
file_menu.add_command(label ="Exit", command = Ui.destroy)

#Edit Menu
edit_menu = Menu(menu, activebackground="#ff6529", tearoff=0)
menu.add_cascade(label="Edit", menu = edit_menu)
edit_menu.add_command(label="Undo", command = lambda: main_text.edit_undo())
edit_menu.add_command(label="Redo", command = lambda: main_text.edit_redo())
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command = lambda: EditMenu.copy_text(1))
edit_menu.add_command(label="Cut", command = lambda: EditMenu.cut_text(1))
edit_menu.add_command(label="Paste", command = lambda: EditMenu.paste_text(1))
edit_menu.add_separator()
edit_menu.add_command(label="Delete All Text", command = lambda: EditMenu.delete_all_text())

#Style Menu
'''style_menu = Menu(menu, activebackground="#ff6529", tearoff=0)
menu.add_cascade(label="Style", menu=style_menu)
style_menu.add_command(label="Font")
style_menu.add_command(label="Font Size")
style_menu.add_separator()
style_menu.add_command(label="Bold")
style_menu.add_command(label="Italics")
style_menu.add_command(label="Underline")'''

#Add Page
'''add_menu = Menu(menu, activebackground="#ff6529", tearoff=0)
menu.add_cascade(label="Add", menu = add_menu)
add_menu.add_command(label="Add Image")'''

#Create Status Label
status_label=Label(Ui, text='File Not Saved', fg = "grey")
status_label.place(y=2, x=46)

#Looping the UI
Ui.mainloop()
try:
    Ui.destroy()
except TclError:
    pass
