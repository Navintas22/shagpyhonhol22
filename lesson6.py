import requests

#help(requests)

def func():
    pass

class Superclass:
    def print1(self):
        print('hello')

rq = requests
f = func
sc = Superclass()

print(rq.__name__)
print(requests.__name__)
print(f.__name__)
print(func.__name__)
print(__name__)

print(type(rq))
print(type(f))
print(type(sc))

list_ = []
for method in dir(list_):
    print(method)

if hasattr(sc, "print1"):
    sc.print1()

print("kkkkk")

st = "papa"
print(callable(st))
print(callable(func))

import inspect

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))

print(inspect.getmodule(requests.get))
print(inspect.getmodule(Superclass))

