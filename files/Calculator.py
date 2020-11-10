# Imports
import tkinter as tk
import tkinter.font as tk_font

# Window Initialization
calc = tk.Tk()
calc.title("MU Calculator")
calc.resizable(0, 0)

# Style Definitions
btn_font = tk_font.Font(family="Consolas", size = 20, weight = "bold") # Button font style.
if_font = tk_font.Font(family="Consolas", size = 30) # Input field font style.
v_pix = tk.PhotoImage(width = 1, height = 1) # Enables buttons to be sized with pixel dimensions.
ab = "#707070" # Button background color on click.
af = "#f0f0f0" # Button foreground color on click.

# Input Field Definition
input_field = tk.Entry(font = if_font, width = 12, borderwidth = 5, justify = "right") 
input_field.grid(row = 0, column = 0, columnspan = 5)

input_list = []
def input_append(symbol):
    """ Appends the chosen symbol to the input field and input list. """
    input_list.append(symbol)
    input_field.insert("end", symbol)
    print(input_list)

def input_clear():
    """ Clears the input field and input list. """
    if (len(input_list) > 0):
        input_list.clear()
        print(input_list)
    
    input_field.delete(0, "end")
    
def input_back():
    """ Deletes the most recent entry from the input field and input list. """
    if (len(input_list) > 0):
        input_list.pop(len(input_list) - 1)
        print(input_list)

    input_field.delete(len(input_list),"end")

# def input_check(input_list):
#     LWithoutR = False
#     recentOperator = -1
#     index = 0
#     for x in input_list:
#         if(x == "("):
#             LWithoutR = True
#         elif(x == ")" and LWithoutR == True):
#             LWithoutR = False
#         elif(x == ")" and LWithoutR == False):
#             input_clear()
#             input_field.insert("end", "Error: ) without (")
#         if(not(isInt(x)) and x != "."):
#             recentOperator = index
#         if(x == "."):
#             current_string = ""
#             i = recentOperator + 1
#             while((i < len(input_list) - 1) and (isInt(input_list) or input_list[i] == ".")):
#                 current_string += input_list.pop(i)
#             input_list.insert(i, current_string)
#     index += 1 

def use_input(input_list):
    input_list = concat(input_list)
    print(input_list)
    error_check(input_list)

def concat(input_list):
    newList = []
    current_string = ""
    number_of_decimals = 0
    fail = False
    for i in input_list:
        if(not isSymbol(i)):
            if(i == "."):
                number_of_decimals += 1
            if(number_of_decimals > 1):
                input_clear()
                newList.clear()
                input_field.insert("end", "Error: invalid decimal point")
                fail = True
            current_string += i
        if(isSymbol(i)):
            if(current_string != ""):
                newList.append(current_string)
                number_of_decimals = 0
                current_string = ""
            current_string += i
            newList.append(current_string)
            current_string = ""
    if(not fail and current_string != ""):
        newList.append(current_string)
    return newList
        

def error_check(input_list):
    LwithoutR = False
    index = 0
    while(index < len(input_list)):
        if(input_list[index] == "("):
            LwithoutR = True
        elif(input_list[index] == ")" and LwithoutR == True):
            LwithoutR = False
        elif(input_list[index] == ")" and LwithoutR == False):
            input_clear()
            input_field.insert("end", "Error: ) without (")
            break
        if(index > 0):
            if(input_list[index] == ")" and input_list[index - 1] == "("):
                input_clear()
                input_field.insert("end", "Error: empty ()")
                break
            if(isSymbol(input_list[index]) and isSymbol(input_list[index - 1])):
                if(input_list[index] != "(" and input_list[index - 1] != ")"):
                    input_clear()
                    input_field.insert("end", "Error: invalid operation placement")
                    break
        if(index == 0 and isSymbol(input_list[index])):
            if(input_list[index] != "("):
                input_clear()
                input_field.insert("end", "Error: invalid operation placement")
                break
        index += 1
    if(LwithoutR):
        input_clear()
        input_field.insert("end", "Error: ( without )")

def isInt(y):
    if(y in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}):
        return True
    else:
        return False

def isSymbol(y):
    if(y in {"(", ")", "^", "+", "-", "/"}):
        return True
    else:
        return False


# One Button
btn_1 = tk.Button(calc, text = "1", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("1"))

# Two Button
btn_2 = tk.Button(calc, text = "2", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("2"))

# Three Button
btn_3 = tk.Button(calc, text = "3", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("3"))

# Four Button
btn_4 = tk.Button(calc, text = "4", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("4"))

# Five Button
btn_5 = tk.Button(calc, text = "5", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("5"))

# Six Button
btn_6 = tk.Button(calc, text = "6", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("6"))

# Seven Button
btn_7 = tk.Button(calc, text = "7", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("7"))

# Eight Button
btn_8 = tk.Button(calc, text = "8", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("8"))

# Nine Button
btn_9 = tk.Button(calc, text = "9", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("9"))

# Zero Button
btn_0 = tk.Button(calc, text = "0", image = v_pix, width = 126, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("0"))

# Decimal Point Button
btn_pnt = tk.Button(calc, text = ".", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("."))

# Exponent Button
btn_exp = tk.Button(calc, text = "^", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("^"))

# Addition Button
btn_add = tk.Button(calc, text = "+", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("+"))

# Subtraction Button
btn_sub = tk.Button(calc, text = "-", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("-"))

# Multiplication Button
btn_mul = tk.Button(calc, text = "*", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("*"))

# Division Button
btn_div = tk.Button(calc, text = "/", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("/"))

# Equals Button
btn_eql = tk.Button(calc, text = "=", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: use_input(input_list))

# Left Parentheses Button
btn_lparen = tk.Button(calc, text = "(", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                       activebackground = ab, activeforeground = af, command = lambda: input_append("("))

# Right Parentheses Button
btn_rparen = tk.Button(calc, text = ")", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1, 
                       activebackground = ab, activeforeground = af, command = lambda: input_append(")"))

# Backspace Button
btn_back = tk.Button(calc, text = "<-", image = v_pix, width = 126, height = 60, compound = "c", font = btn_font, bd = 1, 
                     activebackground = ab, activeforeground = af, command = input_back)

# Clear Button
btn_clear = tk.Button(calc, text = "C", image = v_pix, width = 126, height = 60, compound = "c", font = btn_font, bd = 1, 
                      activebackground = ab, activeforeground = af, command = input_clear)


# Button Display
btn_clear.grid(row = 1, column = 0, columnspan = 2)
btn_back.grid(row = 1, column = 3, columnspan = 2)

btn_7.grid(row = 2, column = 0)
btn_8.grid(row = 2, column = 1)
btn_9.grid(row = 2, column = 2)
btn_add.grid(row = 2, column = 3)
btn_exp.grid(row = 2, column = 4)

btn_4.grid(row = 3, column = 0)
btn_5.grid(row = 3, column = 1)
btn_6.grid(row = 3, column = 2)
btn_sub.grid(row = 3, column = 3)
btn_lparen.grid(row = 3, column = 4)

btn_1.grid(row = 4, column = 0)
btn_2.grid(row = 4, column = 1)
btn_3.grid(row = 4, column = 2)
btn_mul.grid(row = 4, column = 3)
btn_rparen.grid(row = 4, column = 4)

btn_0.grid(row = 5, column = 0, columnspan = 2)
btn_pnt.grid(row = 5, column = 2)
btn_div.grid(row = 5, column = 3)
btn_eql.grid(row = 5, column = 4)

calc.mainloop()

