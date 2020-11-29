# Returns whether the input is valid or not
# Displays errors so direct implementation into calc_interface may be necessary
# Could be changed to return an answer which can then be printed in calc_interface
def validate(lexeme_list):
        lparen_present = 0
        prev_isop = False
        prev_isLparen = False
        for index in lexeme_list:
            # Make sure close parens have an open paren
            if(index == "RPAREN"):
                if(lparen_present == 0):
                    input_clear()
                    calc_screen.config(state = "normal")
                    # Displays the error
                    calc_screen.insert("end", "RPAREN without LPAREN")
                    # Returns the screen to a read-only state.
                    calc_screen.config(state = "readonly")
                    return False
                else:
                    lparen_present -= 1
            if(index == "LPAREN"):
                lparen_present += 1
            # Check the numbers are actual numbers
            if(not (index in {"LPAREN", "RPAREN", "PLUS", "MINUS", "TIMES", "DIVIDES", "POWER", "E", "PI"})):
                try:
                    float(index[7:len(index) - 1])
                except ValueError:
                    input_clear()
                    calc_screen.config(state = "normal")
                    # Displays the error
                    calc_screen.insert("end", "Invalid number entered")
                    # Returns the screen to a read-only state.
                    calc_screen.config(state = "readonly")
                    return False
            # Don't allow operators to be next to each other
            if(index in {"PLUS", "MINUS", "TIMES", "DIVIDES", "POWER"}):
                if(prev_isop == True):
                    input_clear()
                    calc_screen.config(state = "normal")
                    # Displays the error
                    calc_screen.insert("end", "Operator cannot follow Operator")
                    # Returns the screen to a read-only state.
                    calc_screen.config(state = "readonly")
                    return False
                elif(prev_isop == False):
                    prev_isop = True
            # Don't allow operators to precede right parens
            if(prev_isop == True and index == "RPAREN"):
                input_clear()
                calc_screen.config(state = "normal")
                # Displays the error
                calc_screen.insert("end", "RPAREN cannot follow Operator")
                # Returns the screen to a read-only state.
                calc_screen.config(state = "readonly")
                return False
            if(not (index in {"PLUS", "MINUS", "TIMES", "DIVIDES", "POWER"})):
                prev_isop = False
            if(index == "LPAREN"):
                prev_isLparen = True
            # Make sure operators don't come directly after (
            if(prev_isLparen == True and (index in {"PLUS", "MINUS", "TIMES", "DIVIDES", "POWER"})):
                    input_clear()
                    calc_screen.config(state = "normal")
                    # Displays the error
                    calc_screen.insert("end", "Operator cannot follow LPAREN")
                    # Returns the screen to a read-only state.
                    calc_screen.config(state = "readonly")
                    return False
            elif(index != "LPAREN"):
                prev_isLparen = False
        # Make sure parenthesis are closed
        if(lparen_present != 0):
            input_clear()
            calc_screen.config(state = "normal")
            # Displays the error
            calc_screen.insert("end", "Unclosed parens")
            # Returns the screen to a read-only state.
            calc_screen.config(state = "readonly")
            return False
        return True
