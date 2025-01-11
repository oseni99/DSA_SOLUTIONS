import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.store = []

        # I HAVE THAT STORE ARRAY BECAUSE WHEN I WANT TO DO THE REMOVE I USE IT TO SUCCESFULLY REMOVE
        # AND GET THE RANDOM BECAUSE RANDOM NEEDS INDEX TO WORK
        # I STORE THE HASHMAP WITH JUST THE INDEX IT IS IN THAT STORE

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.store)
            self.store.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            last_val = self.store[-1]
            self.store[idx] = last_val
            self.hashmap[last_val] = idx
            self.store.pop()
            del self.hashmap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.store)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()