# Tuples su coleciton data tipovi koji su ordered i immutable, mogu duplikati elemenata
# slicno listi ali ne moze da se menja nakon sto se napravi
# ne moze sort, reverse
# cesto se koristi za objekte koji pripadaju zajedno
# ()

# zagrade nisu obavezne
mytuple = ("Vika", 28, "Beograd")
print(mytuple)

# ako ima samo jedan element, ne prepoznaje ga kao tupl
mytuple1 = ("Vile")
print(type(mytuple1))
# prepoznaje ga kao string, onda se doda , na kraj
mytuple1 = ("Vile",)
print(type(mytuple1))

# tupl moze da se stvori preko tupl funkcije, da se stvori od iteratora 
# npr liste
mytuple = tuple(["Vika", 29, "Ulica"])
print(mytuple)

# pristup elementima preko indeksa
item = mytuple[0]
print(item)
# -1 poslednji element, -2 pretposlednji itd

# ako hocemo da menjamo elemente
#mytuple[0] = "Tima"
print(mytuple)
# ovo je nemoguce, jer je tupl immutable

# lupovanje
for i in mytuple:
    print(i)

# proverimo dal je item u listi
if "la" in mytuple:
    print("yes")
else: 
    print("no")

# koliko je elemenata u listi
print(len(mytuple))

# za brojanje
print(mytuple.count('V'))

# za indeks elementa
print(mytuple.index(29))

# konvertovanje tupla u listu i obrnuto
myList = list(mytuple)
print(myList)
mytuple2 = tuple(myList)
print(mytuple2)

# slicing - da pristupimo delovima tupla sa :
a = (1,2,3,4,5,6)
b = a[2:5]
print(b)
# bez prvog ide od pocetka, ako ne odredimo stop ide do kraja
# npr :5 od pocetka, 1: ide do kraja

# optional step indeks [::1] - uzme svaki item,
# [::2] - uzme svaki drugi item
# [::-1] - da se obrne tupl

# unpacking
my_tuple = "Max", 28, "Pariz"
name, age, city = my_tuple
print(age)
print(name)
print(city)
# mora da se poklapa broj sa elemntima u tuplu
# unpack vise elemenata sa *
my_tuple = (0,1,2,3,4)
#i1, *i2, i3 = my_tuple -> ovo kaze da ne valja
#print(i1)
#print(i3)
#print(i2) #svi elementi izmedju 1 i 3, sada pretvoreni u listu

# poredjenje tupla i liste, lista je veca
# sa import sys, i getsizeof metodom
import sys
my_list = [0,1,2,"cao"]
my_tuplee = (0,1,2,"cao")
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuplee),"bytes")
# poredjenje vremena sa timeit modulom
# brzi su tupls, tj efikasniji su od liste
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4)",number=1000000))
