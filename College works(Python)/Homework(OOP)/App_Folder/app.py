import tkinter as tk
from tkinter import ttk
from tkinter import Menu
import SpaceShip
class App: 
    def __init__(self): 
        self.win = tk.Tk() #making a new class(сделали окошко)
        self.win.geometry("1280x720")#size
        self.win.title("Ships")#title and window size
        self.setUI()
        self.win.mainloop()#запуск
    def SettingsWindow(self):
        self.setWin = tk.Tk()
        self.setWin.geometry("550x550+100+100")
        self.setWin.title("Look at ships")

        
        
        self.lbox = tk.Listbox(self.setWin,width=60,height=30)
        self.lbox.pack(padx=5,pady=5)
        self.items = ["елеменеты",1,2,3,]
        for item in self.items:
            self.lbox.insert(item)
        

        self.setWin.mainloop()
    
        # 1 0 2 0 
    def setUI(self):
        p = {'padx':10,'pady':10}
        
        self.nameLbn = ttk.Label(text="Тип корабля")
        self.nameLbn.grid(row=0,column=0,**p)
        items = ["Маленький","Средний","Большой"]
        self.itemList = ttk.Combobox(values=items)
        self.itemList.grid(row = 1, column=0,**p)
        
        self.quantityLbn=ttk.Label(text="Количество")
        self.quantityLbn.grid(row=0,column=1,**p)
        self.quantityEntry = ttk.Entry()
        self.quantityEntry.grid(row=1,column=1,**p)
        
        self.priceLbn = ttk.Label(text="Цена")
        self.priceLbn.grid(row=0,column=3,**p)
        self.priceEntry = ttk.Entry()
        self.priceEntry.grid(row=1,column=3,**p)
        
        self.sellbtn = ttk.Button(text="Sell")
        self.sellbtn.grid(row=2,column= 0,columnspan=2,**p)
        self.buybtn = ttk.Button(text="Buy")
        self.buybtn.grid(row=2,column= 2,columnspan=1,**p)
        
        
        #listbox
    
        #listbox
        menubar = Menu(self.win)
        self.win.config(menu=menubar)
        file_menu = Menu(menubar)
        file_menu.add_command(
        label='Exit',
        command=self.win.destroy
        )
        file_menu.add_command(
            label='Settings',
            command = self.SettingsWindow
        )
        menubar.add_cascade(
        label="File",
        menu=file_menu
        )

initC = App()