class MyHashSet:

    def __init__(self):
        self.size = 10_000
        self.table = [[] for _ in range(self.size)]
        

    def _hash(self, key):
        return hash(key) % self.size 

    def add(self, key: int) -> None:
        bucket =self. _hash(key)
        if key not in self.table[bucket]: 
            self.table[bucket].append(key)
        

    def remove(self, key: int) -> None:
        bucket = self._hash(key)
        if key in self.table[bucket]: 
            self.table[bucket].remove(key)
        

    def contains(self, key: int) -> bool:
        bucket = self._hash(key)
        return key in self.table[bucket]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)