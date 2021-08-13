from collections import OrderedDict
from typing import TypeVar
from math import inf

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class MinHeap(dict):  
    def __setitem__(self, k: _KT, v: _VT) -> None:
        try:
            if self[k] > v:
                super().__setitem__(k, v)
        except KeyError:
            super().__setitem__(k, v)
    
    def pop(self) -> tuple:
        if self.is_not_empty():
            key = next(iter(self))
            val = self[key]
            for k, v in self.items():  
                if v < val:
                    key = k
                    val = v
            del self[key]
            return key , val
        else:
            raise KeyError('Storage is empty')
    
    def is_not_empty(self):
        return bool(self)

def perform_test_min_heap(cases: int):
    mh = MinHeap()
    for i in reversed(range(0, cases)):
        mh[f'key_{i}'] = i
    mh.pop()

def perform_test_std_collection(cases: int):
    l = list()
    for i in reversed(range(0, cases)):
        l.append(i)
    l.sort()
    l.pop()

if __name__ == '__main__':
    mh = MinHeap()
    for i in reversed(range(0, 10)):
        mh[f'key_{i}'] = i
    print(mh.pop())
    print(mh)