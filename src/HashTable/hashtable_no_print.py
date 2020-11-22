class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        result = 0
        for pos in range(len(value)):
            sym = value[pos]
            result += ord(sym) * pos
        return result % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        iteration = 0
        while iteration < self.size:
            iteration += 1
            if self.slots[slot] is None:
                return slot
            else:
                slot = (slot + self.step) % self.size
        return None

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            return slot
        else:
            return None

    def find(self, value):
        slot = self.hash_fun(value)
        iteration = 0
        while iteration < self.size:
            iteration += 1
            if self.slots[slot] == value:
                return slot
            else:
                slot = (slot + self.step) % self.size
        return None
