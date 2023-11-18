"""
HASH TABLE/MAP 1
NOTE:
- hash function
- hash function has various methodology
  1. using ASCII numbers
"""


# Writing has function
def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)  # ord() - find ascii value within ascii table
    return h % 100


# print(get_hash("march 28"))
# print(get_hash("march 21"))


class HashTable:
    def __init__(self):
        self.MAX = 50
        self.arr = [None for i in range(self.MAX)]  # list of None with len(self.MAX)

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  # ord() - find ascii value within ascii table
        return h % self.MAX

    def __setitem__(self, key, val):
        """OVERWRITE build in __setitem__"""
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        """OVERWRITE build in __getitem__"""
        h = self.get_hash(key)
        print("HASHED INDEX", h)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


table = HashTable()
print(table.get_hash("march 2021"))
# table.add("march 99", 45)
table["march 99"] = 45
print(table["march 99"])
del table["march 99"]
print(table["march 99"])
# print(table.get("march 99"))
# print(table.arr)
# NEXT: -- collision
