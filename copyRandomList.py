# A linked list of length n is given such that each node contains
# an additional random pointer, which could point to any node in
# the list, or null.

# construct a deep copy of the list.

import LL

class Solution():
    # copy a linked list with random pointers
    def copySLL(self, head):

        if not head:
            return head

        # let's first try and make a deep copy of
        # a regular singly linked list

        node = LL.SLLNode(head.val)
        node.next = my.copySLL(head.next)

        return node
    
    def copySLLIter(self, head):


        cur = head
        newList = None
        tail = None
        
        while cur:
            if newList is None:
                newList = LL.SLLNode(cur.val, None)
                tail = newList
            else:
                tail.next = LL.SLLNode()
                tail = tail.next
                tail.val = cur.val
                tail.next = None
            cur = cur.next

        return newList

    def copyListPush(self, head):
        # a sleeker looking solution that allows us to 
        # reduce code length

        cur = head
        newList = None
        tail = None

        while cur:

            if not newList:
                newList = LL.SLLNode(cur.val, newList)
                tail = newList
            else:
                tail.next = LL.SLLNode(cur.val, tail.next)
                tail = tail.next
            cur = cur.next
            
        return newList

    def copyListSentinel(self, head):
        # yet one move way to deep-copy a singly linked list
        # here we have a sentinel node to deal with the first
        # node case.

        cur = head
        sent = LL.SLLNode()

        tail = sent

        while cur:
            tail.next = LL.SLLNode(cur.val, tail.next)
            tail = tail.next
            cur = cur.next
        
        return sent.next



    def copyRandomSLL(self, head):

        dct_correspondence = {}
        dct_back = {}
        dct_randoms = {}

        cur = head
        tail = None
        newList = None
        
        while cur:
            if not newList:
                newList = LL.SLLNode(cur.val, newList)
                tail = newList

            else:
                tail.next = LL.SLLNode(cur.val, tail.next)
                tail = tail.next

            dct_correspondence[tail] = cur
            dct_back[cur] = tail
            dct_randoms[cur] = cur.random
            cur = cur.next

        cur = newList
        while cur:
            correspondence = dct_correspondence[cur]
            if dct_randoms[correspondence]:
                cur.random = dct_back[dct_randoms[correspondence]]
            else:
                cur.random = None
            cur = cur.next
        
            

        #print(dct)
        return newList
    
    def copyRandomSLL1Dict(self, head):

        # an approach that uses (wowza!) one dictionary
        # instead of three

        dct = {}

        cur = head
        tail = None
        newList = None
        
        while cur:
            if not newList:
                newList = LL.SLLNode(cur.val, newList)
                tail = newList

            else:
                tail.next = LL.SLLNode(cur.val, tail.next)
                tail = tail.next

            dct[(cur, tail)] = cur.random

        cur = newList
        while cur:
            correspondence = dct_correspondence[cur]
            if dct_randoms[correspondence]:
                cur.random = dct_back[dct_randoms[correspondence]]
            else:
                cur.random = None
            cur = cur.next
        
            

        #print(dct)
        return newList
        

N5 = LL.SLLNode(5, None, None)
N4 = LL.SLLNode(4, N5, None)
N3 = LL.SLLNode(3, N4, N5)
N2 = LL.SLLNode(2, N3, N4)
N1 = LL.SLLNode(1, N2, N3)
N0 = LL.SLLNode(0, N1, N2)

SLL1 = LL.MySLL()
SLL1.head = N0
SLL1.prettyPrint()
print(SLL1.len())

my = Solution()
out = my.copyRandomSLL(SLL1.head)

SLLout = LL.MySLL()
SLLout.head = out

print(SLLout.head.next)
print(SLL1.head.next)
SLLout.prettyPrint()

