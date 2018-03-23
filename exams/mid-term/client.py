import requests

class Ring():

    def __init__(self,url='http://127.0.0.1:3000'):
        self.url = url


    def __call__(self, *args, **kwargs):
        # http://farmdev.com/src/secrets/magicmethod/index.html#introducing-call
        # TODO make HTTP GET call /items to retrieve all names.
        return "Alice,Bob,Charlie"


    def append(self, name):
        # TODO make HTTP POST call /items to append new name.
        pass


    def __getitem__(self, index):
        # Python special method: http://www.diveintopython.net/object_oriented_framework/special_class_methods.html
        # TODO make HTTP GET call /items/{index} to a name.
        return "Alice"


def test():
    '''DO NOT CHANGE THIS TEST CODE OR YOU WILL GET ZERO!'''
    ring = Ring('http://127.0.0.1:3000')
    ring.append('Chuck')
    ring.append('Alice')
    ring.append('Bob')
    print(ring[0])
    print(ring())
    ring.append('Charlie')
    print(ring[0])
    print(ring())


if __name__ == "__main__":
    test()
    