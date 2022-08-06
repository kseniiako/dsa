class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 0:
            return [1]
        if len(digits) >= 1:
            incr = digits[-1]+1
            if incr<10:
                digits[-1] = incr
                return digits
            else:
                if len(digits)>1:
                    digits2 = digits[:-1]
                    out = self.plusOne(digits2)
                    out.append(0)
                    return out
                else:
                    return [1, 0]

my = Solution()
print(my.plusOne([1, 2, 9]))