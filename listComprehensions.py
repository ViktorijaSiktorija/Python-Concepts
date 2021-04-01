# list comprehension - stvaranje nove liste od postojece sa 1 linijom
# Comprehension postoji za liste, setove i dictionarije
c = [1,2,3,4,5]
d = [i*i for i in c]
# znaci 1 puta 1, 2 puta 2 itd
print(c)
print(d)

my_list = [num*2 for num in range(0,100)]
power = [num**2 for num in range(0,100)]
print(power)
# da se zadrza samo celi, mora if uslov, ide na kraju
even = [num**2 for num in range(0,100) if num %2 ==0]
print(even)

# Duplikati
# count -> kolko puta se item pojavljuje u listi
lista = ['a','b','b','c','d','e','e']
# set() funkcija pretvara listu u set, i onda nema duplikata
# tj rezultat nije bb ee, nego b i e
# i list je vraca u listu od seta
duplicates = list(set([slovo for slovo in lista if lista.count(slovo)>1]))
print(duplicates)


