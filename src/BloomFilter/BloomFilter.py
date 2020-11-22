#import hashlib
#from random import randint
class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.bloom_array=self.filter_len * [0]

    def hash1(self, str1):

        result=1
        rand_int=17
        for c in str1:
            result = result*rand_int + ord(c)
        return result % self.filter_len

    #
    # def hash2(self, str1):
    #
    #     result=0
    #     b_str1=str.encode(str1)
    #     h=hashlib.sha1(b_str1).hexdigest()
    #     for c in str1:
    #         result += ord(c)
    #     return result % self.filter_len

    def hash2(self, str1):
        result=1
        rand_int=223
        for c in str1:
            result = result*rand_int + ord(c)
        return result % self.filter_len

    def add(self, str1):
        self.bloom_array[self.hash1(str1)] = 1
        self.bloom_array[self.hash2(str1)] = 1

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        if not self.bloom_array[self.hash1(str1)] or not self.bloom_array[self.hash2(str1)]:
            return False
        else:
            return True

# if __name__ == '__main__':
#     dataset=["0123456789", "1234567890", "sdfsdfsdf", "sdf2143124",  "hophey", "abirvaolg", "8901234567", "2356sdfqix,ed", "9012345678"]
#     dataset2=["012345678932", "12345623e47890", "sdfdsfq1sdfsdf", "sdf2gs2143124",  "qwerhophey", "atgxcvbirvaolg", "8sdgaw901234567", "321452356sdfqix,ed", "5124e39012345678"]
#     BLOOM_TEST=BloomFilter(32)
#     for data in dataset:
#         BLOOM_TEST.add(data)
#     for data in dataset2:
#         if BLOOM_TEST.is_value(data):
#             print(f'It seems {data} is here')
#         else:
#             print(f'No {data} by the name of bloom filter ')
#     for data in dataset:
#         if BLOOM_TEST.is_value(data):
#             print(f'It seems {data} is here')
#         else:
#             print(f'No {data} by the name of bloom filter ')
#     print( BLOOM_TEST.bloom_array)