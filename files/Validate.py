# Returns whether the input is valid or not
# Displays errors so direct implementation into calc_interface may be necessary
def validate(lexeme_list):
        lparen_present = 0
        prev_isop = False
        prev_isLparen = False
        prev_item = ""
        for index in lexeme_list:
            if(index == "RPAREN"):
                if(lparen_present == 0):
                    return "RPAREN without LPAREN"
                else:
                    lparen_present -= 1
            if(index == "LPAREN"):
                lparen_present += 1
            if(index[0:6] == "NUMBER"):
                try:
                    float(index[7:len(index) - 1])
                except ValueError:
                    return "Invalid number entered"
            if(prev_item == "RPAREN" and index[0:6] == "NUMBER"):
                return "Please specify operator after RPAREN"
            if(index == "LPAREN" and prev_item[0:6] == "NUMBER"):
                return "Please specify operator before LPAREN"
            if(prev_item[0:6] == "NUMBER" and (index == "PI" or index == "E")):
                return "Please specify operator between numbers and symbols"
            if(index[0:6] == "NUMBER" and (prev_item == "PI" or prev_item == "E")):
                return "Please specify operator between numbers and symbols"
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
            prev_item = index
        if(lparen_present != 0):
            return "Unclosed parens"
        return "passed"