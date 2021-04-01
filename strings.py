# ''' su za dugacke stringove
dugi_string = '''vau VAU 0000''' #vau VAU 0000
#ako se ispise vau pa ispod vau pa ispod nule, izacice jedno ispod drugog
print(dugi_string)

# Concat
first_name = 'Vika'
prezime = 'Lukic'
punoIme = first_name + ' ' + prezime
print(punoIme)

# Escape Sequence - za ' i "" i \, za \ je \\
# \t -> za tab
# \n -> novi red
vreme = "It\'s \\\"sunny\" \n imaj lep dan!"
print(vreme)

# Formatted Strings
name = 'Vika'
age = 30
#f - formated string
#print(f'hi {name}. Ti imas {age} godina') -> ovo ne radi, radi u repl
# ranije je bilo ... .format('Vika','30')

name = "John"
age = 23
print("%s is %d years old." % (name, age))
print('hi {0}. imas {1} godina'.format(age,name))
print('hi {novo_ime}. Imas {nove_godine} godina'.format(novo_ime='Pera', nove_godine=100))

# String indexes
ja = 'ja ja ja'
brojevi = '01234567'
# [start:stop:stepover] - string slicing
print(ja[0:8:2])
print(brojevi[1:])
print(brojevi[:5])
print(brojevi[::1])
# -1 kraj stringa, -2 pretposlednji itd
print(brojevi[-1])
# ::-1 je obrtanje stringa ::-2 preskace po 2
print(brojevi[::-1])

# Immutability
# stringovi u Pajtonu su imjutabl, ne mogu da se menjaju
# ne moze ovo: brojevi = '01234' brojevi[0]='8'
# sa re asign vrednost tako se menja
