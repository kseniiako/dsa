# Remove n-th node from the end of a singly linked list
import LL

class Solution:
    def removefromend(self, head, n):
        cur = head
        dct = {}
        ind = 0
        while cur.next:
            dct[ind] = cur
            cur = cur.next
            ind += 1
        
        print(dct)
        print(ind)

        if n == 1:
            if dct:
                dct[ind - 1].next = None
                return head
            else:
                return None

        if (ind - n) < -1:
            print("Invalid index!")

        if (ind - n) >= 0:
            dct[ind - n].next = dct[ind - n + 1].next

        if (ind - n) == -1:
            head = head.next

        return head
    
    # practicing the second solution from leetcode article +
    # practicing using a dummy node
    def secondApproach(self, head, n):
        dummy = LL.SLLNode(None)
        dummy.next = head
        cur1 = cur2 = dummy

        # first pointer starts moving at first node,
        # second pointer needs to start at n+1th node

        for _ in range(n+1):

            if not cur2:
                raise IndexError("This index is invalid! Index should be within [1, n], where n is listg length")

            cur2 = cur2.next
        
        while cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        
        if cur1.next == head:
            head = head.next
        else:
            cur1.next = cur1.next.next


        return head

        

#N5 = LL.SLLNode(5)
#N4 = LL.SLLNode(5)
#N3 = LL.SLLNode(4, N4)
#N2 = LL.SLLNode(3)
N1 = LL.SLLNode(2)
N0 = LL.SLLNode(1, N1)

SLL1 = LL.MySLL()
SLL1.head = N0
SLL1.prettyPrint()
print(SLL1.len())

my = Solution()

# import pdb; pdb.set_trace()

out = my.secondApproach(SLL1.head, 2)
#out = my.removefromend(SLL1.head, 2)
print(out)
SLL1.head = out
SLL1.prettyPrint()