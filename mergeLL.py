import LL

class Solution:
    """ Given heads of two sorted singly linked lists,
    merge the lists! """
    def mergeTwoLists(self, head1, head2):
        # Recursive approach. Runs in O(n + m) time,
        # O(n + m) space.
        if not head1:
            return head2
        if not head2:
            return head1
        else:
            if head1.val > head2.val:
                head2.next = self.mergeTwoLists(head1, head2.next)
                return head2
            else:
                head1.next = self.mergeTwoLists(head2, head1.next)
                return head1
    
    def mergeIterative(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1

        if head1.val < head2.val:
            output_head = head1
            mainlist = head1
            addlist = head2
        else:
            output_head = head2
            mainlist = head2
            addlist = head1

        while mainlist.next:
            if addlist:
                if addlist.val < mainlist.next.val:
                    # insert addlist head between
                    # mainlist and mainlist.next
                    # proceed with addlist.next and
                    # mainlist
                    temp_mainlist = mainlist.next
                    mainlist.next = addlist
                    new_addlist = addlist.next
                    addlist.next = temp_mainlist

                    addlist = new_addlist
                    mainlist = mainlist.next

                else:

                    mainlist = mainlist.next
                    # proceed with addlist and
                    # mainlist.next
            else:
                return output_head

        if addlist:
            mainlist.next = addlist

        return output_head
            # append whatever is left of endlist

    def MergeIter(self, head1, head2):

        if head1 and head2:
            if head1.val <= head2.val:
                output_head = head1
                head1 = head1.next
            
            else:
                output_head = head2
                head2 = head2.next
        else:
            return head1 if head1 else head2

        cur = output_head
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        
        if head1 or head2:
            cur.next = head1 if head1 else head2
            
        return output_head





if __name__ == "__main__":
    N5 = LL.SLLNode(8)
    N4 = LL.SLLNode(6, N5)
    N3 = LL.SLLNode(4, N4)
    N2 = LL.SLLNode(2, N3)
    N1 = LL.SLLNode(2, N2)
    N0 = LL.SLLNode(0, N1)
    L1 = LL.MySLL()
    L1.head = N0
    L1.prettyPrint()

    N11 = LL.SLLNode(9)
    N10 = LL.SLLNode(7, N11)
    N9 = LL.SLLNode(6, N10)
    N8 = LL.SLLNode(5, N9)
    N7 = LL.SLLNode(3, N8)
    N6 = LL.SLLNode(1, N7)
    L2 = LL.MySLL()
    L2.head = N6
    L2.prettyPrint()

    #import pdb; pdb.set_trace()

    my = Solution()
    #out = my.mergeTwoLists(L1.head, L2.head)
    out1 = my.mergeIterative(L1.head, L2.head)
    outSLL = LL.MySLL()
    outSLL.head = out1
    outSLL.prettyPrint()

    N6 = LL.SLLNode(6)
    N5 = LL.SLLNode(6, N6)
    N4 = LL.SLLNode(1, N5)
    N3 = LL.SLLNode(-4, N4)
    N2 = LL.SLLNode(-9, N3)
    N1 = LL.SLLNode(-10, N2)
    N0 = LL.SLLNode(-10, N1)
    L1 = LL.MySLL()
    L1.head = N0
    L1.prettyPrint()

    L7 = LL.SLLNode(-7)
    L2 = LL.MySLL()
    L2.head = L7
    L2.prettyPrint()

    out2 = my.MergeIter(L1.head, L2.head)
    outSLL = LL.MySLL()
    outSLL.head = out2
    outSLL.prettyPrint()



                
                

