#str()
#int()
#type()
#print()
print(len('hello')) #length ne pocinje od indexa 0,nego od 1
greet = 'helllloooo'
print(greet[:]) # pokaze ceo string
print(greet[0:len(greet)]) # ceo pokaze

# Built in methods
# npr string methods
# imaju .ispred npr .format()
quote = 'biti ili ne biti'
print(quote.upper())
print(quote.capitalize()) # veliko slovo za prvu rec
print(quote.lower())
print(quote.find('be')) #pronadje indeks
print(quote.find('bi'))
print(quote.replace('bi', 'me')) # zamenjuje
print(quote) # vrati pocetnicki string,STRINGS SU IMMUTABLE!
quote2 = quote.replace('bi','me')
print(quote2)