from files.Tree_Nodes import *
from queue import LifoQueue

def expr(prev_precedence):
    lhs = term()
    while(len(lexeme_list) > 0):
        op = lexeme_list.pop(0)
        if(op == "RPAREN"):
            break
        current_precedence = precedence(op)
        if(current_precedence < prev_precedence):
            lexeme_list.insert(0, op)
            break
        elif(len(lexeme_list) > 0):
            if(association(op) == "left"):
                rhs = expr(current_precedence + 1)
            else:
                rhs = expr(current_precedence)
        lhs = ExpressionNode(op, lhs, rhs) 
    return lhs


def term():
    value = lexeme_list.pop(0)
    if(value[0:6] == "NUMBER"):
        return NumberNode(float(value[7:len(value) - 1]))
    elif(value == "PI"):
        return NumberNode(pi)
    elif(value == "E"):
        return NumberNode(e)
    elif(value == "LPAREN"):
        node = expr(-1)
        return node
        

def precedence(op):
    if(op in {"PLUS", "MINUS"}):
        return 0
    if(op in {"TIMES", "DIVIDES"}):
        return 1
    if(op == "POWER"):
        return 2
    else:
        return -1

def association(op):
    if(op in {"PLUS", "MINUS", "TIMES", "DIVIDES"}):
        return "left"
    if(op in {"POWER"}):
        return "right"

def build_tree(list1):
    global lexeme_list
    lexeme_list = list1
    return expr(-1)