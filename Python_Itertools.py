# # # # -*- coding: utf-8 -*-
# Python itertools is used to create
import itertools

if __name__ == '__main__':

    ## Create unlimited times of iterators
    # itertools.count() -> creates iterators that generates value = start with step
    start = 10
    step = 5
    for i in itertools.count(start, step):
        if i > 20:
            break
        print i

    # itertools.cycle() -> creates iterators that is cyclic
    i = 0
    for item in itertools.cycle(['a', 'b', 'c']):
        i += 1
        if i == 5:
            break
        print (i, item)

    # Implementation of itertools.cycle()
    def cycle(iterable):
        # cycle('ABCD') --> A B C D A B C D A B C D ...
        saved = []
        # Below for loop will only loop once and record all elements in iterable into saved []
        for element in iterable:
            yield element
            saved.append(element)
        # Infinite loop started
        while saved:
            for element in saved:
                yield element

    # itertools.chain(*iterables) -> takes multiple iterables in the parameter, and combine the elements in each iterable into one iterable
    for i in itertools.chain([1, 2], ['a', 'b']):
        print i

    # itertools.groupby(iterable[, key]) -> creates iterator that will classify elements in iterable grouped by key

    # Output is ['A', 'B', 'C', 'D', 'A', 'B']
    print [k for k, g in itertools.groupby('AAAABBBCCDAABBB')]
    # Output is [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D'], ['A', 'A'], ['B', 'B', 'B']]
    print [list(g) for k, g in itertools.groupby('AAAABBBCCDAABBB')]

    # This is because by default, key is the value from prior element when evaluating current element
    # When it comes to evaluate the 'B' in 'AAAAB..', since 'B' is different than the prior element 'A', it will put it
    # into the (key,group) pair

    a = ['aa', 'ab', 'abc', 'bcd', 'abcde']
    # Result:
    # 2 ['aa', 'ab']
    # 3 ['abc', 'bcd']
    # 5 ['abcde']
    for i, k in itertools.groupby(a, len):  # len is the key to group by each element
        print i, list(k)


    # itertools.imap(function, *iterables) -> creates an iterator that generate function(i1, i2, ..., iN)
    # where i1，i2...iN are from iter1，iter2 ... iterN, if function is None then return tuple (i1, i2, ..., iN)
    def imap(function, *iterables):
        # imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
        iterables = map(iter, iterables)
        while True:
            args = [next(it) for it in iterables]
            if function is None:
                yield tuple(args)
            else:
                yield function(*args)


    print 'Pows:'
    for i in imap(pow, (2,), (5,)):
        print i

    print 'Doubles:'
    for i in imap(lambda x: 2 * x, xrange(5)):
        print i

    # itertools.permutations(iterable, r=None) -> generates permutation of iterables with lenth r
    for i in itertools.permutations("abc",r=2):
        print i

    for i in itertools.permutations("abc",r=1):
        print i

