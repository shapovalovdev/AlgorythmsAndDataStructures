# class NativeDictionary:
#     def __init__(self, sz):
#         self.size = sz
#         self.keys = [None] * self.size
#         self.values = [None] * self.size
#
#     def hash_fun(self, key):
#         # в качестве key поступают строки!
#         # всегда возвращает корректный индекс слота
#         def hashing(value):
#             result = 0
#             for pos in range(len(value)):
#                 sym = value[pos]
#                 result += ord(sym) * pos
#             return result % self.size
#
#         slot = hashing(key)
#
#         iteration = 0
#         step = 3
#         while iteration < self.size:
#             iteration += 1
#             if self.keys[slot] is None:
#                 return slot
#             else:
#                 slot = (slot + step) % self.size
#         return None
#
#     def is_key(self, key):
#         # возвращает True если ключ имеется,
#         # иначе False
#         if key in self.keys:
#             return True
#         else:
#             return False
#
#     def put(self, key, value):
#         if self.is_key(key):
#             slot=self.keys.index(key)
#             self.values[slot] = value
#         else:
#             slot = self.hash_fun(key)
#             if slot is not None:
#                 self.keys[slot] = key
#                 self.values[slot] = value
#             else:
#                 return None
#         # гарантированно записываем
#         # значение value по ключу key
#
#     def find_key(self, value, size, step):
#         slot = self.hash_fun(value)
#         for i in range(size):
#             if self.keys[slot] == value:
#                 return slot
#             else:
#                 slot = (slot + step) % size
#         return None
#
#     def get(self, key):
#
#         if self.is_key(key):
#             slot = self.find_key(key, self.size, 3)
#             return self.values[slot]
#         else:
#             # возвращает value для key,
#             # или None если ключ не найден
#             return None


class NativeCache():
    def __init__(self, sz):
        self.size = sz
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hashing(self, value):
        result = 0
        for pos in range(len(value)):
            sym = value[pos]
            result += ord(sym) * pos
        return result % self.size

    def seek_empty_slot(self, key):
        slot = self.hashing(key)
        for i in range(self.size):
            if self.keys[slot] is None:
                return slot
            else:
                slot = (slot + 3) % self.size
        return None

    def find_value(self, value):
        slot = self.hashing(value)

        for i in range(self.size):
            if self.keys[slot] == value:
                return slot
            else:
                slot = (slot + 3) % self.size
        return None


    def get(self, key):

        if self.is_key(key):
            slot = self.find_value(key)
            self.hits[slot]+=1
            return self.values[slot]
        else:
            # возвращает value для key,
            # или None если ключ не найден
            return None

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.keys:
            return True
        else:
            return False

    def find_slot_to_clean(self):
        return self.hits.index(min(self.hits))



    def put(self, key, value):



        if self.is_key(key):
            slot = self.find_value(key)
            self.values[slot] = value

        else:
            slot = self.seek_empty_slot(key)
            if slot:
                self.keys[slot] = key
                self.values[slot] = value
            else:
                #вытесняем самый менее запрашиваемый слот
                slot_to_clean = self.find_slot_to_clean()
                self.keys[slot_to_clean] = key
                self.values[slot_to_clean] = value

    # def illustration(self):
    #     for s, v, h in zip(self.keys, self.values, self.hits):
    #         print(f"Key {s} value {v} hit {h}")

# from random import choice
# import requests
# import os
# if __name__ == '__main__':
#     if not os.path.exists('words.txt') and not os.path.getsize('words.txt') > 0:
#         http = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
#         with open('words.txt', 'w+') as file:
#             file.write(http.text)
#     words=[]
#     with open('words.txt', 'r') as f:
#         for i in range(1000):
#             line = f.readline()
#             words.append(line.rstrip())
#
#     # print(words)
#     cache=NativeCache(7)
#     words_to_add_1=[('Albert', 'Einstein'),
#                     ('Donald', 'Duck'),
#                     ('Muck', 'Donalds'),
#                     ('Gabriel', 'Batistuta'),
#                     ('Vladimir', 'Putin'),
#                     ('aBRAKADABRA', 'oDUDENKO')]
#     words_to_add_2 = [('Petr', 'Ivan'),
#                     ('Gomunkul', 'Saraevo'),
#                     ('Robert', 'Lewandovski'),
#                     ('Yan', 'Prokofiev'),
#                       ('Boris', 'Nemcov')]
#
#     # for i in range(23):
#     #     cache.put(choice(words), choice(words))
#     for name, surname in words_to_add_1:
#         cache.put(name, surname)
#
#
#     # for i in range(100):
#     #     cache.get(choice(words))
#     #     r = http.request('GET', 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
#     #     list_of_words=r.data.decode('utf-8').split('\n')
#
#
#     cache.illustration()
#     cache.get('Vladimir')
#     cache.get('Vladimir')
#     cache.get('Donald')
#     for name, surname in words_to_add_2:
#         cache.put(name, surname)
#     print("sdfsdfdsfdfsd")
#     cache.illustration()