# use linked list with hashed buckets
class listNode:
    def __init__(self, key=0, value=0):
        self.value = value
        self.key = key
        self.next = None

class MyHashMap:

    def __init__(self):
        # initialize map with 10000 indices to store linked lists
        self.map = [None] * 10000

    def put(self, key: int, value: int) -> None:
        # hash the key
        hashed_key = key % 10000
        new_node = listNode(key, value)
        if not self.map[hashed_key]:
            self.map[hashed_key] = new_node
        else:
            cur = self.map[hashed_key]
            if cur.key == key:
                cur.value = value
                return
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def get(self, key: int) -> int:
        hashed_key = key % 10000
        if not self.map[hashed_key]: return -1
        cur = self.map[hashed_key]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        hashed_key = key % 10000
        if not self.map[hashed_key]: return
        cur = self.map[hashed_key]
        if cur.key == key:
            self.map[hashed_key] = cur.next
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)