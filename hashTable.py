"""This particular HashMap function does not handle the collision of Key 
    To handle that please check hashTableUpdate.py in same repo"""
class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr = [None for i in range(self.MAX)]

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
        self.arr[h] = value
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    table = HashTable()

    """table.add('march 6',320)
    print(table.get('march 6'))"""
    table['march 9'] = 190
    table['march 20'] = 290
    print(table.arr)
    del table['march 9']
    print(table.arr)
    print(table['march 20'])
