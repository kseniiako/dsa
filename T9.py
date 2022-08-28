# Letter Combinations of a Phone Number (Leetcode 17)

class Solution:
    def letterCombinations(self, digits):
        mapping = {"2" : "abc", "3" : "def",
        "4" : "ghi", "5" : "jkl", "6" : "mno",
        "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
    
        output = []
        if digits == "":
            return output
        
        target_len = len(digits)

        def backtrack(i, cur):
            if i == target_len:
                output.append(cur)
                return

            for letter in mapping[digits[i]]:
                backtrack(i+1, cur+letter)

        backtrack(0, "")

        return output
            

if __name__ == "__main__":
    my = Solution()
    print(my.letterCombinations("23"))