class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size #array initialization

    def hash_fun(self, value):
        # в качестве value поступают строки!
        sum=0
        for pos in range(len(value)):
            sym=value[pos]
            sum+=ord(sym)*pos
        # всегда возвращает корректный индекс слота
        return sum%self.size

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        slot=self.hash_fun(value)
        #print(f"The first slot is {slot}")
        iteration=0
        while iteration < self.size:
            iteration+=1
            print(f"The slot in the loop is {slot} the iteration {iteration}")
            if self.slots[slot] is None:
                return slot
            else:
                slot=(slot+self.step)%self.size
        #print(f"Cannot find slot in  {iteration} iterations for the size of array {self.size}")
        return None


    def put(self, value):
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        slot=self.seek_slot(value)
        if slot is not None:
            self.slots[slot]=value
            return slot
        else:
            return None

    def find(self, value):
        # находит индекс слота со значением, или None
        slot=self.hash_fun(value)
        iteration = 0
        while iteration < self.size:
            iteration += 1
            if self.slots[slot] == value:
                return slot
            else:
                slot=(slot+self.step)%self.size
        #print(f"Cannot find value {value} in  {iteration} iterations for the size of array {self.size}")
        return None

# if __name__=="__main__":
#      table1=HashTable(19,5)
#     print (table1.hash_fun("fgweasdfsdf"))
#     TEST_STRINGS=["Open", "afile", "on23thedisk", "please", "change1", "thefilepath)", "abrakadabra" , "2342", "hachaturian", "1", "", "krakoziabra", "zabadulia", "karkas", "qqqq", "0", "9832", ",s.3234$", "uresdf" ]
#     for pos in range(len(TEST_STRINGS)):
#         print(f"{pos} string of value {TEST_STRINGS[pos]} ")
#         print(table1.put(TEST_STRINGS[pos]))
#     print("#######")
#     table1.put("change")
#     print(table1.find("please"))