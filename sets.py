# unordered kolekcije jedinstvenih objekata

my_set = {1,2,3,4,5}
my_set.add(1000)
my_set.add(2) # ne dodaje jer vec ima 2
print(my_set)

# set funkcija
my_list = [1,2,3,4]
print(set(my_list))

# pristup preko itema, kao u dict
print(1 in my_set)

# duzina
print(len(my_set))

# kopiranje
my_set2 = my_set.copy() # nova kopija
my_set.clear()
print(my_set2)

# difference, poredjenje 2 seta
set1 = {'vika','jole','dus',5,6}
set2 = {5,6,'jagoda','banana','kajsija'}

print(set1.difference(set2))

# discard, izbaci
set1.discard(5)
print(set1)

# difference update, sklone se razlike izmedju 2 seta
set1.difference_update(set2) # menja, za razliku od difference
print(set1)

# intersection, daje zajednicke iteme 2 seta
print(set1.intersection(set2))

# is disjoint, da li imaju nesto zajednicko
print(set1.isdisjoint(set2)) # true

# union, spoji 2 seta, skloni duplikate, stvori novi set
print(set1.union(set2))
print(set1 | set2)

# is subset
print(set1.issubset(set2)) # false, nije set1 podskup set2

# is superset
print(set2.issuperset(set1)) # false, nema glavnog skupa i podskupa