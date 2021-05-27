from typing import List


class LinkedPair:
    '''
    Linked List hash table key/value pair
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.initial_capacity = capacity
        self.storage: List[LinkedPair] = [None] * capacity

    def _hash(self, key: str):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key: str):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key: str):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def _change_length(self, size: int):
        self.length += size

        if self.length / self.capacity <= 0.2 and size < 0 and self.capacity > self.initial_capacity:
            self.resize(up=False)

        if self.length / self.capacity >= 0.7 and size > 0:
            self.resize(up=True)

    def insert(self, key: str, value: any):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        '''
        hashed_key = self._hash_mod(key)
        node = self.storage[hashed_key]

        if node:
            while node.next and node.key != key:
                node = node.next

            if node.key == key:
                node.value = value
            else:
                node.next = LinkedPair(key, value)
                self._change_length(1)
        else:
            self.storage[hashed_key] = LinkedPair(key, value)
            self._change_length(1)

    def remove(self, key: str):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        '''
        hashed_key = self._hash_mod(key)
        trailing_node = self.storage[hashed_key]
        leading_node = trailing_node.next

        if trailing_node and trailing_node.key == key:
            self.storage[hashed_key] = trailing_node.next
            self._change_length(-1)
            return

        while leading_node and leading_node.next and leading_node.key != key:
            trailing_node = trailing_node.next
            leading_node = leading_node.next

        if leading_node and leading_node.key == key:
            trailing_node.next = leading_node.next if leading_node else None
            self._change_length(-1)
            return

        print("Value not found...")

    def retrieve(self, key: str):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        '''
        hashed_key = self._hash_mod(key)
        node = self.storage[hashed_key]

        while node and node.next and node.key != key:
            node = node.next

        return node.value if node and node.key == key else None

    def resize(self, up=True):
        '''
        Doubles or Halves the capacity of the hash table and
        rehash all key/value pairs.
        '''
        items: List[LinkedPair] = [*self.storage]
        self.capacity = int(self.capacity * 2 if up else self.capacity // 2)
        self.storage = [None] * self.capacity
        self.length = 0

        for item in items:
            while item:
                self.insert(item.key, item.value)
                item = item.next


if __name__ == "__main__":
    ht = HashTable(2)

    old_capacity = len(ht.storage)
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing

    new_capacity = len(ht.storage)
    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
