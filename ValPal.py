# A string is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. 

# Given string s, return true if it is a palindrome, false
# otherwise.
zero_ord = 48
nine_ord = 57
A_ord = 65
Z_ord = 90
a_ord = 97
z_ord = 122

# The idea is going inwards towards the middle and checking that
# all characters are the same.

class Solution:
    def ValPal(self, s):
        front = 0
        back = len(s) - 1

        while front < back:

            while front < back and not s[front].isalnum():
                front += 1

            while front < back and not s[back].isalnum():
                back -= 1
                
            if s[front].lower() != s[back].lower():
                return False
            
            front += 1
            back -= 1
            
        return True


my = Solution()
print(my.ValPal("9"))
print(my.ValPal("A man, a plan, a canal: Panama"))
print(my.ValPal("race a car"))
print(my.ValPal(""))
print(my.ValPal(".,"))

# ord(a) is 97
# ord(z) is 122
# ord(A) is 65
# ord(Z) is 90
# ord(0) is 48
# ord(9) is 57

# Takeaway: .isalnum(), .lower() are powerful methods which
# should be used! Generally, there are so many methods and
# API nuances/possibilities when working with strings!

# Always keep in mind: are we allowed to modify the input?

# Terms/thoughts: loop termination condition, loop invariant,
# string [::1]
