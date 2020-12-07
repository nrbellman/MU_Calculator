#
#   Project Name: MU_Calculator
#   File Name: Calc_Interface.py
#   Author(s): Nicholas Bellman
#              Max Harris
#   Date Modified: 2020-11-19
#
#   A simple GUI calculator made with Python and tkinter.
#
#        Calculator Layout
#   -----------------------------
#   | [   Calculator Screen   ] | 
#   |---------------------------|
#   | [ e ][ π ][   ][ C ][ < ] |
#   | [ 7 ][ 8 ][ 9 ][ + ][ ^ ] |
#   | [ 4 ][ 5 ][ 6 ][ - ][ ( ] |
#   | [ 1 ][ 2 ][ 3 ][ * ][ ) ] |
#   | [   0    ][ . ][ / ][ = ] |
#   -----------------------------
#
if __name__ != "__main__":

    from files.Lexical_Analyzer import analyze
    from files.Validate import validate
    from files.Build_tree import *
    from files.Evaluate import evaluate
    import tkinter as tk
    import tkinter.font as tk_font


    # Window Initialization
    calc = tk.Tk()
    calc.title("MU Calculator") # Adds a title to the window.
    calc.resizable(0, 0) # Forces the window to be a constant size.

    # --------Style Definitions--------

    # Button font styles
    btn_font = tk_font.Font(family="Consolas",
                            size = 20, 
                            weight = "bold")
    # Input field font style.
    if_font = tk_font.Font(family="Consolas",
                           size = 30) 
    # Enables buttons to be sized with pixel dimensions.
    v_pix = tk.PhotoImage(width = 1,
                          height = 1) 
    ab = "#707070" # Button background color on click/keypress.
    af = "#f0f0f0" # Button foreground color on click/keypress.

    # -----Input Field  Definition-----
    calc_screen = tk.Entry(font = if_font,
                           width = 12, 
                           borderwidth = 5, 
                           justify = "right", 
                           state = "readonly")

    calc_screen.grid(row = 0, column = 0, columnspan = 5)

    # -------Function Definitions------
    
    # A list to store the numbers and symbols to be evaluated.
    input_list = []
    
    # Prints the input list to the terminal.
    print("Input list: ", end = "")
    print(input_list)
    
    # Boolean that stores the state of the calculator.
    # If True:  The expression displayed in the screen has been evaluated by
    #           the calculator.
    # If False: The expression displayed in the scteen has not been evaluated
    #           by the calculator yet
    is_answered = False 
    
    def input_append(symbol):
        """ 
        Appends a symbol to the input field and input list. 
        
        Parameters:\n
            symbol - The number or operator symbol being appended to the
                     current input of the calculator screen.
        """
        global is_answered
        if is_answered == True:
            # Checks to see if there is an answer displayed in the calculator
            # screen. If there is, reset the screen for new input.
            input_clear()
            is_answered = False
        if is_answered == False:
            # Adds the symbol to the input list.
            input_list.append(symbol)

        # Changes the state of the calculator screen from a read-only state to 
        # a normal state for input.
        calc_screen.config(state = "normal")
        # Adds the added symbol to the screen.
        calc_screen.insert("end", symbol)
        # Returns the screen to a read-only state.
        calc_screen.config(state = "readonly")

        # Ensures the most recent symbol is visible on the calculator screen.
        calc_screen.xview("end")
        
        print("Input list: ", end = "")
        print(input_list)

    def input_clear():
        """ 
        Clears the calcualtor screen and list of current inputs. 
        """
        
        if (len(input_list) > 0):
            input_list.clear() # Removes all elements of the input list.

            print("Input list: ", end = "")
            print(input_list)

        # Changes the state of the calculator screen from a read-only state to 
        # a normal state for input.
        calc_screen.config(state = "normal")
        # Clears all of the current inputs from the calculator screen.
        calc_screen.delete(0, "end")
        # Returns the screen to a read-only state.
        calc_screen.config(state = "readonly")
        
    def input_back():
        """ 
        Deletes the most recent entry from the calculator screen and input 
        list. 
        """

        # Checks if the input list is nonempty. If true, the last input is
        # popped off of the list.
        if (len(input_list) > 0):
            input_list.pop(len(input_list) - 1)

            print("Input list: ", end = "")
            print(input_list)

        # Changes the state of the calculator screen from a read-only state to 
        # a normal state for input.
        calc_screen.config(state = "normal")
        # Deletes the most recent entry from the calculator screen.
        calc_screen.delete(len(input_list),"end")
        # Returns the screen to a read-only state.
        calc_screen.config(state = "readonly")

    

    def calc_evaluate():
        """
        TODO: Implement the expression evaluation part of the calculator
        """
        global is_answered 

        lexeme_list = analyze(input_list)

        check = validate(lexeme_list)

        if(check != "passed"):
            input_clear()
            calc_screen.config(state = "normal")
            # Adds the added symbol to the screen.
            calc_screen.insert("end", check)
            # Returns the screen to a read-only state.
            calc_screen.config(state = "readonly")
            is_answered = True
        else:
            lexeme_tree = build_tree(lexeme_list)
            try:
                answer = evaluate(lexeme_tree)
            except ZeroDivisionError:
                answer = "Cannot divide by zero"
            if(isinstance(answer, float) and answer % 1 == 0.0):
                answer = int(answer)
            print("Answer: ", end = "")
            print(answer)

            input_clear()
            # Changes the state of the calculator screen from a read-only state to 
            # a normal state for input.
            calc_screen.config(state = "normal")
            # Displays the evaluated
            calc_screen.insert("end", answer)
            # Returns the screen to a read-only state.
            calc_screen.config(state = "readonly")
            is_answered = True


    def virtual_press(button):
        """ 
        Visually simulates the pressing of a given button and invokes the 
        command assigned to the button.

        Parameters:\n 
            button - The button that is being pressed.
        """

        # Changes the foreground and background color of the button to the same
        # colors that appear when the button is clicked on-screen.
        button.config(fg = af, bg = ab)
        # Invokes the button's command.
        button.invoke()

    def virtual_release(button):
        """
        Visually simulates the releasing of a given button.

        Paramters:\n
            button - The button that is being released.
        """

        # Changes the foreground and background colors of the button to their  
        # default values.
        button.config(fg = "#000000", bg = "#f0f0f0")

    # -------Button Definitions--------

    # Zero Button
    btn_0 = tk.Button(calc, 
                      text = "0", 
                      image = v_pix, 
                      width = 126, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("0"))

    btn_0.grid(row = 5, column = 0, columnspan = 2)
    
    calc.bind("0", lambda e: virtual_press(btn_0))
    calc.bind("<KeyRelease-0>", lambda e: virtual_release(btn_0))

    # [---One Button---]
    
    btn_1 = tk.Button(calc, # Initializes the button.
                      text = "1", 
                      image = v_pix,
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("1"))

    # Displays the button in the window.
    btn_1.grid(row = 4, column = 0)

    # Binds keypresses to functions that invoke the button command.
    calc.bind("1", lambda e: virtual_press(btn_1))
    calc.bind("<KeyRelease-1>", lambda e: virtual_release(btn_1))

    # Two Button
    btn_2 = tk.Button(calc, 
                      text = "2", 
                      image = v_pix, 
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("2"))
    
    btn_2.grid(row = 4, column = 1)
    calc.bind("2", lambda e: virtual_press(btn_2))
    calc.bind("<KeyRelease-2>", lambda e: virtual_release(btn_2))

    # Three Button
    btn_3 = tk.Button(calc, 
                      text = "3", 
                      image = v_pix,
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("3"))

    btn_3.grid(row = 4, column = 2)
    calc.bind("3", lambda e: virtual_press(btn_3))
    calc.bind("<KeyRelease-3>", lambda e: virtual_release(btn_3))

    # Four Button
    btn_4 = tk.Button(calc, 
                      text = "4", 
                      image = v_pix, 
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("4"))
    btn_4.grid(row = 3, column = 0)
    calc.bind("4", lambda e: virtual_press(btn_4))
    calc.bind("<KeyRelease-4>", lambda e: virtual_release(btn_4))

    # Five Button
    btn_5 = tk.Button(calc, 
                      text = "5", 
                      image = v_pix, 
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("5"))

    btn_5.grid(row = 3, column = 1)
    calc.bind("5", lambda e: virtual_press(btn_5))
    calc.bind("<KeyRelease-5>", lambda e: virtual_release(btn_5))

    # Six Button
    btn_6 = tk.Button(calc, 
                      text = "6", 
                      image = v_pix, 
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("6"))

    btn_6.grid(row = 3, column = 2)
    calc.bind("6", lambda e: virtual_press(btn_6))
    calc.bind("<KeyRelease-6>", lambda e: virtual_release(btn_6))

    # Seven Button
    btn_7 = tk.Button(calc, 
                      text = "7", 
                      image = v_pix, 
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("7"))

    btn_7.grid(row = 2, column = 0)
    calc.bind("7", lambda e: virtual_press(btn_7))
    calc.bind("<KeyRelease-7>", lambda e: virtual_release(btn_7))

    # Eight Button
    btn_8 = tk.Button(calc, 
                      text = "8", 
                      image = v_pix, 
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("8"))

    btn_8.grid(row = 2, column = 1)
    calc.bind("8", lambda e: virtual_press(btn_8))
    calc.bind("<KeyRelease-8>", lambda e: virtual_release(btn_8))

    # Nine Button
    btn_9 = tk.Button(calc, 
                      text = "9", 
                      image = v_pix, 
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("9"))

    btn_9.grid(row = 2, column = 2)
    calc.bind("9", lambda e: virtual_press(btn_9))
    calc.bind("<KeyRelease-9>", lambda e: virtual_release(btn_9))

    # e Button
    btn_e = tk.Button(calc, 
                      text = "e", 
                      image = v_pix, 
                      width = 60, 
                      height = 60, 
                      compound = "c", 
                      font = btn_font, 
                      bd = 1, 
                      activebackground = ab, 
                      activeforeground = af, 
                      command = lambda: input_append("e"))

    btn_e.grid(row = 1, column = 0)
    calc.bind("e", lambda e: virtual_press(btn_e))
    calc.bind("<KeyRelease-e>", lambda e: virtual_release(btn_e))

    # pi Button
    btn_pi = tk.Button(calc, 
                       text = "π", 
                       image = v_pix, 
                       width = 60, 
                       height = 60, 
                       compound = "c", 
                       font = btn_font, 
                       bd = 1, 
                       activebackground = ab, 
                       activeforeground = af, 
                       command = lambda: input_append("pi"))

    btn_pi.grid(row = 1, column = 1)
    calc.bind("p", lambda e: virtual_press(btn_pi))
    calc.bind("<KeyRelease-p>", lambda e: virtual_release(btn_pi))

    # Decimal Point Button
    btn_pnt = tk.Button(calc, 
                        text = ".", 
                        image = v_pix, 
                        width = 60, 
                        height = 60, 
                        compound = "c", 
                        font = btn_font, 
                        bd = 1, 
                        activebackground = ab, 
                        activeforeground = af, 
                        command = lambda: input_append("."))

    btn_pnt.grid(row = 5, column = 2)
    calc.bind(".", lambda e: virtual_press(btn_pnt))
    calc.bind("<KeyRelease-.>", lambda e: virtual_release(btn_pnt))

    # Addition Button
    btn_add = tk.Button(calc, 
                        text = "+", 
                        image = v_pix, 
                        width = 60, 
                        height = 60, 
                        compound = "c", 
                        font = btn_font, 
                        bd = 1, 
                        activebackground = ab, 
                        activeforeground = af, 
                        command = lambda: input_append("+"))

    btn_add.grid(row = 2, column = 3)
    calc.bind("+", lambda e: virtual_press(btn_add))
    calc.bind("<KeyRelease-+>", lambda e: virtual_release(btn_add))

    # Subtraction Button
    btn_sub = tk.Button(calc, 
                        text = "-", 
                        image = v_pix, 
                        width = 60, 
                        height = 60, 
                        compound = "c", 
                        font = btn_font, 
                        bd = 1, 
                        activebackground = ab, 
                        activeforeground = af, 
                        command = lambda: input_append("-"))

    btn_sub.grid(row = 3, column = 3)
    calc.bind("-", lambda e: virtual_press(btn_sub))
    calc.bind("<KeyRelease-->", lambda e: virtual_release(btn_sub))

    # Multiplication Button
    btn_mul = tk.Button(calc, 
                        text = "*", 
                        image = v_pix, 
                        width = 60, 
                        height = 60, 
                        compound = "c", 
                        font = btn_font, 
                        bd = 1, 
                        activebackground = ab, 
                        activeforeground = af, 
                        command = lambda: input_append("*"))

    btn_mul.grid(row = 4, column = 3)
    calc.bind("*", lambda e: virtual_press(btn_mul))
    calc.bind("<KeyRelease-*>", lambda e: virtual_release(btn_mul))

    # Division Button
    btn_div = tk.Button(calc, 
                        text = "/", 
                        image = v_pix, 
                        width = 60, 
                        height = 60, 
                        compound = "c", 
                        font = btn_font, 
                        bd = 1, 
                        activebackground = ab,
                        activeforeground = af, 
                        command = lambda: input_append("/"))

    btn_div.grid(row = 5, column = 3)
    calc.bind("/", lambda e: virtual_press(btn_div))
    calc.bind("<KeyRelease-/>", lambda e: virtual_release(btn_div))

    # Exponent Button
    btn_exp = tk.Button(calc, 
                        text = "^", 
                        image = v_pix, 
                        width = 60, 
                        height = 60, 
                        compound = "c", 
                        font = btn_font, 
                        bd = 1,
                        activebackground = ab, 
                        activeforeground = af, 
                        command = lambda: input_append("^"))

    btn_exp.grid(row = 2, column = 4)
    calc.bind("^", lambda e: virtual_press(btn_exp))
    calc.bind("<KeyRelease-^>", lambda e: virtual_release(btn_exp))

    # Left Parentheses Button
    btn_lparen = tk.Button(calc, 
                           text = "(", 
                           image = v_pix, 
                           width = 60, 
                           height = 60, 
                           compound = "c", 
                           font = btn_font, 
                           bd = 1, 
                           activebackground = ab, 
                           activeforeground = af, 
                           command = lambda: input_append("("))

    btn_lparen.grid(row = 3, column = 4)
    calc.bind("(", lambda e: virtual_press(btn_lparen))
    calc.bind("<KeyRelease-(>", lambda e: virtual_release(btn_lparen))

    # Right Parentheses Button
    btn_rparen = tk.Button(calc, 
                           text = ")", 
                           image = v_pix, 
                           width = 60, 
                           height = 60, 
                           compound = "c", 
                           font = btn_font, 
                           bd = 1, 
                           activebackground = ab, 
                           activeforeground = af, 
                           command = lambda: input_append(")"))

    btn_rparen.grid(row = 4, column = 4)
    calc.bind(")", lambda e: virtual_press(btn_rparen))
    calc.bind("<KeyRelease-)>", lambda e: virtual_release(btn_rparen))

    # Backspace Button
    btn_back = tk.Button(calc, 
                         text = "<", 
                         image = v_pix, 
                         width = 60, 
                         height = 60, 
                         compound = "c", 
                         font = btn_font,
                         bd = 1, 
                         activebackground = ab, 
                         activeforeground = af, 
                         command = input_back)

    btn_back.grid(row = 1, column = 4)
    calc.bind("<BackSpace>", lambda e: virtual_press(btn_back))
    calc.bind("<KeyRelease-BackSpace>", lambda e: virtual_release(btn_back))

    # Clear Button
    btn_clear = tk.Button(calc, 
                          text = "C", 
                          image = v_pix, 
                          width = 60, 
                          height = 60, 
                          compound = "c", 
                          font = btn_font,
                          bd = 1, 
                          activebackground = ab, 
                          activeforeground = af, 
                          command = input_clear)

    btn_clear.grid(row = 1, column = 3)
    calc.bind("c", lambda e: virtual_press(btn_clear))
    calc.bind("<KeyRelease-c>", lambda e: virtual_release(btn_clear))

    # Equals Button
    btn_eql = tk.Button(calc, 
                        text = "=", 
                        image = v_pix, 
                        width = 60, 
                        height = 60, 
                        compound = "c", 
                        font = btn_font, 
                        bd = 1, 
                        activebackground = ab, 
                        activeforeground = af, 
                        command = calc_evaluate)

    btn_eql.grid(row = 5, column = 4)
    calc.bind("<Return>", lambda e: virtual_press(btn_eql))
    calc.bind("=", lambda e: virtual_press(btn_eql))
    calc.bind("<KeyRelease-Return>", lambda e: virtual_release(btn_eql))
    calc.bind("<KeyRelease-=>", lambda e: virtual_release(btn_eql))

    calc.bind("<Escape>", lambda e: calc.destroy())

    # Tkinter main loop.
    calc.mainloop()
