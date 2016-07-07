# # # # -*- coding: utf-8 -*-
import functools

if __name__ == '__main__':

    def add(a,b):
        """
        Returns sum of two ints
        :param a: int
        :param b: int
        :return: int
        """
        return a+b
    # functools.partial
    # print (add(3,4))
    add3 = functools.partial(add,3) # The first argument must be callable, returned value is also callable
    print (add3(4))

    # functools.update_wrapper
    def wrap(func):
        def call_it(*args,**kwargs):
            """wrap function: call_it"""
            print ("before call")
            return func(*args, **kwargs)
        return call_it

    @wrap
    def hello():
        """ Say hello """
        print ("hello world")

    from functools import update_wrapper
    def wrapper(func):
        def call_it(*args, **kwargs):
            """wrapper function: call_it"""
            print ("before call")
            return func(*args, **kwargs)
        return update_wrapper(call_it, func)

    @wrapper
    def hello2():
        """ Say hello 2 """
        print ("hello2 world")

    from functools import wraps
    def wrapper_with_wraps(func):
        @wraps(func)
        def call_it(*args, **kwargs):
            """wrapper function: call_it"""
            print ("before call")
            return func(*args, **kwargs)
        return call_it # Note this is different than update_wrapper()

    @wrapper_with_wraps
    def hello3():
        """ Say hello 3 """
        print ("hello 3 world")

    f = hello
    f()
    print (f.__doc__)
    print (f.__name__)
    f2 = hello2
    f2()
    print (f2.__doc__)
    print (f2.__name__)

    f3 = hello3
    f3()
    print (f3.__doc__)
    print (f3.__name__)
