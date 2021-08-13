class MinHeap(dict):
    def __setitem__(self, k, v: tuple) -> None:
        if not isinstance(v, tuple):
            raise ValueError("Value must be a tuple. Distance and vertice")
        try:
            if self[k][0] > v[0]:
                super().__setitem__(k, v)
        except KeyError:
            super().__setitem__(k, v)

    def pop(self) -> tuple:
        if self.is_not_empty():
            key = next(iter(self))
            val = self[key]
            for k, v in self.items():
                if v[0] < val[0]:
                    key = k
                    val = v
            del self[key]
            return key, val
        else:
            raise KeyError("Storage is empty")

    def is_not_empty(self):
        return bool(self)


def perform_test_min_heap(cases: int):
    mh = MinHeap()
    for i in reversed(range(0, cases)):
        mh[f"key_{i}"] = i
    mh.pop()


def perform_test_std_collection(cases: int):
    std_list = list()
    for i in reversed(range(0, cases)):
        std_list.append(i)
    std_list.sort()
    std_list.pop()


if __name__ == "__main__":
    mh = MinHeap()
    for i in reversed(range(0, 10)):
        mh[f"key_{i}"] = i
    print(mh.pop())
    print(mh)
