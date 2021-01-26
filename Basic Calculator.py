from tkinter import *

root = Tk()
root.title("Basic Calculator")
root.configure(bg = "#232323")

#creates input box
operator = ""
finishedCalc = False
text_input = StringVar()
e = Entry(root, font = "Verdana 50", fg = "white", bg = "#333333", width = 10, borderwidth = 0, insertbackground = "#333333", cursor = "arrow", justify = 'right', textvariable = text_input)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#when number or operation is clicked
def button_click(sym):
    global operator
    global finishedCalc
    if ((sym == 0) or (sym == 1) or (sym == 2)or (sym == 3)or (sym == 4)or (sym == 5)or (sym == 6)or (sym == 7)or (sym == 8)or (sym == 9)):
        if finishedCalc:
            operator = ""
    finishedCalc = False
    operator = operator + str(sym) 
    text_input.set(operator)

#if clear cutton is clicked
def button_clear():
    global operator
    operator = ""
    text_input.set(operator)

#if equals button is clicked
def button_equals():
    global operator
    global finishedCalc
    finishedCalc = True
    sumup = eval(operator)
    if isinstance(sumup, int):
        text_input.set(str(sumup))
    else:
        text_input.set(str('%.8g' % sumup))   
    operator = str(sumup)
    
#creates buttons
button1 = Button(root, text = "1", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command=  lambda: button_click(1))
button2 = Button(root, text = "2", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command = lambda: button_click(2))
button3 = Button(root, text = "3", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click(3))
button4 = Button(root, text = "4", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click(4))
button5 = Button(root, text = "5", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click(5))
button6 = Button(root, text = "6", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click(6))
button7 = Button(root, text = "7", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click(7))
button8 = Button(root, text = "8", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click(8))
button9 = Button(root, text = "9", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click(9))
button0 = Button(root, text = "0", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click(0))
buttonAdd = Button(root, text = "+", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click("+"))
buttonSub = Button(root, text = "-", padx = 50, pady = 25, font = "Segoe 21", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click("-"))
buttonMul = Button(root, text = "*", padx = 50, pady = 25, font = "Segoe 21", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click("*"))
buttonDiv = Button(root, text = "/", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click("/"))
buttonDot = Button(root, text = ".", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command =  lambda: button_click("."))
buttonEqual = Button(root, text = "=", padx = 49.5, pady = 25, font = "Segoe 18", fg = "white", bg = "#5F5FEE", bd = 0, command = lambda: button_equals())
buttonClear = Button(root, text = "c", padx = 50, pady = 25, font = "Segoe 18", fg = "white", bg = "#232323", bd = 0, command = button_clear)

#places buttons
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

button0.grid(row = 4, column = 1)
buttonDot.grid(row = 4, column = 0)
buttonEqual.grid(row = 4, column = 2)

buttonDiv.grid(row = 1, column = 3)
buttonMul.grid(row = 2, column = 3)
buttonSub.grid(row = 3, column = 3)
buttonAdd.grid(row = 4, column = 3)
buttonClear.grid(row = 0, column = 3)


root.mainloop()