class RandomizedSet:

    def __init__(self):
        self.sett = set()

    def insert(self, val: int) -> bool:
        in_set = val not in self.sett
        self.sett.add(val)

        return in_set

    def remove(self, val: int) -> bool:
        in_set = val in self.sett
        if in_set:
            self.sett.remove(val)
        return in_set
        

    def getRandom(self) -> int:
        return random.choice(tuple(self.sett))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
