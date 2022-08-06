# given a string s, find the length of the longest
# substring w/o repeating characters. 

class Solution:
    def lengthOfLongestSubstring(self, string):
        current_start = 0
        current_end = 0
        max_length = 0
        dct = {}

        for ind, elem in enumerate(string):
            if elem in dct and dct[elem] >= current_start:
                current_start = dct[elem] + 1

            current_end = ind
            dct[elem] = ind

            # print(string[current_start:current_end+1])

            max_length = max(max_length, (current_end - current_start + 1))

        
        return max_length



s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "dvdf"
s5 = "tmmzuxt"
s6 = "bbtablud"

my = Solution()

print(my.lengthOfLongestSubstring(s1))
print(my.lengthOfLongestSubstring(s2))
print(my.lengthOfLongestSubstring(s3))
print(my.lengthOfLongestSubstring(s4))
# import pdb; pdb.set_trace()
print(my.lengthOfLongestSubstring(s5))
print(my.lengthOfLongestSubstring(s6))
            


