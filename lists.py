# List: ordered sekvenca objekata koji mogu biti bilo kog tipa
#  mutable, allows duplicate elements
# one su kao arej
# sa []

myList = ["la","ku","ku","ku"]
print(myList)
print(myList[0])
myList[1] = 'ki' #mutable su za razliku od stringa
print(myList)

myList2 = list()
print(myList2)

# count - koliko puta se ponavlja
print(myList.count('ku')) # kada je bilo 1 ku,pisalo je 0?
# sa 3 ku pise 2

# index
print(myList.index('la'))

# -1 poslednji element, -2 pretposlednji itd
item = myList[-1]
print(item)

# in
print("ku" in myList) # true

#range - nova lista
print(list(range(101))) #do 100

# lupovanje
for i in myList:
    print(i)

# proverimo dal je item u listi
if "la" in myList:
    print("yes")
else: 
    print("no")

# koliko je elemenata u listi
print(len(myList))

# dodavanje itemsa:
myList.append("llimun")
print(myList)

# ako hocemo da dodamo na odredjeno mesto
myList.insert(1, "malina")
print(myList)

# extends
# uzme iterable, listu, ne stvara novu nego menja originalnu
new_list = myList.extend([100,101])
print(myList)
print(new_list)

# remove items:
# pop uzima poslednji element i vraca ga
item = myList.pop(2) #izbacuje po indeksu
print(item)

# remove odredjeni element
item = myList.remove("la")
print(myList)

# brisanje svih elemenata
#item = myList.clear()
print(myList)

# reverse liste
item = myList.reverse()
print(myList)

# sort - po alfabetu ili rastuce po brojevima
# menja originalnu listu
myList2 = [4,3,2,-3,-6]
item = myList2.sort()   
print(myList2)

# sorted ali da ne menja originalnu, nego da pravi novu listu
new_List = sorted(myList2)
print(myList2)
print(new_List)

# da se napravi nova lista sa istim elementima vise puta
myList3 = [0] * 5
print(myList3)

# concat/spajanje 2 liste
myList4 = [1,2,3,4,5]
new_List2 = myList4 + myList3
print(new_List2)
# join, nova string za list of items
nova_sentence = " ".join(['cao','ja','sam','vika'])
print(nova_sentence)

# kopiranje liste
list_original = ["banana", "jabuka", "jagoda"]
list_cpy = list_original 
# ako promenimo cpy,menja i originalnu listu
list_cpy.append("limun")
print(list_cpy)
print(list_original)

# pravo kopiranje, copy()
list_original = ["banana", "jabuka", "jagoda"]
#list_cpy = list_original.copy()
print(list_cpy)

# list funkcija za kopiranje i slicing

# list comprehension - stvaranje nove liste od postojece sa 1 linijom
c = [1,2,3,4,5]
d = [i*i for i in c]
# znaci 1 puta 1, 2 puta 2 itd
print(c)
print(d)

# slicing - da pristupimo delovima liste sa :
# sa tim pravimo novu listu, ne utice na originalnu,pravimo novu kopiju
# mutable je jer mozemo sa indeksom da menjamo
novaLista = [1,2,3,4,5,6,7,8,9]
a = novaLista[1:5]
b = novaLista[1:5:2]
# bez prvog ide od pocetka, ako ne odredimo stop ide do kraja
# npr :5 od pocetka, 1: ide do kraja, [:] je sve
print(novaLista)
print(a)
print(b)
# optional step indeks [::1] - uzme svaki item, [::2] - uzme svaki drugi item
# [::-1] - da se obrne lista, stvara novu listu
novaLista2 = novaLista
novaLista[1] = 58
print(novaLista2)
print(novaLista) # menja i original jer smo ih izjednacili!

# Matrix - multi dimensional liste
matrix = [
    [1,2,3],#ovo je [0]
    [2,4,6],
    [7,8,9]
] #ovo je dvodimenzionalna
print(matrix[0][1])
basket = [
"Banana", 
["Apples", 
["Oranges"], 
"Blueberries"]
]
print(basket[1][1]) #ili [1][1][0]

# list unpacking (kao za promenljive)
a,b,c,d,e,f,g,h,i =[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
#print(other), sa *other mi ne radi
print(d)