def groupAnagrams_helper(str):
    charcount= [0] * 26
    for x in str:
        charcount[ord(x)-ord('a')]+=1
    # make immutable for hashing
    charcount = tuple(charcount)
    return charcount
            
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dct = {}
        for x in strs:
            x_tpl = groupAnagrams_helper(x)

            if x_tpl in dct:
                dct[x_tpl].append(x)
            else:
                dct[x_tpl] = [x]
                
        output = []
        for elem in dct:
            output.append(dct[elem])
        return output

my = Solution()
print(my.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Just a little playing around figuring out what would work
# for reverse iteration over list elements (with the purpose
# of running a dynamic programming algorithm where appending 
# front element to a list is O(n) and appending element to back
# is O(1) amortized).

l1 = ['a', 'b', 'c', 'd', 'e']
for i in range(len(l1)-1, -1, -1):
    print(l1[i])

# Takeaway: I had a lot of problems because I tried to 
# implicitly hash dictionaries! And that's not possible (unless
# you make dictionaries hashable -> for which you'd have to make them
# immutable unless you want bugs)