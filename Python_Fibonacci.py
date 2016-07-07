# # # # -*- coding: utf-8 -*-

def fib(n):
    if n <= 2:
        return 1
    if n > 2:
        return fib(n-1) + fib(n-2)

def fib2(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        value = fib2(n-1)

def fibonacci(x):

    List = []
    f = 1
    List.append(f)
    List.append(f) #because the fibonacci sequence has two 1's at first
    while f<=x:
        f = List[-1] + List[-2]   #says that f = the sum of the last two f's in the series
        List.append(f)
    else:
        List.remove(List[-1])  #because the code lists the fibonacci number one past x. Not necessary, but defines the code better
        for i in range(0, len(List)):
            print List[i]

if __name__ == '__main__':
    print fib(5)
    