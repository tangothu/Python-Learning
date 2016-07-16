# # # # -*- coding: utf-8 -*-
def log(func):
    def wrapper(*args, **kwargs):
        import datetime
        print ('call %s(): , at time %s' % (func.__name__, datetime.datetime.now()))
        print args
        print kwargs
        return func(*args, **kwargs)
    return wrapper  # Note there is no () here

# Adding log to the top of definition of now() is equivalent to now = log(now)
@log
def now(a,b='abc',*args,**kwargs):
    print 'a=',a
    print 'b=',b
    print 'args=',args
    print 'kwargs=',kwargs
    pass

def log2(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print ('%s, %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log2('test') # This call is equivalent to now2 = log2('test')(now2)
def now2():
    pass


# Why/when do  we need python decorator?

# # Case 1. Run time check on function return value
# # Assume you have many functions that will return a dict with a field called "summary". All summary's returned value
# # should have length shorter than 80 so you can validate the functions like this:
# def validate_summary(func):
#     def wrapper(*args, **kwargs):
#         data = func(*args, **kwargs)
#         if len(data["summary"]) > 80:
#             raise ValueError("Summary too long")
#         return data
#     return wrapper
#
# @validate_summary
# def fetch_customer_data():
#     # ...
#
# @validate_summary
# def query_orders(criteria):
#     # ...
#
# # Case 2. Reuse code
# # Assume you have an API make_api_call() that needs to be repeated multiple times and this is already everywhere in your code
# # Now you need to add retry logic to this function call
#
# resp = None
# while True:
#     resp = make_api_call()
#     if resp.status_code == 500 and tries < MAX_TRIES:
#         tries += 1
#         continue
#     break
# process_response(resp)
#
# # The decorated function returns a Response object,
# # which has a status_code attribute. 200 means
# # success; 500 indicates a server-side error.
#
# def retry(func):
#     def retried_func(*args, **kwargs):
#         MAX_TRIES = 3
#         tries = 0
#         while True:
#             resp = func(*args, **kwargs)
#             if resp.status_code == 500 and tries < MAX_TRIES:
#                 tries += 1
#                 continue
#             break
#         return resp
#     return retried_func
#
# This gives you an easy-to-use @retry decorator:
#
# @retry
# def make_api_call():
#     # ....

if __name__ == '__main__':
    now('abc','def',d='ddd',c='abc')
    #now2()
