# comp sciense term
# one su one time anonimne funkcije koje nam ne trebaju vise od 1 puta
# lambda param: action(param)

my_list = [1,2,3]
print(list(map(lambda num: num*2, my_list)))
# moze i sa map i filter
from functools import reduce
print(reduce(lambda acc,item: acc+item, my_list))

# Square
moja_lista = [5,6,7]
print(list(map(lambda num: num**2, moja_lista)))

# List Sorting sa razl key-ovima, moze i sa dictionary 
a = [(0,2), (4,3), (10,-1), (9,9)]
# key za sort funkciju je da iterise kroz svaki item koji cu dobiti
# x je tuple, ocu da koristim vrednost drugog itema tj [1]
# da je x[0] to je prvi item, onda bi sortirao prema prvom item u tuplu
a.sort(key=lambda x: x[1])
print(a)