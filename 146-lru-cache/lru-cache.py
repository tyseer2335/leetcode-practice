class DoublyLinkedList:
    def __init__(self, val, key, prev, next):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Sentinels: Least Recently Used (LRU) <-> Most Recently Used (MRU)
        self.LRU = DoublyLinkedList("LRU", None, None, None)
        self.MRU = DoublyLinkedList("MRU", None, None, None)

        # Connect sentinels together
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

        # Dictionary: key -> node
        self.data = {}

    def get(self, key: int) -> int:
        """Return the value for a given key and move it to the MRU position."""
        if key not in self.data:
            return -1

        node = self.data[key]

        # Remove node from its current position
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

        # Insert node before MRU sentinel (move to end)
        self.MRU.prev.next = node
        node.prev = self.MRU.prev
        node.next = self.MRU
        self.MRU.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        """Insert or update the key-value pair in the cache."""

        # Key already exists -> update value & move to MRU
        if key in self.data:
            node = self.data[key]
            node.val = value

            # Remove from current position
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

            # Add to MRU end
            self.MRU.prev.next = node
            node.prev = self.MRU.prev
            node.next = self.MRU
            self.MRU.prev = node
            return

        # Cache full -> evict LRU node
        if len(self.data) + 1 > self.capacity:
            lru = self.LRU.next
            del self.data[lru.key]

            # Unlink the LRU node
            self.LRU.next = lru.next
            self.LRU.next.prev = self.LRU

        # Insert new node at MRU position
        new_node = DoublyLinkedList(value, key, None, None)
        self.MRU.prev.next = new_node
        new_node.prev = self.MRU.prev
        new_node.next = self.MRU
        self.MRU.prev = new_node

        # Track in dictionary
        self.data[key] = new_node


# NOTE: What messed me up was the pointer shifting when we had to remove and add from a Doubly Linked List, need to be 
# very careful since pointers shift and the old ones arent the same as new ie ORDER MATTERS 
# Dont use parelell assignment and draw it out 

# Time Taken: Too long 
# Time Complexity: 
# - get() -> O(1) 
# - put() -> O(1) 
# Space Complexty: O(n)
