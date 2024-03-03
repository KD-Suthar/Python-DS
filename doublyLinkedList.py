class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        if self.head is None:
            self.head = Node(None,data,self.head)
        else: 
            node = Node(None,data,self.head)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(None,data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(itr,data,None)
    
    def insert_at(self,data,index):
        if index <0 or index>self.length():
            raise("Invalid Index")
        
        if index == 0:
            self.insert_at_start(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(itr,data,itr.next)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1
    
    def remove_at(self,index):
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        itr = self.head

        while itr :
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            
            itr = itr.next
            count += 1
        
    def insert_val(self,data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)
            

    def length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def print_forward(self):
        if self.head == None:
            print('Link List is Empty')
            return
        
        itr = self.head
        dlist = ''
        while itr:
            dlist += str(itr.data) + '-->'
            itr = itr.next
        
        print('forward_list',dlist)

    def get_last_node(self):

        itr = self.head
        while itr.next:
            itr = itr.next
        
        return itr
    
    def print_backward(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        last_node = self.get_last_node()
        itr = last_node
        dlist = ''
        while itr:
            dlist += str(itr.data) + '-->'
            itr = itr.prev

        print('reveresed_list', dlist)

        

if __name__ == '__main__':
    ll = doublyLinkedList()
    ll.insert_val(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at("jackfruit",0)
    ll.print_forward()
    ll.insert_at("dates",6)
    ll.print_forward()
    ll.insert_at("kiwi",2)
    ll.print_forward()