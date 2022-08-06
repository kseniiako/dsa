# Valid Parentheses: given a string s containing
# just the characters {}, [], (), determine 
# if the input string is valid. 

# Validity conditions:
# 1. Open brackets must be closed by the same type of brackets. 
# 2. Open brackets must be closed in the correct order. 

import collections

class Solution:
    def isValid(self, s):
        dct = {"{": "}", "[": "]", "(": ")"}

        q = collections.deque([])
        for elem in s:
            if elem in dct:
                q.appendleft(dct[elem])
            else:
                if (not q) or (elem != q.popleft()):
                    return False

        return not q
    
    def isValidList(self, s):
        dct = {"{": "}", "[": "]", "(": ")"}

        stack = []
        for elem in s:
            if elem in dct:
                stack.append(dct[elem])
            else:
                if (not stack) or (elem != stack.pop()):
                    return False
        
        return not stack


my = Solution()
print(my.isValidList("["))

# This is an important problem for writing parsers,
# a sub-task that goes into checking if a given expression
# is valid or not!

# The fact that we have different types of brackets adds complexity!
# Think about it: we need to keep track of the types of opened/opening
# brackets with their positions relative to each other. If you
# come upon a closing bracket, it is only valid if the closest unmatched
# opening bracket is of the same type!

# Note: if we add closing brackets to the end of a python list
# instead and pop things from the end of the list, we can use less space!
# Remember that popping something from the emd of the list is O(1)
