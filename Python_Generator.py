# # # # -*- coding: utf-8 -*-
# Generator - the value calculation is done while iterating the loop during program runtime
# The list doesn't have to be generated at once. This will save memory during runtime.
# Function is executed in sequence, while generator is executed and get interrupted at yield key word.
# When generator is executed again, it will be executed from the last point (yield) where it's interrupted


if __name__ == '__main__':
    # How to create a generator
    # List Comprehension
    L = [x * x for x in range(5)]
    print L
    # How to define a generator?
    # 1. By changing square bracket to bracket in list comprehension, we can get a generator
    G = (x * x for x in range(5))
    print G
    # If no element can be retrieved, it will throw stopiteration error
    #print G.next(),G.next(),G.next(),G.next(),G.next(),G.next(),G.next()
    # We can also use for loop to iterate generator
    for g in G:
        print g

    # 2. By adding key word "yield" in function definition

    # function
    def fib(max):
        n, a, b = 0, 0, 1
        while n<max:
            print b # -> change this line to yield b
            a, b = b, a+b
            n += 1
        return

    def fibgenerator(max):
        n, a, b = 0, 0, 1
        while n<max:
            yield b # -> change this line to yield b
            a, b = b, a+b
            n += 1
        return

    # How to use
    for i in fibgenerator(10):
        print i