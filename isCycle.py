import LL

class Solution:
    def hasCycle(self, head):
        """ Detect a cycle in a linked list: return True (if cycle found)
        or false """
        if head is None:
            return False
        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


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

#import pdb; pdb.set_trace()
print(my.hasCycle(SLL1.head))

    
