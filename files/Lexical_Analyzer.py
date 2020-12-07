#
#   Project Name: MU_Calculator
#   File Name: Lexical_Analyzer.py
#   Author(s): Nicholas Bellman
#   Date Modified: 2020-11-19
#   
#   Scans characters from an input list, appropriately assigns them to a       
#   lexeme, and compiles the lexemes into a list.
#
def analyze(input_list):
    """
    [summary]

    Args:
        input_list (list): [description]

    Returns:
        list: [description]
    """

    print("\n|-----File: Lexical_Analyzer-----|\n")
    
    print("Input List: ", end = "")
    print(input_list)

    input_list.append(' ')

    lex = {"plus" : "+",
           "minus" : "-",
           "times" : "*",
           "divides" : "/",
           "power" : "^",
           "lparen" : "(",
           "rparen" : ")",
           "number" : ['0','1','2','3','4','5','6','7','8','9','.'],
           "pi" : "pi",
           "e" : "e"}
    
    lex_list = []
    dig_list = [] # Stores consecutive digits in the input list.
    
    for elem in input_list:
        
        # Handles numbers in the input list
        if elem in lex["number"]:
            dig_list.append(elem)
        elif dig_list != []:
            num = "".join(dig_list)
            lex_list.append("NUMBER(" + num + ")")
            dig_list = []

        if elem == lex["plus"]:
            lex_list.append("PLUS")

        if elem == lex["minus"]:
            lex_list.append("MINUS")
        
        if elem == lex["times"]:
            lex_list.append("TIMES")
        
        if elem == lex["divides"]:
            lex_list.append("DIVIDES")
        
        if elem == lex["power"]:
            lex_list.append("POWER")
        
        if elem == lex["lparen"]:
            lex_list.append("LPAREN")
        
        if elem == lex["rparen"]:
            lex_list.append("RPAREN")
        
        if elem == lex["pi"]:
            lex_list.append("PI")
        
        if elem == lex["e"]:
            lex_list.append("E")
            
    print("Lexeme List: ", end='')
    print(lex_list)

    print("\n|---End File: Lexical_Analyzer---|\n")

    return lex_list