"""
SOLVING COLLISION in HASH TABLE with LINEAR PROBING

NOTE:
- Hashed function is used to decide the position (index)
of the information within the array. 
- We still can use the key as the reference to the value
with `(key, val)`
- `arr[key] = val` in this code is not similar with accessing
the Dictionary. It is slicing and overwrite. 

"""


class HashTable:
    def __init__(self):
        self.MAX = 50
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key: str):
        """
        Hashing the key, returned index:int.
        """
        h = 0
        for char in key:
            h += ord(char)
        index: int = h % self.MAX
        return index

    def __setitem__(self, key, val):
        key_idx = self.get_hash(key)

        # TODO: Using (key, val) instead of arr[key] = val

        counter = 0

        while True:
            if self.arr[key_idx] == None:
                self.arr[key_idx] = val
                break
            else:
                counter += 1
                self.arr[key_idx + counter] = val
                break

    def __getitem__(self, key):
        key_idx = self.get_hash(key)

        return self.arr[key_idx]


table = HashTable()

# COLLISION 1
table["march 6"] = 32
table["march 17"] = 99

# COLLISION 2
table["march 1"] = 98
table["march 12"] = 44

print(
    table["march 12"],
    table["march 1"],
)
print(table.arr)
