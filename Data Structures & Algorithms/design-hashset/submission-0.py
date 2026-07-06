class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        # ensure data is large enough to contain the key
        while len(self.data) < key+1:
            self.data.append(0)
        self.data[key] = 1
        
    def remove(self, key: int) -> None:
        if len(self.data) < key+1:
            return
        self.data[key] = 0

    def contains(self, key: int) -> bool:
        if len(self.data) < key+1:
            return False
        return True if self.data[key] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)