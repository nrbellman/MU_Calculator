def validate(lexeme_list):
        lparen_present = 0
        prev_isop = False
        prev_isLparen = False
        for index in lexeme_list:
            if(index == "RPAREN"):
                if(lparen_present == 0):
                    return "RPAREN without LPAREN"
                else:
                    lparen_present -= 1
            if(index == "LPAREN"):
                lparen_present += 1
            if(not (index in {"LPAREN", "RPAREN", "PLUS", "MINUS", "TIMES", "DIVIDES", "POWER", "E", "PI"})):
                try:
                    float(index[7:len(index) - 1])
                except ValueError:
                    return "Invalid number entered"
            if(index in {"PLUS", "MINUS", "TIMES", "DIVIDES", "POWER"}):
                if(prev_isop == True):
                    return "Operator cannot follow Operator"
                elif(prev_isop == False):
                    prev_isop = True
            if(prev_isop == True and index == "RPAREN"):
                return "RPAREN cannot follow Operator"
            if(not (index in {"PLUS", "MINUS", "TIMES", "DIVIDES", "POWER"})):
                prev_isop = False
            if(index == "LPAREN"):
                prev_isLparen = True
            if(prev_isLparen == True and (index in {"PLUS", "MINUS", "TIMES", "DIVIDES", "POWER"})):
                    return "Operator cannot follow LPAREN"
            elif(index != "LPAREN"):
                prev_isLparen = False
        if(lparen_present != 0):
            return "Unclosed parens"
        return "passed"
