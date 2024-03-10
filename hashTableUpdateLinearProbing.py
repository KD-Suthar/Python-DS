class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        hash = 0
        for x in key:
            hash += ord(x)
        return hash % self.Max
    
    def __getitem__(self,key):
        hash = self.get_hash(key)

        if self.arr[hash] == None:
            return
        p_range = self.get_probe_range(hash)
        for index in p_range:
            ele = self.arr[index]
            if ele == None:
                return
            if ele[0] == key:
                return ele[1]

    def __setitem__(self,key, val):
        hash = self.get_hash(key)

        if self.arr[hash] ==  None:
            self.arr[hash] = (key,val)
        else:
            new_hash = self.find_loc(key,hash)
            self.arr[new_hash] = (key,val)
        
        print(self.arr)

    def get_probe_range(self, idx):
        return [*range(idx,len(self.arr))] + [*range(0,idx)]
    
    def find_loc(self,key,idx):
        p_range = self.get_probe_range(idx)
        for index in p_range:
            if self.arr[index] == None:
                return index
            if self.arr[index][0] == key:
                return index
        raise Exception("Hash Map is full")
    
    def __delitem__(self,key):
        hash = self.get_hash(key)
        p_range = self.get_prob_range(hash)
        for index in p_range:
            if self.arr[index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[index][0] == key:
                self.arr[index]=None
        print(self.arr)

if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 20
    t["march 17"] =  88
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    print(t["dec 1"])
    print(t["march 33"])
    print(t.arr)