# Decode Ways (LC 91)

# A message containing letters from A-Z can be encoded
# into numbers using the following mapping: A -> 1, B -> 2,
# Z -> 26.

# To decode an encoded message, all digits must be grouped
# (e. g. is 12 a 12 (L) or a 1 and a 2 (A, B)?) and then mapped 
# back into letters.

# Given an string s of digits, return the number of ways
# to decode it.

# Any digit except for 0 can represent a letter by itself.
# Digits 1 and 2 can represent the first digit in a letter code,
# where the second digit is any digit for 1 and a digit < 7 for 2.


class Solution:
    def numDecodings(self, s):
        if not s or s[0] == "0":
            return 0

        # create a dynamic programming array, populate
        # with default values
        dp = [-1 for each in s]

        # set the beginning value for first element
        # from the end
        if s[-1] == "0":
            dp[-1] = 0
        else:
            dp[-1] = 1

        # iterate backwards through all elements in the array,
        # setting correct values
        for i in range(len(s)-2, -1, -1):
            
            # only set value where it has not already been determined
            # (where the default value is still present)
            if dp[i] == -1:

                # account for the fact that encountering 0
                # limits our number of options
                if s[i] == "0":
                    if s[i-1] == "1" or s[i-1] == "2":
                        dp[i] = dp[i-1] = dp[i-2] = dp[i+1]
                    # a zero following a number other than 1 or 2 is a
                    # signal that no valid encoding exists, so we immediately
                    # return 0
                    else:
                        return 0
                
                # account for the fact that 1 can be a beginning
                # of a two-digit letter code. if 1 is the second from
                # last number, we have 1 + dp[last] number of encodings.
                # if 1 is further into the array, it is the sum of dp[i+1]
                # and dp[i+2]
                elif s[i] == "1":
                    if i == (len(s)-2):
                        dp[i] = 1 + dp[i+1]
                    else:
                        dp[i] = dp[i+1] + dp[i+2]
                
                # account for the fact that 2 can be a beginning
                # of a two-digit letter code
                elif s[i] == "2" and s[i+1] < "7":
                    if i == (len(s)-2):
                        dp[i] = 1 + dp[i+1]
                    else:
                        dp[i] = dp[i+1] + dp[i+2]

                # if none of these special cases apply, the current number 
                # of encodings is the same as it was at the previous index
                else:
                    dp[i] = dp[i+1]

        # return the number of encodings after the whole array is traversed
        return dp[0]

    def numDecodings2(self, s):
        # A sleeker, shorter solution from Neetcode

        # Dictionary: a smart solution to not worry about
        # default value selection. Moreover, we set "nonexistent"
        # value at (last index + 1) to 1 so that we can perform
        # dp[i] += dp[i+2] without worrying about reaching a nonexistent
        # position in the array. It makes sense since 1 is the "default"
        # number of options we suppose exists for a string encoding, and 
        # this algorithm is designed to handle other, particular cases.
        dp = {len(s): 1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if i+1 < len(s) and \
                (s[i] == "1" or (s[i] == "2" and s[i+1] < "7")):
                dp[i] += dp[i+2]

        return dp[0]

        # The logic behind this approach is as follows:
        # for most elements, dp[i] = dp[i+1]. When we encounter
        # a 0, we set dp[i] to 0 (in case the number before 0 is
        # invalid for a two-digit code). However, when we encounter
        # 1 or 2 (with a valid element following two), we add
        # an extra set of possibilities (encoding options at dp[i+2])
        # to the currently available encoding options dp[i+1]. This is
        # because a grouping starting with 1 or 2 can contain 1 or 2
        # digits. This maneuver returns dp[i] to the pre-zero value dp[i+2]
        # in case a 0 follows 1 or 2: in this situation, only one grouping
        # is possible.

    # Both solutions have O(n) runtime (one pass over the array)
    # and use O(n) space (to store the dp array).

    def numDecodingsMemo(self, s):
        # A top-down approach using memoization
        dp = {len(s) : 1}

        def dfs(i):
            # Base cases: return 0 for 0,
            # existing value if it is present.
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i+1)
            if (i + 1 < len(s) and (s[i] == "1" or \
                (s[i] == "2" and s[i+1]<="6"))):
                res += dfs(i+2)
            
            dp[i] = res
            return res
        
        return dfs(0)

        # O(n) time, O(n) space — just a slightly different
        # logic for getting from intermediate to final result.

    def numDecodingsFin(self, s):
        # This is a variation on the dynamic programming approach
        # that uses O(1) space for a constant number of values instead
        # of O(n) space for an n-sized array.

        # From the previous solutions it is obvious that we only need to
        # keep track of values dp[i+1] and dp[i+2] at index i: one and two steps
        # to the right of current value. So we initialize two variables to
        # hold that data, and avoid allocating a whole array.

        oneStep = twoSteps = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                cur = 0
            else:
                cur = oneStep
            
            if (i < len(s) - 1) and (s[i] == "1" \
                or (s[i] == "2" and s[i+1] <= "6")):
                cur += twoSteps

            oneStep, twoSteps = cur, oneStep
        
        return oneStep

            


if __name__ == "__main__":
    my = Solution()

    print(my.numDecodings("12"))
    print(my.numDecodings("226"))
    print(my.numDecodings("06"))
    print(my.numDecodings("2101"))
    print(my.numDecodings("10"))

    print(my.numDecodings2("12"))
    print(my.numDecodings2("226"))
    print(my.numDecodings2("06"))
    print(my.numDecodings2("2101"))
    print(my.numDecodings2("10"))

    print(my.numDecodingsMemo("12"))
    print(my.numDecodingsMemo("226"))
    print(my.numDecodingsMemo("06"))
    print(my.numDecodingsMemo("2101"))
    print(my.numDecodingsMemo("10"))

    print(my.numDecodingsFin("12"))
    print(my.numDecodingsFin("226"))
    print(my.numDecodingsFin("06"))
    print(my.numDecodingsFin("2101"))
    print(my.numDecodingsFin("10"))
            