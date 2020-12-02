from files.Tree_Nodes import *
from queue import LifoQueue

def expr(lexeme_list, pos, prev_precedence):
    lhs = term(lexeme_list, pos, prev_precedence)
    if(pos != lhs[1]):
        pos = lhs[1]
    lhs = lhs[0]
    while(pos < len(lexeme_list) - 1):
        pos += 1
        op = lexeme_list[pos]
        print(op)
        pos += 1
        if(op == "RPAREN"):
            break
        else:
            current_precedence = precedence(op)
            if(current_precedence < prev_precedence):
                break
            if(association(op) == "left"):
                rhs = expr(lexeme_list, pos, current_precedence + 1)
            else:
                rhs = expr(lexeme_list, pos, current_precedence)
            lhs = ExpressionNode(op, lhs, rhs)
    return lhs


def term(lexeme_list, pos, current_precedence):
    value = lexeme_list[pos]
    if(value[0:6] == "NUMBER"):
        return NumberNode(float(value[7:len(value) - 1])), pos
    elif(value == "PI"):
        return NumberNode(pi), pos
    elif(value == "E"):
        return NumberNode(e), pos
    elif(value == "LPAREN"):
        posb = pos
        while(lexeme_list[pos] != "RPAREN"):
            pos += 1
        return expr(lexeme_list, posb + 1, -1), pos
        

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
