from files.Tree_Nodes import *
from queue import LifoQueue

def expr(lexeme_list, pos, prev_precedence):
    lhs = term(lexeme_list, pos, prev_precedence)
    pos = lhs[1]
    lhs = lhs[0]
    pos += 1
    if(pos < len(lexeme_list) and lexeme_list[pos] != "RPAREN"):
        op = lexeme_list[pos]
        pos += 1
        current_precedence = precedence(op)
        if(not(current_precedence < prev_precedence)):
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
        post_pos = pos
        while(lexeme_list[post_pos] != "RPAREN"):
            post_pos += 1
        return expr(lexeme_list, pos + 1, -1), post_pos
        

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
