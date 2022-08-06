# Given a signed 32-bit int, return it with its digits reversed.
# E. g, for 123 return 321. Id reversing x causes the vaslue
# to go outside the signed 32-bit integer range, return 0.

# Constraint: assume the environment does not allow you
# to store 64-bit integers (signed or unsigned). We are
# limited to 32-bit ones.
class Solution:
    def reverseDigits(self, n):

        if n == 0:
            return 0

        if n > 0:

            # first, determine how many digits there are
            power = 1
            temp = n // (10**power)
            while temp != 0:
                power +=1
                temp //= 10

            
            print("Power is: "+str(power))

            i = 1
            out = 0
            while n != 0:
                out += ((n % 10) * (10**(power - i)))
                n //= 10
                i +=1
            
            return out

        else:
            n = -n
            return -self.reverseDigits(n)


my = Solution()
print(my.reverseDigits(123))
print(my.reverseDigits(-123))

#import pdb; pdb.set_trace()
print(my.reverseDigits(651))
print(my.reverseDigits(1))
print(my.reverseDigits(900000))
            
            
