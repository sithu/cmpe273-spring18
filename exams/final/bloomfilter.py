# Install mmh3 and bitarray 3rd party module first
# pip install mmh3
# pip install bitarray
import math
import mmh3
from bitarray import bitarray

ERR_RATE=0.05

class BloomFilter():
 
    '''
    Class for Bloom filter, using murmur3 hash function
    '''
 
    def __init__(self, items_count):
        '''
        items_count : int
            Number of items expected to be stored in bloom filter
        error_rate : float
            False Positive probability in decimal
        '''
        # Size of bit array to use
        self.size = self.get_size(items_count, ERR_RATE)
 
        # number of hash functions to use
        self.hash_count = self.get_hash_count(self.size,items_count)
 
        # Bit array of given size
        self.bit_array = bitarray(self.size)
 
        # initialize all bits as 0
        self.bit_array.setall(0)
 
    def add(self, item):
        '''
        Add an item in the filter
        '''
        for i in range(self.hash_count):
            digest = mmh3.hash(item,i) % self.size
            self.bit_array[digest] = True
 
    def __contains__(self, item):
        '''
        TODO: Check for existence of an item in filter
        '''
        return True
 
    @classmethod
    def get_size(self,n,p):
        '''
        Return the size of bit array(m) to used using
        following formula
        m = -(n * lg(p)) / (lg(2)^2)
        n : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        '''
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)
 
    @classmethod
    def get_hash_count(self, m, n):
        '''
        Return the hash function(k) to be used using
        following formula
        k = (m/n) * lg(2)
 
        m : int
            size of bit array
        n : int
            number of items expected to be stored in filter
        '''
        k = (m/n) * math.log(2)
        return int(k)


def test():
    bf = BloomFilter(20)
    # words to be added
    word_present = ['abound','abounds','abundance','abundant','accessable',
                'bloom','blossom','bolster','bonny','bonus','bonuses',
                'coherent','cohesive','colorful','comely','comfort',
                'gems','generosity','generous','generously','genial']

    for item in word_present:
        bf.add(item)

    word_absent = ['bluff','cheater','hate','war','humanity',
               'racism','hurt','nuke','gloomy','facebook',
               'geeksforgeeks','twitter']

    test_words = word_present[:10] + word_absent

    for word in test_words:
        if word in bf:
            if word in word_absent:
                print("'{}' is a false positive!".format(word))
            else:
                print("'{}' is probably present!".format(word))
        else:
            print("'{}' is definitely not present!".format(word))


test()