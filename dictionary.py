# u drugim jezicima hash table/map/objekat
# data tip ali i data struktura
# SA {}, key-value pair
# unordered - nisu jedna pored druge u memoriji, za razliku od liste
dictionary = {
    'a': [1,2,3],
    'b': 'helllo',
    'x': True
}
print(dictionary['a'][1])

my_list = [{
    'a': [1,2,3],
    'b': 'helllo',
    'x': True
},
{
    'a': [4,5,6],
    'b': 'helllo',
    'x': True
}]
print(my_list[0]['a'][2])

# keys
# moraju da imaju poseban properti, mora da bude imutable (npr broj, bool, string)
# mora da bude jedinstven
dict2 = {
    123: [1,2,3],
    True: 'hello'
}
print(dict2[123])

# get
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}
print(user.get('age', 55)) #None,pa dodamo vrednost ako ne postoji age

# dict funkcija
user2 = dict(name='Pera')
print(user2)

# in
# za trazenje
print('greet' in user) # Ako nema, false

# keys, proverava kljuceve (i vrednosti)
print('age' in user.keys())

# items, uzme ceo item
print(user.items())

# clear
# print(user.clear()) 

# copy , kopiramo
user3 = user.copy()
print(user)
print(user3)

# pop, sklanja key i value
print(user.pop('age'))

# popitem, rendum nesto skloni
print(user.popitem())
print(user)

# update, i ako nema age idalje ce ga apdejtovati
print(user.update({'age':55}))
print(user)