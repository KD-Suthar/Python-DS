"""This HashMap function handle the collision of Key. 
    To check the classic implementation of the Hash Table please check hashTable.py in same repo
    To solve the collision problem we will be exploring 2 methods
    1. chaining -> where val are stored in key value pair and in form of linklist
    2. linear probing -> it goes to the next empty index and assign the value to that """

class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for x in key:
            h += ord(x)
        return h % self.MAX
    
    """def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None        """
    
    #Using python operator [getitem, setitem and delitem] so have a functionality like dict in python
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        flag = False
        for idx, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[h][idx] = (key,value)
                flag = True
                break
        
        if not flag:
            self.arr[h].append((key,value))
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx, ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][idx]

if __name__ == '__main__':
    table = HashTable()

    """table.add('march 6',320)
    print(table.get('march 6'))"""
    print(table.get_hash('march 6'),table.get_hash('march 17'))
    table['march 6'] = 190
    table['march 20'] = 290
    table['march 17'] = 240
    print(table.arr)
    #del table['march 9']
    print(table['march 17'])
    print(table['march 6'])
    del table['march 17']
    print(table.arr)
