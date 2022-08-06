class DLLNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyDLL():

    def __init__(self):
        self.head = None
        self.tail = None

    def len(self):
        # return length of the list
        # (remember the list is 0-indexed, so
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
            self.head = DLLNode(val)
            self.head.next = prev_head
        else:
            self.head = DNode(val)

    def addAtTail(self, val):
        if self.head:
            # add node at tail
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = DLLNode(val)
        else:
            self.head = DLLNode(val)

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
            cur.next =  DLLNode(val)
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


            print(" < - > ".join(out))
        else:
            print("")


class LRUCache:

    def __init__(self, capacity):
        self.dct = {}
        self.left = capacity
        self.priority = MyDLL()

    def get(self, key):
        try:
            out = self.dct[key]
        
        except KeyError:
            return -1
        
            # now let's find this node in our stack
            # and move it to the top (i. e. end of
            # doubly linked list)
        cur = self.priority.tail
        while cur:
            if cur.val == key:
                if cur == self.priority.tail:
                    cur = None
                else:
                    prv = cur.prev
                    nxt = cur.next

                    # add node to the old tail
                    cur.prev = self.priority.tail
                    self.priority.tail.next = cur
                    cur.next = None
                    # set as the new tail
                    self.priority.tail = cur

                    # shift the other nodes
                    if prv:
                        prv.next = nxt
                    nxt.prev = prv
                    if self.priority.head is cur: 
                        self.priority.head = nxt
            else:
                cur = cur.prev

        return self.dct[key]


        

    def put(self, key, value):
        # the case where key is already in dct,
        # we're just replacing it
        if key in self.dct:
            self.dct[key] = value
            
            # search out the element in the linked list
            cur = self.priority.tail
            if key == self.priority.tail.val:
                return
            else:
                while cur:
                    if cur.val == key:

                        if cur == self.priority.head:
                            if cur != self.priority.tail:
                                self.priority.head = cur.next
                                self.priority.head.prev = None
                                
                        prv = cur.prev
                        nxt = cur.next

                        self.priority.tail.next = cur
                        cur.prev = self.priority.tail
                        self.priority.tail = cur
                        cur.next = None

                        # closing the gap at the previous position
                        # of the element
                        if prv:
                            prv.next = nxt
                        nxt.prev = prv


                        return
                    else:
                        cur = cur.prev

        # the case where value is not already in self.dict:

        # evicting LRU item if dictionary is at capacity
        if self.left == 0:
            LRUNode = self.priority.head
            self.priority.head = LRUNode.next

            if LRUNode.next:
                self.priority.head.prev = None

            del self.dct[LRUNode.val]
            self.left += 1
        
        # putting in the new item
        self.left -= 1

        self.dct[key] = value
        new_head = DLLNode(key)
        
        old_head = self.priority.tail 
        # print(old_head.val)
        self.priority.tail = new_head

        if old_head:
            old_head.next = new_head
            new_head.prev = old_head

        else:
            self.priority.head = self.priority.tail = new_head


        

if __name__ == "__main__":
    """N5 = DLLNode(5)
    N4 = DLLNode(4, N5)
    N3 = DLLNode(3, N4)
    N2 = DLLNode(2, N3)
    N1 = DLLNode(1, N2)
    N0 = DLLNode(0, N1)

    DLL1 = MyDLL()
    DLL1.head = N0
    DLL1.prettyPrint()
    print(DLL1.len())

    MyLRU = LRUCache(2)
    MyLRU.dct = {1: 2, 3 : 4}
    print(MyLRU.dct)
    print(MyLRU.get(1))
    print(MyLRU.get(0))

    obj = LRUCache(2)
    obj.put(1, 2)
    obj.put(3, 4)
    obj.put(5, 6)
    print(obj.dct)
    obj.priority.prettyPrint()
    print(obj.priority.tail.prev.val)
    # import pdb; pdb.set_trace()
    obj.get(3)
    print(obj.priority.tail.val)
    print(obj.dct)
    print("Pretty Print!")
    obj.priority.prettyPrint()"""

    testcase = LRUCache(2)
    print(testcase.put(2, 1))
    print(testcase.put(1, 1))

    print("Dct after first two puts")
    print(testcase.dct)
    print(testcase.priority.head.val)
    print(testcase.priority.tail.val)

    print(testcase.put(2, 3))

    print("Dct after one more put")
    print(testcase.dct)
    print(testcase.priority.head.val)
    print(testcase.priority.tail.val)

    #print(testcase.get(1))
    # import pdb; pdb.set_trace()
    print(testcase.put(4, 1))
    #print(testcase.dct)
    # import pdb; pdb.set_trace()
    #print(testcase.put(1, 2))
    print(testcase.get(1))
    #print(testcase.dct)
    print(testcase.get(2))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)