# Evaluate the value of an arithmetic expression in
# RPN: Reverse Polish Notation. 

# Valid operators are +, -, *, /. Each operand may
# be an integer or another expression. 

# Division between two integers should truncate towards
# 0. 
from collections import deque
import math

class Solution:
    ops = {"+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)}

    def evalRPN(self, tokens):
        stack = deque([])

        for elem in tokens:
            if elem in self.ops:
                second = stack.pop()
                first = stack.pop()
                result = self.ops[elem](first, second)
                print(result)
                stack.append(result)
            else:
                stack.append(int(elem))
        
        return stack[0]

my = Solution()
 tokens0 = ["2","1","+","3","*"]
 tokens1 = ["4","13","5","/","+"]
tokens2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

#print(my.evalRPN(tokens0))
#print(my.evalRPN(tokens1))
print(my.evalRPN(tokens2))


