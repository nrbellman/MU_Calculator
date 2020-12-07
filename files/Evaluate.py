from files.Tree_Nodes import *

def evaluate(node):
    if(isinstance(node, ExpressionNode)):
        lhs = evaluate(node.left)
        rhs = evaluate(node.right)
        return node.op(lhs, rhs)
    else:
        return node.value