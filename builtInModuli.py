# from utiliyy import * - da sve importuje, al bolje da se oznaci
#from folder.folder2 import modul
# __init__.py treba da bude default folder
# i onda pozovemo modul i funkciju koja nam treba u main

# __main__
# if __name__ == '__main__':


# Built it moduli:
from array import array
import datetime
from collections import Counter, defaultdict, OrderedDict
import sys
import random as alias
from random import randint
print(dir(alias))  # pokaze sve metode moguce za random
print(alias.randint(1, 10))
print(alias.choice([1, 2, 3, 4, 5]))

# sistem
print(sys)
sys.argv  # argv, da iz terminala dajemo parametre

# Guessing game
#answer = randint(int(sys.argv[1]), int(sys.argv[2]))
#answer = randint(1, 10)
# while True:
# try:
# guess = int(input(' guess '))
# if 0 < guess < 11:
# if guess == answer:
#   print('you are a genius!')
#   break
# else:
#  print('hey bozo, I said 1~10')
# except ValueError:
#   print('please enter a number')
#   continue

# pipenv
# venv - virtual environments, da tu drzimo sve pakete na jednom mestu

# collections
li = [1, 2, 3, 4, 5, 6, 7, 7]  # Counter object/ koliko puta se pojavio najvise
# tj hash map / dictionary
sentence = 'cao ja sam vika'
print(Counter(li))
print(Counter(sentence))

# defaultdict
dicti = defaultdict(lambda: 5, {'a': 1,  # callable funkcija
                                'b': 2})
print(dicti['a'])  # ako stavimo c, dobijemo 5

# OrdeeredDict - nebitan sad jer je Pajton uveo
# da su dicti poredjani po redu po difoltu
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)  # True

# Datetime
#datetime.time(datetime.time(5, 45, 5))
print(datetime.date.today())

# Time (u dekoratorima), merimo vreme

# From array, bolje za performans od listi, ako necemo da koristimo generatore
arr = array('i', [1, 2, 3])
print(arr)
