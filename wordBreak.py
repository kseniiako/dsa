# Word Break (Leetcode 139)

# Given a string s and a dictionary of words worddict, return
# true if s can be segmented into a space-separated sequence of
# one or more dictionary words.

class Solution:
    def wordBreakBruteForce(self, s, wordDict):
        # A slow-but-sure brute-force solution
        if s in wordDict:
            return True

        for i in range(0, len(s)):
                if s[:i] in wordDict:
                    remaining = self.wordBreakBruteForce(s[i:], wordDict)
                    if remaining:
                        return True
                
        return False
    
    def wordBreak(self, s, wordDict):
        # Here we go again! An attempt to efficiently and elegantly solve this problem.
        # Instead of checking letter by letter, we will be checking only for possible
        # fits for words in our dictionary: that makes sense from the perspective of time complexity
        # when we compare the string length and dictionary size and think of the numbers of combinatoric
        # possibilities.

        # Solution from Neetcode.

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and \
                s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
            
        return dp[0]

        # Space complexity: O(string_length) to store the dp array.
        # Time complexity: O(string_length * dict_length) to store two nested for loops.
                         
                
if __name__ == "__main__":
    my = Solution()
    print(my.wordBreakBruteForce("leetcode", {"leet","code"}))
    print(my.wordBreakBruteForce("applepenapple", {"apple", "pen"}))
    print(my.wordBreakBruteForce("catsandog", {"cats","dog","sand","and","cat"}))

    print(my.wordBreak("leetcode", {"leet","code"}))
    print(my.wordBreak("applepenapple", {"apple", "pen"}))
    print(my.wordBreak("catsandog", {"cats","dog","sand","and","cat"}))
    print(my.wordBreak("leev", {"leet"}))
    print(my.wordBreak("aaaaaaa", {"aaaa", "aa"}))
    print(my.wordBreak("goalspecial", {"go", "goal", "goals", "special"}))
    print(my.wordBreak("aaaaaaaaaaaaaaab", {"a", "aa", "aaa"}))
    #print(len("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"))
    #print(my.wordBreak("a", {"b"}))
    #print(my.wordBreak("aaaaaab", {"a", "aa"}))
    print(my.wordBreak("aaaaaaaaaaaaaaaaaaaaab",
{"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"}))
    print(my.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
{"aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"}))

    #print(my.wordDictHelper({"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"}))