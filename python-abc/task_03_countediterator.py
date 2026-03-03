#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterobj):
        #  iter() is a python built-in funct. that turns iterable into iterator
        #  It stores the original iterator
        self.iterobj = iter(iterobj)
        self.counter =  0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            obj = next(self.iterobj)
            self.counter += 1
            #  normally next() will automatically raise stopiterations
            return obj
        except StopIteration:
            raise StopIteration
        
    def get_count(self):
        return self.counter 
       