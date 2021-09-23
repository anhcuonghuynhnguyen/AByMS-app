from tkinter import *
from PIL import ImageTk
from tkinter.ttk import Style, Checkbutton
from tkinter import messagebox

def Todolist():
    global count, entr, lst
    TodoGUI = Tk()
    TodoGUI.title("TodoList app")
    TodoGUI.geometry("500x700")
    TodoGUI.resizable(0,0)

    #set style for checkbutton
    style = Style()
    style.configure("TCheckbutton" , font = ('Time New Roman',12,'bold'), background= "#2d3134", foreground= "white")
    style.map("TCheckbutton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'light yellow'), ('active', 'light green')])

    lst = ['',"","","","","",""]
    count = 0
    """--------------------------------------------------------------------------------------------------------------------------------------------------"""
    # define fuction add button
    def addbutton():
        global count
        a = entr.get()
        if count <=  6:
            lst[count] = a
            count += 1
        elif count == 7:
            messagebox.showerror("ERROR", "Vượt quá công việc cho phép")
        for i in range(7):
            if i == 0:
                Task1.configure(text= "1. " + lst[0])
            elif i == 1:
                Task2.configure(text= "2. " + lst[1])
            elif i == 2:
                Task3.configure(text= "3. " + lst[2])
            elif i == 3:
                Task4.configure(text= "4. " + lst[3])
            elif i == 4:
                Task5.configure(text= "5. " + lst[4])
            elif i == 5:
                Task6.configure(text= "6. " + lst[5])
            elif i == 6:
                Task7.configure(text= "7. " + lst[6])
        entr.delete(0, END)

   
    # set fuction done button
    def donebutton():
        global count
        if count >=1 :
            if task1.get():
                task1.set(False)
                if lst[0] != "":
                    tex.insert("end", lst[0]+"\n")
                    lst.pop(0)
                    lst.append("")  
                    count -= 1
            elif task2.get():
                task2.set(False)
                if lst[1] != "":
                    tex.insert("end", lst[1]+"\n")
                    lst.pop(1)
                    lst.append("")
                    count -= 1
            elif task3.get():
                task3.set(False)
                if lst[2] != "":
                    tex.insert("end", lst[2]+"\n")
                    lst.pop(2)
                    lst.append("")
                    count -= 1
            elif task4.get():
                task4.set(False)
                if lst[3] != "":
                    tex.insert("end", lst[3]+"\n")
                    lst.pop(3)
                    lst.append("")
                    count -= 1
            elif task5.get():
                task5.set(False)
                if lst[4] != "":
                    tex.insert("end", lst[4]+"\n")
                    lst.pop(4)
                    lst.append("")
                    count -= 1
            elif task6.get():
                task6.set(False)
                if lst[5] != "":
                    tex.insert("end", lst[5]+"\n")
                    lst.pop(5)
                    lst.append("")
                    count -= 1
            elif task7.get():
                task7.set(False)
                if lst[6] != "":
                    tex.insert("end", lst[6]+"\n")
                    lst.pop(6)
                    lst.append("")
                    count -= 1
        for i in range(7):
            if i == 0:
                Task1.configure(text= "1. " + lst[0])
            elif i == 1:
                Task2.configure(text= "2. " + lst[1])
            elif i == 2:
                Task3.configure(text= "3. " + lst[2])
            elif i == 3:
                Task4.configure(text= "4. " + lst[3])
            elif i == 4:
                Task5.configure(text= "5. " + lst[4])
            elif i == 5:
                Task6.configure(text= "6. " + lst[5])
            elif i == 6:
                Task7.configure(text= "7. " + lst[6])
    

    # set fuction delete button
    def deletebutton():
        global count,lst
        count = 0
        lst= ["","","","","","",""]
        for i in range(7):
            if i == 0:
                Task1.configure(text= "1. " + lst[0])
            elif i == 1:
                Task2.configure(text= "2. " + lst[1])
            elif i == 2:
                Task3.configure(text= "3. " + lst[2])
            elif i == 3:
                Task4.configure(text= "4. " + lst[3])
            elif i == 4:
                Task5.configure(text= "5. " + lst[4])
            elif i == 5:
                Task6.configure(text= "6. " + lst[5])
            elif i == 6:
                Task7.configure(text= "7. " + lst[6])

        
        

    """--------------------------------------------------------------------------------------------------------------------------------------------------"""

    
    #set bachground
    img =ImageTk.PhotoImage(file="Images\Todo.jpg")
    Label(TodoGUI, image= img, highlightthickness=0, borderwidth= 0).place(x= 0, y= 0)

    # add button
    add = PhotoImage(file= "Images\Add button.PNG")
    add= add.subsample(5,5)

    done = PhotoImage(file= "Images\Done button.PNG")
    done = done.zoom(2,2)
    done = done.subsample(3,3)

    delete = PhotoImage(file= "Images\Delete button.PNG")
    delete = delete.zoom(2,2)
    delete = delete.subsample(3,3)

    save = PhotoImage(file="Images\Save button.PNG")
    save = save.subsample(3,3)

    # set frame 
    frame = Frame(TodoGUI, width= 420, height= 350, highlightthickness= 0, borderwidth= 0, background= "#2d3134")
    frame1 = Frame(TodoGUI, width= 420, height= 280, highlightthickness= 0, borderwidth= 0, background= "#2d3134")

    # set frame todo list
    fr1 = LabelFrame(frame, text= "Todo List", width= 415, height= 300, background= "#2d3134", foreground= "white")
    lab = Label(frame, text= "Task :", font= 11, background= "#2d3134", foreground= "white")
    entr = Entry(frame, width= 30, borderwidth= 0, background= "light blue", font= (9), foreground= "black")

    add_button = Button(frame, image= add, highlightthickness= 0, borderwidth= 0, command= addbutton)

    Done = Button(fr1, image= done, highlightthickness= 0, borderwidth= 0, command= donebutton)
    Delete = Button(fr1, image= delete, highlightthickness= 0, borderwidth= 0, command= deletebutton)

    task1 = BooleanVar()
    task2 = BooleanVar()
    task3 = BooleanVar()
    task4 = BooleanVar()
    task5 = BooleanVar()
    task6 = BooleanVar()
    task7 = BooleanVar()

    Task1 = Checkbutton(fr1, variable= task1, text= "1. ")
    Task2 = Checkbutton(fr1, variable= task2, text= "2. ")
    Task3 = Checkbutton(fr1, variable= task3, text= "3. ")
    Task4 = Checkbutton(fr1, variable= task4, text= "4. ")
    Task5 = Checkbutton(fr1, variable= task5, text= "5. ")
    Task6 = Checkbutton(fr1, variable= task6, text= "6. ")
    Task7 = Checkbutton(fr1, variable= task7, text= "7. ")

    fr1.place(x= 2, y= 50)
    lab.place(x= 13, y= 15)
    entr.place(x= 70, y= 17)
    add_button.place(x= 350, y= 12)

    Done.place(x= 300, y= 250)
    Delete.place(x= 350, y= 250)

    Task1.place(x= 30, y= 10)
    Task2.place(x= 30, y= 45)
    Task3.place(x= 30, y= 80)
    Task4.place(x= 30, y= 115)
    Task5.place(x= 30, y= 150)
    Task6.place(x= 30, y= 185)
    Task7.place(x= 30, y= 220)


    # set fuction saxe button
    def savebutton():
        with open("ToDolist.txt", mode= "w") as file:
            a = tex.get("1.0", END)
            file.write(a)
        tex.delete("1.0",END)

    #set done frame
    fr2 = LabelFrame(frame1, text= "Done List", width= 412, height= 236, background= "#2d3134", foreground= "white")
    tex = Text(fr2, width= 50, height= 13, background= "light yellow", font= (20))
    Savebutton = Button(frame1, image= save, command= savebutton)

    fr2.place(x= 2, y= 2)
    tex.place(x= 2 ,y= 2)
    Savebutton.place(x=165, y= 240)


    frame.place(x= 40, y= 20)
    frame1.place(x= 40, y= 400)
    entr.focus_set()
    TodoGUI.mainloop()

Todolist()