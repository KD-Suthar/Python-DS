#defining the node of the linkedlist which has 2 parts data and the address of the next node

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

#Defining the LinkedList and some functionalities of the Linked List 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):

        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data,None)
        itr.next = node
    
    def insert_val(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    
    def remove_at(self,index):
        if index<0 or index>=self.length():
            raise ("Invalid Index")
            return
        
        if index == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1 :
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, val):
        if index<0 or index>=self.length():
            raise ("Invalid Index")
            return
        
        if index == 0:
            self.insert_at_start(val)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(val,itr.next)
                itr.next = node
                break 
            itr = itr.next
            count += 1

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return 
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return 
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def remove_by_value(self,data):
        if self.head is None:
            print("Link List is empty")
            return 
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr=self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr= itr.next
            


    def length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count


    def print(self):
        if self.head is None:
            print('Linked List has no elements')
        
        itr = self.head
        linked_list = ''

        while itr:
            linked_list += str(itr.data) + " --> "
            itr= itr.next
        print(linked_list)


#let's start with the main function

if __name__ == '__main__':
    
    """ data = [1,2,3,4,5,"mango"]
    ll = LinkedList()
    ll.insert_val(data)
    ll.print()
    ll.insert_at(2,"apple")
    ll.print()
    print(f'Length of the Linked List is - ',ll.length())
    ll.remove_at(0)
    ll.print()
    print(f'Length of the Linked List is - ',ll.length())
    ll.remove_at(2)
    ll.print()
    print(f'Length of the Linked List is - ',ll.length())


    llist = LinkedList()
    llist.insert_at_end(2)
    llist.insert_at_start(3)
    llist.insert_at_start(4)
    llist.insert_at_end(6)
    print(llist.length())
    llist.print()
    """

    ll_test = LinkedList()
    ll_test.insert_val(["banana","mango","grapes","orange"])
    ll_test.print()
    ll_test.insert_after_value("mango","apple") # insert apple after mango
    ll_test.print()
    ll_test.remove_by_value("orange") # remove orange from linked list
    ll_test.print()
    ll_test.remove_by_value("figs")
    ll_test.print()
    ll_test.remove_by_value("banana")
    ll_test.remove_by_value("mango")
    ll_test.remove_by_value("apple")
    ll_test.remove_by_value("grapes")
    ll_test.print()