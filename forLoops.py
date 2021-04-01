for slovo in 'Viktorija':
    print(slovo)

# set
for item in {1,2,3,4,5}:
    for x in ['a','b','c']:
        print(item, x)

# iterator - objekat/kolekcija kroz koji mozemo da iterisemo
# da idemo 1 po 1, da proverimo svaki item u kolekciji

# iterables - list, dict, tuple, set, string

# Objekat - dictionary

user = {
    "name": "koko",
    "age": 2,
    "can_swim": False
}

# .() za key i vrednost
# keys() - za keys
for osobina in user.keys():
    print(osobina)
# izadje tapl sa key i vrednostima

# values() - za vrednosti
for osobina in user.values():
    print(osobina)

# items() - key i vrednost
for osobina in user.items():
    print(osobina)

# da izadju oba a da nisu tapl?
for k, v in user.items(): # key i value
    print(k, v)

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for broj in my_list:
    counter = counter + broj
print(counter)

# range ()
# objekat, vraca objekat koji vraca sekvencu intidzera
print(range(100)) # 0 je difolt, moze 50,100 npr

for i in range(0, 100, 2): # moze _ umesto i ili promenljive, kada je nebitna
    print(i) # 2 - ide po svaki drugi

for _ in range(10, 0, -1): # -1 da ide unazad, -2 svaki drugi
    print(_)

for _ in range(2): 
    print(list(range(10)))

# enumerate()
# uzme iterable, i daje indeks kaunter i item tog indeksa - i
for i, char in enumerate('Viktorija'):
    print(i, char)

for i, char in enumerate([1,2,3,4]):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i)

# Vezba

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fill = '*'
empty = ''
for row in picture:
    for pixel in row:
        if pixel:
            print(fill) #, end='') # end ne radi u VS cod, radi u repl
        else:
            print(empty) #end='')
    print('')

# Vezba 2
lista = ['a','b','c','b','d','m','n','n']
duplicates = []
for char in lista:  #prolaziš jedan po jedan kroz elemente prvog niza... 
    #i to po indexima.. prvo nulti, pa prvi, pa drugi itd do kraja niza
    if lista.count(char) > 1: #proveravaš da li je broj pojavljivanja 
        #trenutno uzetog elementa niza veći od 1 (znači da je duplikat u prvom nizu)
        if char not in duplicates: #ako je gornji  uslov zadovoljen 
            #(duplikat je u prvom nizu) proveravaš da nije već dodat u drugi niz
            duplicates.append(char) #ako su prethodna dva uslova zadovoljena (duplikat 
            #je u prvom nizu i nije već dodat u drugi niz) dodaješ element u drugi niz
print(duplicates)

  