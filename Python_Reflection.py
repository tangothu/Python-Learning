# # # # -*- coding: utf-8 -*-
'''
Refleciton is a common concept in programming that allows users to dynamically inspect attributes, methods
when they are unknown to users. It happens for a user when he/she doesn't know the details of an object but
still want to access the attributes or methods. Users will then use reflection, built in methods or inspect
module to get the unknow information during runtime.

'''
import inspect
def foo(param="test"):
    """
    :return:
    """
    a = 1
    print (param)
    return

class Car(object):
    """ Definition of class Car """
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
    def run(self):
        print ("Car %s is running!" % self.model)

class Train(object):
    pass

if __name__ == '__main__':
    model = "Edge"
    brand = "Ford"
    c = Car(model,brand)
    # Inspect module
    print (inspect.getmembers(c)) #
    print (inspect.ismethod(c.run()))
    print (inspect.ismethod(c.run))
    print (inspect.getmodule(c))

    # Accessing object's attributes using getattr and setattr
    # print (dir(c))
    # setattr(c,'model','F150')
    # current_model = getattr(c,'model')
    # print ("current model is %s" %current_model)
    # c.run()

    # Accessing the metadata of object
    # 1. class type of object
    # print (isinstance(c,Car))
    # print (isinstance(c,Train))

    # 2. module information

    import fnmatch as m
    # print (m.__doc__)
    # print (m.__name__) # Returns the module name when defined
    # print (m.__file__) #
    # print (m.__dict__) # Returns the dictionary of attributes with their values

    # 3. class information

    # print (Car.__doc__)
    # print (Car.__dict__)
    # print (Car.__bases__)

    # 4. object information
    # Try to print same attributes of an object
    # print (c.__doc__)
    # note __name__ and __file__ are attributes of modules, NOT of objects
    # print (c.__name__)
    # print (c.__file__)
    # print (c.__dict__)
    # print (c.__class__)

    # 5. function/method information
    # f = "test".split # f is the function of split
    # l = "test".split() # l is the result after calling split() function of string
    # ll = "t e s t".split()
    # print (type(f))
    # print (type(l))
    # print (l)
    # print (ll)
    # #print (f.func_dict) # Note split is a built-in function(builtin_function_or_method), who usually doesn't have func_dict
    # #print (f.func_code)
    # print (foo.__dict__)

