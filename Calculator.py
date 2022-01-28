#tkinter - Creating GUI


from tkinter import * 
import math

mainscreen = Tk()              #Creates a main screen
mainscreen.title("Chaitanya's Calculator")


e = Entry( width = 35, borderwidth = 3 )         #Creates an input box
e.grid(row = 0, column = 0 , columnspan = 10, padx = 10, pady = 10)  # To grid the in put box using .grid()


# All functions 



def algo(number):         
         current = e.get()
         e.delete(0,END)
         e.insert(0,str(current) + str(number))
         

def clear():
         e.delete(0,END)
         
def add():
         inserted_no = e.get()
         global n
         global math
         math = 'addition'
         n = int(inserted_no)
         e.delete(0,END)
         
def multiply():
         inserted_no = e.get()
         global n
         global math
         math = 'multiplication'
         n = int(inserted_no)
         e.delete(0,END)
def divide():
         inserted_no = e.get()
         global n
         global math
         math = 'division'
         n = int(inserted_no)
         e.delete(0,END)
def subtract():
         inserted_no = e.get()
         global n
         global math
         math = 'subtraction'
         n = int(inserted_no)
         e.delete(0,END)
         
         

def equals():
         n2 = e.get()
         e.delete(0,END)
         if math == 'addition':
                 e.insert(0, int(n)+int(n2))
         if math == 'multiplication':
                 e.insert(0, int(n)*int(n2))
         if math == 'division':
                 e.insert(0, int(n)/int(n2))
         if math == 'subtraction':
                 e.insert(0, int(n)-int(n2))
         

#Define the buttons using Button(screen-name,text on box , cellpadding , command(functions))

      
button1 = Button(mainscreen ,text = "1",  padx = 40, pady = 20,  command = lambda: algo(1))
button2 = Button(mainscreen ,text = "2",  padx = 40, pady = 20, command = lambda: algo(2))
button3 = Button(mainscreen ,text = "3",  padx = 40, pady = 20, command = lambda: algo(3))
button4 = Button(mainscreen ,text = "4",  padx = 40, pady = 20, command = lambda: algo(4))
button5 = Button(mainscreen ,text = "5",  padx = 40, pady = 20, command = lambda: algo(5))
button6 = Button(mainscreen ,text = "6",  padx = 40, pady = 20, command = lambda: algo(6))
button7 = Button(mainscreen ,text = "7",  padx = 40, pady = 20, command = lambda: algo(7))
button8 = Button(mainscreen ,text = "8",  padx = 40, pady = 20, command = lambda: algo(8))
button9 = Button(mainscreen ,text = "9",  padx = 40, pady = 20, command = lambda: algo(9))
button10 = Button(mainscreen ,text = "0", padx = 40, pady = 20, command = lambda: algo(0))
buttonadd = Button(mainscreen , text = "+", padx = 39, pady = 20,  command = add)
buttonmul = Button(mainscreen , text = "*", padx = 40, pady = 20,  command = multiply)
buttondiv = Button(mainscreen , text = "/", padx = 40, pady = 20,  command = divide)
buttonsub = Button(mainscreen , text = "-", padx = 41, pady = 20,  command = subtract)
#buttonsq = Button(mainscreen , text = "SQRT", , command = sqrt)
buttonclear = Button(mainscreen , text = "Clear", padx = 78, pady = 20,  command =clear) 
buttonequal = Button(mainscreen , text = "=", padx = 87, pady = 20,command = equals)
 
# Gridding buttons using .grid(row,columns,rowspan,columnspan)

button1.grid(row =3 , column =0)
button2.grid(row =3 , column =1)
button3.grid(row =3 , column =2)
button4.grid(row =2 , column =0)
button5.grid(row =2 , column =1)
button6.grid(row =2 , column =2)
button7.grid(row =1 , column =0)
button8.grid(row =1 , column =1)
button9.grid(row =1 , column =2)
button10.grid(row =4 , column =0)
buttonadd.grid(row = 5, column = 0)
buttonclear.grid(row = 4, column = 1, columnspan = 2)
buttonequal.grid(row = 5, column = 1, columnspan = 2)

buttondiv.grid(row = 6, column = 2)
buttonmul.grid(row = 6, column = 0)
buttonsub.grid(row = 6, column = 1)

mainscreen.mainloop()





