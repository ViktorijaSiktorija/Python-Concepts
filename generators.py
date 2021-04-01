# dozvoljavaju da generisemo sekvencu vrednosti tokom vremena
# range je generator
# to je posebna stvar koja nam dozvoljava da koristimo keyword yield
# koja moze da pauzira i pokrene funkcije

# iterable su

from time import time
range(100)  # stvara listu 1 po 1
list(range(100))  # ovo je sporije


def make_list(num):
    result = []
    for i in range(num):  # generator ne stvara sam veliku listu u memoriji
        result.append(i*2)
    return result


moja_lista = make_list(100)
print(moja_lista)

# Generator


def special_for(iterable):  # ovako for radi ispod
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])


class MyGen:  # pravimo range
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # this line allows us to use the current number as
        # the starting point for the iteration
        MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 100)  # ovo radi u terminalu, al ne u run
for i in gen:
    print(i)


def performance(fn):  # Vezba iz decoratora, performans generatora:

    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(t2-t1)
        return result
    return wrapper


@ performance  # brzi je generator
def long_time():
    print('1')
    for i in range(100000):
        i*5


@ performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5


long_time()
long_time2()

# Fibonaci


def fib(n):  # uzela resenje iz kursa sa vezbama
    n1 = 0
    n2 = 1
    for i in range(n):
        yield n1  # prvo da bude 0
        nextTerm = n1 + n2  # onda da bude 1
        n1 = n2
        n2 = nextTerm


for x in fib(100):  # ovde se ne cuva u memoriji, brze je
    print(x)


def fib2(n):  # sa listom, ovo je sporije
    # tu ide return i print bez for
    n1 = 0
    n2 = 1
    result = []
    for i in range(n):
        result.append(n1)
        nextTerm = n1
        n1 = n2
        n2 = nextTerm + n2
    return result


print(fib2(100))  # ovako cuva 1 po 1 u memoriji
