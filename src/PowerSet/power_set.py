
class PowerSet:

    def __init__(self):
        # ваша реализация хранилищe
        self.count=0
        self.elements = []

    def get(self, value):
        if value in self.elements:
            return True
        else:
            return False

    def put(self, value):
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        if not self.get(value):

            self.elements.append(value)
            self.count+=1

    def size(self):
        return self.count
        # количество элементов в множестве

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False

        if self.get(value):
           self.elements.remove(value)
           self.count-=1
           return True
        else:
            return False


    def intersection(self, set2):
        # пересечение текущего множества и set2
        result=PowerSet()

        if self.size() < set2.size():
            for value in self.elements:
                if self.get(value) and set2.get(value):
                    result.put(value)
        else:
            for value in set2.elements:
                if self.get(value) and set2.get(value):
                    result.put(value)

        return result

    def union(self, set2):
        # объединенbе текущего множества и set2
        if self.size()==0:
            return set2
        if set2.size()==0:
            return self

        result=PowerSet()
        for value in self.elements:
            result.put(value)
        for value in set2.elements:
            result.put(value)
        return result

    def difference(self, set2):
        # разница текущего множества и set2

        if self.size() == 0 or set2.size == 0:
            return self
        result = PowerSet()
        for value in self.elements:
            if set2.get(value):
                continue
            else:
                result.put(value)
        return result

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for value in set2.elements:
            if  not self.get(value):
                return False
        return True

# from time import perf_counter
# import urllib3
# #
# #
# if __name__ == '__main__':
#     S1=PowerSet()
#     assert S1.size() == 0
#     S1.put('AhalayMahalay')
#     assert S1.get('AhalayMahalay') == True
#     S1.put('AhalayMahalay')
#     assert S1.size() == 1
#     assert S1.size() == 1
#     S1.put('SimSalavim')
#     assert S1.get('SimSalavim') == True
#     assert S1.size() == 2
#     assert S1.remove('SimSalavim') == True
#     assert S1.size() == 1
#     print(S1.elements)
#     print([x for x in S1.elements if x is not None])
#
#     string1='ABCDEF'
#     string2=''
#     S3 = PowerSet()
#     S2 = PowerSet()
#     for s in string1:
#         S2.put(s)
#     for s in string2:
#         S3.put(s)
#
#     start = perf_counter()
#     S4 = S2.union(S3)
#
#     end = perf_counter()
#     print(end - start)
# #
#     start = perf_counter()
#     S4 = S3.difference(S2)
#
#     end = perf_counter()
#     print(end - start)
#
#     string4='ABCDEF'
#     string5='ABC'
#     S4 = PowerSet()
#     S5 = PowerSet()
#     for s in string4:
#         S4.put(s)
#     for s in string5:
#         S5.put(s)
#
#     assert S4.issubset(S5) == True
#     assert S5.issubset(S4) == False
#
#     S1=PowerSet()
#     S2=PowerSet()
#     http = urllib3.PoolManager()
#     r = http.request('GET', 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
#     list_of_words=r.data.decode('utf-8').split('\n')
#     limit=20000
#     for w in list_of_words:
#         if limit < 0:
#             break
#         if limit < 10000:
#             S1.put(w)
#         else:
#             S2.put(w)
#         limit-=1
#
#
#
#     start = perf_counter()
#     S3 = S1.union(S2)
#     print(S3.elements)
#     end = perf_counter()
#     time_perf=end-start
#     print(f"Union time is {time_perf}")
#     print(f"The size of S3 is {S3.size()}")
#     print(f"The size of S1 is {S1.size()}")
#     print(f"The size of S2 is {S2.size()}")