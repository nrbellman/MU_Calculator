#
# Project Name: MU_Calculator
# File Name: Concatinate.py
# Author(s): Max Harris
# Date Modified: 2020-11-10
#

def concat(input_list):
    newList = []
    current_string = ""
    # number_of_decimals = 0
    first_int = True
    index = 0
    new_index = 0
    while(index < len(input_list)):
        # Put the numbers with any potential decimal points together
        # into one string
        if(not isSymbol(input_list[index])):
            # if(input_list[index] == "."):
            #    number_of_decimals += 1
            # throw an error if too many decimal points
            # if(number_of_decimals > 1):
            #    input_clear()
            #    newList.clear()
            #    input_field.insert("end", "Error: invalid decimal point")
            #    fail = True
            current_string += input_list[index]
            if(not first_int):
                new_index-=1
            first_int = False
        # input a single operator
        if(isSymbol(input_list[index])):
            # append the previous string of number(s)
            if(current_string != ""):
                newList.append(current_string)
                first_int = True
                # number_of_decimals = 0
                current_string = ""
            # append the current operator
            current_string += input_list[index]
            newList.append(current_string)
            current_string = ""
            # Add * sign to multiple pi or e by the previous and next numbers
            # if not given an operation
            if(input_list[index] in {"e", "pi"}):
                if(index > 0):
                    if(isInt(input_list[index - 1]) or input_list[index - 1] == "."):
                        newList.insert(new_index, "*")
                        new_index += 1
                if(index < len(input_list) - 1):           
                    if(isInt(input_list[index + 1]) or input_list[index + 1] in {"e", "pi", "."}):
                        newList.insert(new_index + 1, "*")
                        new_index += 1
            # Add * sign to multiple (expr) by the previous and next numbers
            # if not given an operation
            if(input_list[index] == ")"):
                if(index < len(input_list) - 1):
                    if(isInt(input_list[index + 1]) or input_list[index + 1] in {"e", "pi", ".", "("}):
                        newList.insert(new_index + 1, "*")
                        new_index += 1
            if(input_list[index] == "("):
                if(index > 0):
                    if(isInt(input_list[index - 1]) or input_list[index - 1] in {"e", "pi", "."}):
                        newList.insert(new_index, "*")
                        new_index += 1
        new_index += 1
        index += 1
    # Make sure not to fill the new list with the first value if the decimal point check fails
    # But also dont forget to add any potential numbers after an operator
    # also prevents extra "" at the end
    if(current_string != ""):
        newList.append(current_string)
    return newList

def isInt(y):
    if(y in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}):
        return True
    else:
        return False

def isSymbol(y):
    if(y in {"(", ")", "^", "+", "-", "*", "/", "pi", "e"}):
        return True
    else:
        return False 
