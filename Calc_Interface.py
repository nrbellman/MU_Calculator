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
input_field = tk.Entry(font = if_font, width = 10, borderwidth = 5, justify = "right")

# Input Field Display 
input_field.place(x = 0, y = 0, width = 263)


# One Button
btn_1 = tk.Button(calc, text = "1", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Two Button
btn_2 = tk.Button(calc, text = "2", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Three Button
btn_3 = tk.Button(calc, text = "3", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Four Button
btn_4 = tk.Button(calc, text = "4", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Five Button
btn_5 = tk.Button(calc, text = "5", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Six Button
btn_6 = tk.Button(calc, text = "6", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Seven Button
btn_7 = tk.Button(calc, text = "7", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Eight Button
btn_8 = tk.Button(calc, text = "8", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Nine Button
btn_9 = tk.Button(calc, text = "9", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Zero Button
btn_0 = tk.Button(calc, text = "0", image = v_pix, width = 126, height = 60, compound = "c", font = btn_font, bd = 1,
                  activebackground = ab, activeforeground = af)

# Decimal Point Button
btn_pnt = tk.Button(calc, text = ".", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af)

# Exponent Button
btn_exp = tk.Button(calc, text = "^", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af)

# Addition Button
btn_add = tk.Button(calc, text = "+", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af)

# Subtraction Button
btn_sub = tk.Button(calc, text = "-", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af)

# Multiplication Button
btn_mul = tk.Button(calc, text = "*", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af)

# Division Button
btn_div = tk.Button(calc, text = "/", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af)

# Equals Button
btn_eql = tk.Button(calc, text = "=", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                    activebackground = ab, activeforeground = af)

# Left Parentheses Button
btn_lparen = tk.Button(calc, text = "(", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1,
                       activebackground = ab, activeforeground = af)

# Right Parentheses Button
btn_rparen = tk.Button(calc, text = ")", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1, 
                       activebackground = ab, activeforeground = af)

# Clear Button
btn_clear = tk.Button(calc, text = "C", image = v_pix, width = 60, height = 60, compound = "c", font = btn_font, bd = 1, 
                      activebackground = ab, activeforeground = af)


# Button Display
btn_clear.grid(row = 0, column = 4)

btn_7.grid(row = 1, column = 0)
btn_8.grid(row = 1, column = 1)
btn_9.grid(row = 1, column = 2)
btn_add.grid(row = 1, column = 3)
btn_exp.grid(row = 1, column = 4)

btn_4.grid(row = 2, column = 0)
btn_5.grid(row = 2, column = 1)
btn_6.grid(row = 2, column = 2)
btn_sub.grid(row = 2, column = 3)
btn_lparen.grid(row = 2, column = 4)

btn_1.grid(row = 3, column = 0)
btn_2.grid(row = 3, column = 1)
btn_3.grid(row = 3, column = 2)
btn_mul.grid(row = 3, column = 3)
btn_rparen.grid(row = 3, column = 4)

btn_0.grid(row = 4, column = 0, columnspan = 2)
btn_pnt.grid(row = 4, column = 2)
btn_div.grid(row = 4, column = 3)
btn_eql.grid(row = 4, column = 4)

calc.mainloop()