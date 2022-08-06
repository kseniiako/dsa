class SLLNode:
    """ Node for a singly linked list """
    def __init__(self, value = None, nxt = None, random = None):
        # initialize node of a singly linked list
        self.val = value
        self.next = nxt
        self.random = random

class MySLL:
    """ My implementation of a singly linked list """
    def __init__(self):
        # initialize singly linked list
        self.head = None

    def len(self):
        # return length of the list
        # (remeber the list is 0-indexed, so
        # length is last index + 1)
            cur = self.head
            count = 0
            while cur != None:
                cur = cur.next
                count += 1
            return count

    def get(self, index):
        # get the value of node by index 
        # (list is zero-indexed)

        if self.len() - 1 < index:
            return -1

        cur = self.head
        count = 0
        while count < index:
            cur = cur.next
            count += 1
        return cur
    
    def addAtHead(self, val):
        # add node at head
        if self.head:
            prev_head = self.head
            self.head = SLLNode(val)
            self.head.next = prev_head
        else:
            self.head = SLLNode(val)

    def addAtTail(self, val):
        if self.head:
            # add node at tail
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = SLLNode(val)
        else:
            self.head = SLLNode(val)

    def addAtIndex(self, index, val):
        # add node at given index     
        # (list is zero-indexed)
        if index == 0:
            return self.addAtHead(val)

        if self.len() == index:
            return self.addAtTail(val)

        if self.len() < index: 
            return -1
            
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            nxt = cur.next
            cur.next =  SLLNode(val)
            cur.next.next = nxt

    def deleteAtIndex(self, index):
        # delete the node at given index
        if self.len() - 1 < index:
            return -1

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            count = 0
            while count < (index - 1):
                cur = cur.next
                count += 1
            if cur.next: 
                cur.next = cur.next.next
            else:
                cur = None
    
    def prettyPrint(self):
        # pretty-print the linked list with
        # arrows -> between nodes
        # (e. g. "1 -> 2 -> 3")
        if self.head:
            cur = self.head
            out = []
            # out.append(str(cur.val)+" "+str(cur.random)) option for randoms
            out.append(str(cur.val))

            while cur.next != None:
                cur = cur.next
                # out.append(str(cur.val)+" "+str(cur.random)) option for randoms
                out.append(str(cur.val))


            print(" - > ".join(out))
        else:
            print("")

            

# testing
if __name__ == "__main__":
    """ N5 = SLLNode(5)
    N4 = SLLNode(4, N5)
    N3 = SLLNode(3, N4)
    N2 = SLLNode(2, N3)
    N1 = SLLNode(1, N2)
    N0 = SLLNode(0, N1)

    SLL1 = MySLL()
    SLL1.head = N0
    SLL1.prettyPrint()
    print(SLL1.len())

    SLL1.addAtHead(8)
    print(SLL1.len())
    SLL1.prettyPrint()

    SLL1.addAtTail(128)
    SLL1.prettyPrint()
    print(SLL1.len())

    SLL1.addAtIndex(3, 129)
    SLL1.prettyPrint()

    SLL1.deleteAtIndex(3)
    SLL1.prettyPrint()

    print(SLL1.get(3).val)
    print(SLL1.get(0).val)
    print(SLL1.get((SLL1.len() - 1)).val)

    print("Trying to delete at index 0: works!")
    SLL1.deleteAtIndex(0)
    SLL1.prettyPrint()

    print("Trying to delete at the last index: works!")
    SLL1.deleteAtIndex(SLL1.len() - 1)
    SLL1.prettyPrint()


    SLL2 = MySLL()
    SLL2.addAtHead(1)
    SLL2.prettyPrint()
    SLL2.deleteAtIndex(0)
    SLL2.prettyPrint() """

    """SLL3 = MySLL()
    SLL3.addAtHead(7)
    SLL3.addAtHead(2)
    SLL3.addAtHead(1)
    SLL3.prettyPrint()
    print(SLL3.len())
    print("Trying to add at the tail: " + str(SLL3.addAtIndex(3, 5)))
    SLL3.prettyPrint()
    SLL3.deleteAtIndex(2)
    SLL3.addAtHead(6)
    SLL3.addAtTail(4)
    SLL3.prettyPrint()
    print(SLL3.get(4))""" 

    SLL4 = MySLL()
    SLL4.addAtIndex(0, 10)
    SLL4.prettyPrint()
    SLL4.addAtIndex(0, 20)
    SLL4.prettyPrint()
    SLL4.addAtIndex(0, 30)
    SLL4.prettyPrint()
    print(SLL4.get(0).val)




        


    