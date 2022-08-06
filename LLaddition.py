# Leetcode 2

import LL

class Solution():
    
    def addNumbers(self, head1, head2):
        cur1 = head1
        cur2 = head2
        out_head = head1

        carryover = 0
        prev = None
        while cur1 or cur2:
            if not cur1:
                cur1 = LL.SLLNode(0)
                prev.next = cur1
            if not cur2:
                cur2 = LL.SLLNode(0)

            values = divmod(cur1.val+cur2.val+carryover, 10)
            cur1.val = values[1]
            carryover = values[0]

            prev = cur1
            cur1, cur2 = cur1.next, cur2.next
            #prev.next = cur1
        
        if carryover:
            cur1 = LL.SLLNode(carryover)
            prev.next = cur1

        return out_head

#N3 = LL.SLLNode(9)
N2 = LL.SLLNode(9)
N1 = LL.SLLNode(4, N2)
N0 = LL.SLLNode(2, N1)

N7 = LL.SLLNode(9)
N6 = LL.SLLNode(4, N7)
N5 = LL.SLLNode(6, N6)
N4 = LL.SLLNode(5, N5)
    
SLL1 = LL.MySLL()
SLL1.head = N0
SLL1.prettyPrint()
print(SLL1.len())

SLL2 = LL.MySLL()
SLL2.head = N4
SLL2.prettyPrint()
print(SLL2.len())

my = Solution()
out = my.addNumbers(SLL1.head, SLL2.head)
SLLout = LL.MySLL()
SLLout.head = out
SLLout.prettyPrint()