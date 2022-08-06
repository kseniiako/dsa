# Checking if I've learnt to reverse linked lists well!

class Solution():
    def revLL(self, head):

        cur = head
        prev = None

        while cur:
            next_tmp = cur.next
            cur.next = prev
            prev = cur
            cur = next_tmp
        
        return prev

    
import LL


N5 = LL.SLLNode(5)
N4 = LL.SLLNode(4, N5)
N3 = LL.SLLNode(3, N4)
N2 = LL.SLLNode(2, N3)
N1 = LL.SLLNode(1, N2)
N0 = LL.SLLNode(0, N1)

SLL1 = LL.MySLL()
SLL1.head = N0
SLL1.prettyPrint()
print(SLL1.len())

my = Solution()
out_head = my.revLL(SLL1.head)
print(out_head.val)

SLLout = LL.MySLL()
SLLout.head = out_head

SLLout.prettyPrint()