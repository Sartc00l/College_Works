import tkinter as tk
import pickle
import tkinter.messagebox
from tkinter import ttk
from tkinter import Menu
import SpaceShip
class App: 
    
    def __init__(self): 
        self.arrShips =[]
        self.smallShip = SpaceShip.SmallShip("","")
        self.mediumShip = SpaceShip.MediumShip("","")
        self.bigShip = SpaceShip.BigShip("","")
        
        self.win = tk.Tk() #making a new class(сделали окошко)
        self.win.geometry("1280x720")
        self.win.title("Ships")#title and window size
        self.setUI()
        self.win.mainloop()#запуск
    
    def setUI(self):
        p = {'padx':10,'pady':10}
        
        self.nameLbn = ttk.Label(text="Тип корабля")
        self.nameLbn.grid(row=0,column=0,**p)
        
        items = ["Маленький","Средний","Большой"]
        self.itemCmbox = ttk.Combobox(values=items)
        self.itemCmbox.grid(row = 1, column=0,**p)
 
        self.buttonSetCmbox = tk.Button(text="Сохранить в lbox",command=self.setValueToLbx)
        self.buttonSetCmbox.grid(row=3,column=0)
        
        self.individualParLbn=ttk.Label(text="Выберите тип корабля")
        self.individualParLbn.grid(row=0,column=1,**p)
        
        self.quantityEntry = ttk.Entry()
        self.quantityEntry.grid(row=1,column=1,**p)
        
        self.nameLbn = ttk.Label(text="Наименование корабля")
        self.nameLbn.grid(row=0,column=3,**p)
        
        self.nameEntry = ttk.Entry()
        self.nameEntry.grid(row=1,column=3,**p)
        
        self.saveBtn = ttk.Button(text="Сохранить в файл",command=self.saveResultIntoFile)
        self.saveBtn.grid(row=3,column= 1,columnspan=2,**p)
        
        def changeLbn(event):
            match event.widget.get():
                case "Маленький":
                    self.individualParLbn.config(text="Размер команды")
                case "Средний":
                    self.individualParLbn.config(text="Количество продуктов")
                case "Большой":
                    self.individualParLbn.config(text="Размер колонии")
                case _:
                    self.individualParLbn.config(text="Выберите тип корабля") 
        self.itemCmbox.bind("<<ComboboxSelected>>", changeLbn)#Бинд на выборку пользователя в combobox

        menubar = Menu(self.win)
        self.win.config(menu=menubar)
        file_menu = Menu(menubar)
        file_menu.add_command(
        label='Exit',
        command=self.win.destroy
        )
        file_menu.add_command(
            label='View windows',
            command = self.add_win
        )
        menubar.add_cascade(
        label="File",
        menu=file_menu
        )
       
    def setValueToLbx(self):
        if self.nameEntry.get() is not None and self.quantityEntry.get() is not None:
            match self.itemCmbox.get():
                case "Маленький":
                    self.smallShip = SpaceShip.SmallShip(self.nameEntry.get(),self.quantityEntry.get())
                    self.arrShips.append(f"Имя малого корабля: {self.nameEntry.get()}")
                    self.arrShips.append(f"Размер команды: {self.quantityEntry.get()}")
                    self.arrShips.append(f"Скорость корабля: {self.smallShip.velocity}")
                    self.arrShips.append("")
                    tkinter.messagebox.showinfo(message=f"Успешно добавили малый корабль")
                case "Средний":
                    self.mediumShip = SpaceShip.MediumShip(self.nameEntry.get(),self.quantityEntry.get())
                    self.arrShips.append(f"Имя среднего корабля: {self.nameEntry.get()}")
                    self.arrShips.append(f"Количество продуктов: {self.quantityEntry.get()}")
                    self.arrShips.append(f"Скорость корабля: {self.mediumShip.velocity}\n")
                    self.arrShips.append("")
                    tkinter.messagebox.showinfo(message=f"Успешно добавили средний корабль")
                case "Большой":
                    self.bigShip = SpaceShip.BigShip(self.nameEntry.get(),self.quantityEntry.get())
                    self.arrShips.append(f"Имя большого корабля: {self.nameEntry.get()}")
                    self.arrShips.append(f"Размер колонии: {self.quantityEntry.get()}")
                    self.arrShips.append(f"Скорость корабля: {self.bigShip.velocity}")
                    self.arrShips.append("")
                    tkinter.messagebox.showinfo(message=f"Успешно добавили большой корабль")
                case _:
                    tkinter.messagebox.showerror(title="Ошибка ввода",message=f"Ошибка ввода\nПроверьте правильность ввода данных")
        elif self.nameEntry.get() is None and self.quantityEntry.get() is None:
            tkinter.messagebox.showerror(title="Ошибка",message=f"Ошибка ввода {self.nameEntry.get()} {self.quantityEntry.get()}")
    
    def saveResultIntoFile(self):
        self.arrShips = [self.smallShip,self.mediumShip,self.bigShip]
        with open('ships.pickle','wb') as f:
            pickle.dump(self.arrShips,f)
            
    def add_win(self):
        
        self.setWin = tk.Toplevel(self.win)#С tk.Tk() возникает проблема из-за которой невозможно передавать что-либо в листбокс
        self.setWin.geometry("550x550+100+100")
        self.setWin.title("Information")

        self.itemsGet= tk.StringVar(value=self.arrShips)
        self.lbox = tk.Listbox(self.setWin,width=50,height=50,listvariable=self.itemsGet)
        self.lbox.grid(column=0,row=0,columnspan=20)
        
        self.setWin.mainloop()

initC = App()
exit()