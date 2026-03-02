#!/usr/bin/python3
class CounterIterator:
    def __init__(self, iterobj):
        #  iter() is a python built-in funct. that turns iterable into iterator
        self.iterobj = iter(iterobj)
        self.counter =  0
        
    def get_count(self):
        return self.counter