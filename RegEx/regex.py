# potreban je modul
import re


sting = 'trazi ovde nesto trazi'

# search
a = re.search('ovde', sting)  # dobije se match objekat

# span - pokaze indekse gde se nalazi u fromi tupla
print(a.span())
# start - ineks odakle pocinje trazeni string
# end - pokaze end
print(a.start())
# group - pokaze deo stringa de je match
print(a.group())

# umesto kucanja dodamo patern
pattern = re.compile('trazi')

b = pattern.search(sting)
print(b.group())

# findall - trazi sve instance match-a, izadje lista
c = pattern.findall(sting)
print(c)

# fullmatch - mora da bude tacan match tj isto poklapanje
# match - trazi tacan deo stringa i pokaze ako nadje
d = pattern.match(sting)
print(d)
