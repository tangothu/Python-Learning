# # # # -*- coding: utf-8 -*-

if __name__ == '__main__':
    # What is Iterable? Things that can be iterated in a for loop.
    # Example:  1. list, set, tuple, dict, str
    #           2. generator
    from collections import Iterable
    l = [1,2,'a']
    print isinstance(l,Iterable)
    g = (x for x in range(5))
    print isinstance(g,Iterable)

    # What is Iterator? Things that can be iterated by next() -> generator
    # list, set, tuple, dict, str are not iterator but are iterable
    # Why? because iterator is like a data stream, which is lazy initialization
    # This means the data can be evaluated when being accessed, can be a unlimited length of array

    from collections import Iterator
    print isinstance(g, Iterator)
    print isinstance([], Iterator)
    print isinstance(iter([]), Iterator)

