from math import e, pi
import operator
import re

class NumberNode:
    def __init__(self, value):
        self.value = value

class ExpressionNode:
    def __init__(self, op, left, right):
        if(op == 'PLUS'):
            self.op = operator.add
        if(op == 'MINUS'):
            self.op = operator.sub
        if(op == 'TIMES'):
            self.op = operator.mul
        if(op == 'DIVIDES'):
            self.op = operator.truediv
        if(op == 'POWER'):
            self.op = operator.pow  
        self.left = left
        self.right = right