# Palindrome Partitioning (Leetcode 131)

# Given a string s, partition s so that every substring of
# the partition is a palindrome. Return all possible palindrome
# partitionings of s.

class Solution:

    def palindromePartitioning(self, s):
        output = []
        partition = []

        # function to check if a given string is a palindrome.
        def isPalindrome(left, right):
            if left > right:
                return False
            if left == right:
                return True

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # depth-first search to perform backtracking
        def dfs(ind):
            # once we've composed the whole string as a sequence
            # of palindromes, add it to output
            if ind >= len(s):
                # don't forget to hard copy the new element to the
                # output to avoid changing it in place as you backtrack!
                output.append(list(partition))
                return
            # if we haven't reached the end of the string yet, then
            # continue looking for options depth-first
            for j in range(ind, len(s)):
                # as we find a valid palindrome starting with index ind
                # and ending with index j...
                if isPalindrome(ind, j):
                    # we do a search with that palindrome added to a result
                    # option
                    partition.append(s[ind : j+1])
                    dfs(j + 1)
                    # as well as backtrack and continue searching for options without
                    # this palindrome (with some other palindrome starting with ind
                    # instead, or no other options — search at this stage is exhausted.)
                    partition.pop()

        # start depth-first search at the first index
        dfs(0)

        # return a collection of all possible options!
        return output

        # Space complexity: O(n), where n us the length of the string s. This
        # is the space needed for the recursion stack/function call stack.

        # Time complexity: O(n * 2^n), where n is the length of the string s. This
        # is the worst-case time complexity where all the possible substrings
        # are palindromes (id est, the string contains just one letter repeated many
        # times). If we look at the recursive tree for this case, it was 2^n total
        # nodes (2^n possible substrings). For each substring, it takes O(n) time to
        # generate substring and determing if it is a palindrome or not. This gives us
        # time complexity O(n*2^n).
        

if __name__ == "__main__":
    my = Solution()
    print(my.palindromePartitioning("aab"))
    print(my.palindromePartitioning("a"))


