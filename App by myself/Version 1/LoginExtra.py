import tkinter as tk
from tkinter.ttk import *
from openpyxl import *
import Register as Re
import Login as Lo

def Open_Register():
    Re.excel()
    Re.toplevel(loginGUI)

def Open_Login():
    Lo.toplevel(loginGUI)
    


loginGUI = tk.Tk()
loginGUI.title("Login and register")
loginGUI.geometry("500x300+550+250")
loginGUI.resizable(0,0)

# define image of background
bg = tk.PhotoImage(file= "Images\Background.png")
bg = bg.subsample(2,2)

# define image of button
# login
login_im = tk.PhotoImage(file= "Images\Log in.png")
login_im = login_im.subsample(2,2)
# register
register_im = tk.PhotoImage(file= "Images\Register.png")
register_im = register_im.subsample(2,2)
# help
help_im = tk.PhotoImage(file= "Images\Help.png")
help_im = help_im.subsample(2,2)
# escape
escape_im = tk.PhotoImage(file= "Images\Quit.png")
escape_im = escape_im.subsample(2,2)

# set canvas for login_area 
canv = tk.Canvas(loginGUI, height= 300, width= 500)
canv.pack(fill= 'both', expand= True)

# set background
canv.create_image(0, 0, image= bg, anchor= 'nw')

#create button
login = tk.Button(loginGUI, image= login_im, command= lambda: Open_Login())
register =tk.Button(loginGUI, image= register_im, command= lambda: Open_Register())
help = tk.Button(loginGUI, image= help_im)
quit = tk.Button(loginGUI, image= escape_im, command= loginGUI.destroy)
# set button on GUI
login_window = canv.create_window(160, 150, anchor= 'nw', window= login)
register_window = canv.create_window(255, 150, anchor= 'nw', window= register)
help_window = canv.create_window(205, 200, anchor= 'nw', window= help)
quit_window = canv.create_window(430, 10, anchor= 'nw', window= quit)
# set label on GUI
Welcome_text = canv.create_text(255, 70, text= 'Welcome to AByMS', font= ("Time New Roman", 25), fill= 'white')


login.mainloop()




