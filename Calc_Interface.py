#
#   Project Name: MU_Calculator
#   File Name: Calc_Interface
#   Author: Nicholas Bellman
#   Date Modified: 2020-11-08
#
#   A simple GUI calculator made with Python and tkinter.
#
#        Calculator Layout
#   -----------------------------
#   | [     Input  Field      ] | 
#   | [  Clear ][   ][  Back  ] |
#   | [ 7 ][ 8 ][ 9 ][ + ][ ^ ] |
#   | [ 4 ][ 5 ][ 6 ][ - ][ ( ] |
#   | [ 1 ][ 2 ][ 3 ][ * ][ ) ] |
#   | [   0    ][ . ][ / ][ = ] |
#   -----------------------------
#

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
input_field = tk.Entry(font = if_font, width = 12, borderwidth = 5, justify = "right", state = "readonly") 
input_field.grid(row = 0, column = 0, columnspan = 5)

input_list = []
def input_append(symbol):
    """ Appends the chosen symbol to the input field and input list. """
    input_list.append(symbol)

    input_field.config(state = "normal")
    input_field.insert("end", symbol)
    input_field.config(state = "readonly")

    input_field.xview("end")
    
    print(input_list)

def input_clear():
    """ Clears the input field and input list. """
    if (len(input_list) > 0):
        input_list.clear()
        print(input_list)

    input_field.config(state = "normal")
    input_field.delete(0, "end")
    input_field.config(state = "readonly")
    
def input_back():
    """ Deletes the most recent entry from the input field and input list. """
    if (len(input_list) > 0):
        input_list.pop(len(input_list) - 1)
        print(input_list)

    input_field.config(state = "normal")
    input_field.delete(len(input_list),"end")
    input_field.config(state = "readonly")

def calc_evaluate():
    # TODO: Implement the expression evaluation part of the calculator
    pass


# Button Definitions

# Zero Button
btn_0 = tk.Button(calc, text = "0", image = v_pix, width = 126, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("0"))
btn_0.grid(row = 5, column = 0, columnspan = 2)
calc.bind("0", lambda e: btn_0.invoke())

# One Button
btn_1 = tk.Button(calc, text = "1", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("1"))
btn_1.grid(row = 4, column = 0)
calc.bind("1", lambda e: btn_1.invoke())

# Two Button
btn_2 = tk.Button(calc, text = "2", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("2"))
btn_2.grid(row = 4, column = 1)
calc.bind("2", lambda e: btn_2.invoke())

# Three Button
btn_3 = tk.Button(calc, text = "3", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("3"))
btn_3.grid(row = 4, column = 2)
calc.bind("3", lambda e: btn_3.invoke())

# Four Button
btn_4 = tk.Button(calc, text = "4", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("4"))
btn_4.grid(row = 3, column = 0)
calc.bind("4", lambda e: btn_4.invoke())

# Five Button
btn_5 = tk.Button(calc, text = "5", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("5"))
btn_5.grid(row = 3, column = 1)
calc.bind("5", lambda e: btn_5.invoke())

# Six Button
btn_6 = tk.Button(calc, text = "6", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("6"))
btn_6.grid(row = 3, column = 2)
calc.bind("6", lambda e: btn_6.invoke())

# Seven Button
btn_7 = tk.Button(calc, text = "7", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("7"))
btn_7.grid(row = 2, column = 0)
calc.bind("7", lambda e: btn_7.invoke())

# Eight Button
btn_8 = tk.Button(calc, text = "8", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("8"))
btn_8.grid(row = 2, column = 1)
calc.bind("8", lambda e: btn_8.invoke())

# Nine Button
btn_9 = tk.Button(calc, text = "9", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af, command = lambda: input_append("9"))
btn_9.grid(row = 2, column = 2)
calc.bind("9", lambda e: btn_9.invoke())

# Decimal Point Button
btn_pnt = tk.Button(calc, text = ".", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("."))
btn_pnt.grid(row = 5, column = 2)
calc.bind(".", lambda e: btn_pnt.invoke())

# Exponent Button
btn_exp = tk.Button(calc, text = "^", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("^"))
btn_exp.grid(row = 2, column = 4)
calc.bind("^", lambda e: btn_exp.invoke())

# Addition Button
btn_add = tk.Button(calc, text = "+", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("+"))
btn_add.grid(row = 2, column = 3)
calc.bind("+", lambda e: btn_add.invoke())

# Subtraction Button
btn_sub = tk.Button(calc, text = "-", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("-"))
btn_sub.grid(row = 3, column = 3)
calc.bind("-", lambda e: btn_sub.invoke())

# Multiplication Button
btn_mul = tk.Button(calc, text = "*", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("*"))
btn_mul.grid(row = 4, column = 3)
calc.bind("*", lambda e: btn_mul.invoke())

# Division Button
btn_div = tk.Button(calc, text = "/", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = lambda: input_append("/"))
btn_div.grid(row = 5, column = 3)
calc.bind("/", lambda e: btn_div.invoke())

# Left Parentheses Button
btn_lparen = tk.Button(calc, text = "(", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                       activebackground = ab, activeforeground = af, command = lambda: input_append("("))
btn_lparen.grid(row = 3, column = 4)
calc.bind("(", lambda e: btn_lparen.invoke())

# Right Parentheses Button
btn_rparen = tk.Button(calc, text = ")", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1, 
                       activebackground = ab, activeforeground = af, command = lambda: input_append(")"))
btn_rparen.grid(row = 4, column = 4)
calc.bind(")", lambda e: btn_rparen.invoke())

# Backspace Button
btn_back = tk.Button(calc, text = "Back", image = v_pix, width = 126, height = 60, compound = "c", font = btn_font, bd = 1, 
                     activebackground = ab, activeforeground = af, command = input_back)
btn_back.grid(row = 1, column = 3, columnspan = 2)
calc.bind("<BackSpace>", lambda e: btn_back.invoke())

# Clear Button
btn_clear = tk.Button(calc, text = "Clear", image = v_pix, width = 126, height = 60, compound = "c", font = btn_font, bd = 1, 
                      activebackground = ab, activeforeground = af, command = input_clear)
btn_clear.grid(row = 1, column = 0, columnspan = 2)
calc.bind("c", lambda e: btn_clear.invoke())

# Equals Button
btn_eql = tk.Button(calc, text = "=", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af, command = calc_evaluate)
btn_eql.grid(row = 5, column = 4)
calc.bind("<Return>", lambda e: btn_eql.invoke())
calc.bind("=", lambda e: btn_eql.invoke())



calc.mainloop()