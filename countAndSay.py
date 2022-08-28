# Count and Say (Leetcode 38)

class Solution:
    def countAndSay(self, n):

        def countAndSayHelper(st):
            output = ""
            start = 0
            finish = 0
            while finish < len(st):
                while finish < len(st)-1 and \
                st[finish + 1] == st[finish]:
                    finish += 1
                output += str(1 + finish - start)
                output += st[start]
                finish += 1
                start = finish
            return output

        if n == 1:
            return "1"
        else:
            output = "1"
            for _ in range(n - 1):
                output = countAndSayHelper(output)
        return(output)

if __name__ == "__main__":
    my = Solution()
    print(my.countAndSay(1))
    print(my.countAndSay(2))
    print(my.countAndSay(3))
    print(my.countAndSay(4))