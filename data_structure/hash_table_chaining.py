"""
# SOLVING COLLISION HANDLING IN HASHED MAP using CHAINING

Problem happened when the hashed function returned the same hashed value (index)
from different key. This is called collision, where 2 or more key
share the same index.

Solution:
1. Seperate chaining - Using link list on those same memory allocated.
2. Linear probing (search) - linearly probing through all memory than can allocate
the index when collision happened.
"""


class HashTable:
    def __init__(self):
        self.MAX = 50
        self.arr = [
            [] for i in range(self.MAX)
        ]  # change None to [] changed the behaviour

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  # ord() - find ascii value within ascii table
        return h % self.MAX

    def __setitem__(self, key, val):
        """OVERWRITE build in __setitem__"""
        h = self.get_hash(key)
        found = False

        # ITERATE TO CHECK WHETHER THE key is EXISTED
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx == (key, val)]
                found = True  # found key exist
                break

        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        """OVERWRITE build in __getitem__"""
        h = self.get_hash(key)

        # Because self.arr now is list in list, we need to iterate to get the value
        for element in self.arr[h]:
            # element[0] is the key
            # iteration has accessed to every elements,
            # while slicing (implicitly) will access the value in elem
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)

        # This iterate the list inside, not the the list outside
        for idx, element in enumerate(self.arr[h]):
            print(f"IDX: {idx}, h:{h}")
            if element[0] == key:
                print(f"ELEMENT: {element[0]}, {key}")
                del self.arr[h][idx]


table = HashTable()

# COLLISION HERE!
table["march 6"] = 420
table["march 17"] = 17
table["march 22"] = 10


# print(table["march 6"])
# print(table["march 17"])
print("BEFORE: \n", table.arr)

del table["march 17"]
# del table["march 22"]

print("AFTER: \n", table.arr)
