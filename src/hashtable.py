from typing import List

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
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
        self.items = 0
        self.capacity = capacity  # Number of buckets in the hash table
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


    def insert(self, key: str, value: any):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        '''
        hashed_key = self._hash_mod(key)
        linked_list = self.storage[hashed_key]

        if not linked_list:
            self.storage[hashed_key] = LinkedPair(key, value)
            self.items += 1
            if self.items / self.capacity > 0.7:
                self.resize()

        else:
            while linked_list.next and linked_list.key != key:
                linked_list = linked_list.next

            if linked_list.key == key:
                linked_list.value = value
            else:
                linked_list.next = LinkedPair(key, value)

                self.items += 1
                if self.items / self.capacity > 0.7:
                    self.resize()


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
            self.items -= 1
            if self.items / self.capacity < 0.2:
                self.resize(up=False)
            return

        while leading_node and leading_node.next and leading_node.key != key:
            trailing_node = trailing_node.next
            leading_node = leading_node.next

        if leading_node and leading_node.key == key:
            trailing_node.next = leading_node.next if leading_node else None
            self.items -= 1
            if self.items / self.capacity < 0.2:
                self.resize(up=False)
            return

        print("Value not found...")



    def retrieve(self, key: str):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        '''
        hashed_key = self._hash_mod(key)
        linked_list = self.storage[hashed_key]

        while linked_list and linked_list.next and linked_list.key != key:
            linked_list = linked_list.next

        return linked_list.value if  linked_list and linked_list.key == key else None


    def resize(self, up=True):
        '''
        Doubles or Halves the capacity of the hash table and
        rehash all key/value pairs.
        '''
        items: List[LinkedPair] = [*self.storage]
        self.capacity = int(self.capacity * 2 if up else self.capacity // 2)
        self.storage = [None] * self.capacity

        for item in items:
            while item:
                self.insert(item.key, item.value)
                item = item.next






if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
