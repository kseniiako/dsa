# Questions from Cracking the Coding Interview

# Problems from "5 algorithm approaches"

# 1. 

# Work from example cases!

# given a time, calculate angle between munute
# and hour hands

def HourMinuteAngle(h, m):
    return h*30 - m*5.5

# return angle in radians

print(HourMinuteAngle(5, 27))

# Pattern Matching

# Consider what problems the algorithm is
# similar to, and figure out if you can
# modify the solution to develop an algorithm
# for this problem.


# A sorted array has been rotated so that the 
# elements appear in the order
# 3 4 5 6 7 1 2. How to find minimum element?

# Use binary search!

# Simplify and generalize!

# Change a constraint to simplify the problem.
# Try to solve it. Once you have algorithm for simpified
# problem, generalize it again.

# Figure out if a ransom note (string)
# Can be formed out of a given magazine (string)

# Create a hash table with words. Each word maps
# to the number of times the word appears. So
# then we can go through the magazine to see
# if we have all of those characters.

# Base case and build

# Often leads to natural recursive algorithms. 

# Us a recursive algorithm. Generate all permutations
# of a string by "chopping off" the last character
# and generating all permutations ofr s[1, ... n-1].
# Then insert s[n] into every location of the string. 

#def allPermutations(s):
#    ls = []
#    if len(s)<=1:
#        ls.append(s)
#        return ls
#    if len(s)==2:
#        ls = ls + [s[0]+s[1], s[1]+s[0]]
#        return ls
#    if len(s)>2:
#        allPermutationshelper(s, ls)
#        return ls

#def allPermutationshelper(s, ls):
#    for x in range(len(s)):
#        st = s[:x]+s[(x+1):]
#        elem = s[x]
#        ls.append(st+elem)
#        for ind in range(len(st)):
#                ls.append(st[:ind]+elem+st[ind:])
#    return ls

def allPermutations(s):
    ls = []
    for x in range(len(s)):
        elem = s[x]
        st = s[:x]+s[(x+1):]
        for y in range(len(st)+1):
            if y == len(st):
                out = st+elem
            else: 
                out = st[:y]+elem+st[y:]
            ls.append(out)
    print(ls)

allPermutations("abc")

# Python program to print all permutations with
# duplicates allowed

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
	if l==r:
		print (toString(a))
	else:
		for i in range(l,r):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n)

# This code is contributed by Bhavya Jain



# Data Structure Brainstorm

# Hacky, but often works! Simply run through
# a list of data structures and try to apply
# each one. 

# Numbers are randomly generated and stored into
# an expanding array. How would you keep track of
# the median?
