# Given the head of a singly linked list,
# reverse the list

import LL

#import pdb; pdb.set_trace()

class Solution:
    def reverseList(self, head):
        if head:
            cur = head
            nxt = cur.next
            cur.next = None
            prev = None
            while nxt:
                prev = cur
                cur = nxt
                nxt = nxt.next
                cur.next = prev
            return cur
        else:
            return head

if __name__ == "__main__":
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
    out = my.reverseList(SLL1.head)

    SLLout = LL.MySLL()
    SLLout.head = out
    SLLout.prettyPrint()
    
    print("Empty test case: ")
    out1 = my.reverseList(None)
    SLLout1 = LL.MySLL()
    SLLout1.head = out1
    SLLout1.prettyPrint()

    print("One elem-long test case: ")
    out2 = my.reverseList(N0)
    SLLout2 = LL.MySLL()
    SLLout2.head = out2
    SLLout2.prettyPrint()