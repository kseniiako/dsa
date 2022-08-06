import LL

class Solution:
    def reorderFalse(self, head):
        # this code works but produces
        # not the intended result. it was written
        # because I misunderstood the assignment.
        if not (head and head.next):
            return head

        # find last index the list
        count = 0
        end = head
        while end.next:
            end = end.next
            count +=1
        
        mid = count//2
        mid_node = head
        find_mid = 0
        while find_mid < mid:
            mid_node = mid_node.next
            find_mid += 1
        
        # now iteratively update the list in place
        # by inserting nodes from the second halg
        cur = head
        cur_insert = mid_node.next
        while cur_insert.next:
            temp = cur.next
            cur.next = cur_insert
            temp_mid = cur_insert.next
            cur_insert.next = temp

            # now reassign variables
            cur = temp
            cur_insert = temp_mid

        cur.next = cur_insert

        return head 
    
    def reorder(self, head):

        dct = {}
        cur = head
        ind = 0
        while cur:
            dct[ind] = cur
            cur = cur.next
            ind += 1
        
        #print([(x, dct[x].val) for x in dct])
        #print(ind)

        mid = ind // 2
        for x in range(ind-1, mid, -1):
            tmp = dct[ind-x-1].next
            dct[ind-x-1].next = dct[x]
            dct[x].next = tmp

        dct[mid].next = None
        return head


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

# import pdb; pdb.set_trace()

out = my.reorder(SLL1.head)
print(out)
SLLout = LL.MySLL()
SLLout.head = out
SLLout.prettyPrint()

"""out = my.reorderFalse(SLL1.head)
SLLout = LL.MySLL()
SLLout.head = out
SLLout.prettyPrint()

SLL2 = LL.MySLL()
SLL2.head = N5
SLL2.prettyPrint()
print(SLL2.len())

out1 = my.reorderFalse(SLL2.head)
SLLout = LL.MySLL()
SLLout.head = out1
SLLout.prettyPrint()"""
