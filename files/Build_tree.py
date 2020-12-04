from files.Tree_Nodes import *
from queue import LifoQueue

def expr(prev_precedence):
    lhs = term(prev_precedence)
    while(len(lexeme_list) > 0):
        op = lexeme_list.pop(0)
        current_precedence = precedence(op)
        if(op == "RPAREN"):
            break
        if(current_precedence < prev_precedence):
            break
        if(association(op) == "left"):
            rhs = expr(current_precedence + 1)
        else:
            rhs = expr(current_precedence)
        lhs = ExpressionNode(op, lhs, rhs)
    return lhs


def term(current_precedence):
    value = lexeme_list.pop(0)
    if(value[0:6] == "NUMBER"):
        return NumberNode(float(value[7:len(value) - 1]))
    elif(value == "PI"):
        return NumberNode(pi)
    elif(value == "E"):
        return NumberNode(e)
    elif(value == "LPAREN"):
        return expr(-1)
        

def precedence(op):
    if(op in {"PLUS", "MINUS"}):
        return 0
    if(op in {"TIMES", "DIVIDES"}):
        return 1
    if(op == "POWER"):
        return 2

def association(op):
    if(op in {"PLUS", "MINUS", "TIMES", "DIVIDES"}):
        return "left"
    if(op in {"POWER"}):
        return "right"

def build_tree(lexeme_list):
    return expr(lexeme_list, 0, -1)
