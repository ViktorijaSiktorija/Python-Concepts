# to su iz dela o klasama @classicmethod i @staticmethod
# funkcije u Pajtonu mogu da se prosledjuju kao promenljive, mogu da budu argumenti
# slicno se ponasaju kao promenljive
# dekoratori koriste moc funkcija, cine ih mocnijim

# Higher order function HOC - moze da bude:
# funkcija koja prihvata drugu funkciju u parametrima
# ili da bude funkcija koja vraca drugu funkciju
# npr map je HOC, reduce, filter

from time import time


def hello(func):
    func()


def greet():
    def func():
        return 5
    return func


a = greet()
print(a)

# 2


def my_decorator(funcc):
    def wrap_func(*args, **kwargs):
        print('*******')
        funcc(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator
def cao(greeting, emoji=':D'):
    #print('de si')
    print(greeting, emoji)


@my_decorator
def bye():
    print('vidimo se')


cao('eeej')
# bye()

# 3 merenje performansa funkcije


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(t2-t1)
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000):
        i*5


long_time()
