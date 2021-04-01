import re

# Email
# ^ pocetak, da ima u sebi slova i brojeve i _ . + =
# + da ih bude kolko ocemo, @
# isto plus \. koji je tacka bukvalna
# $ je za kraj
patern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = "siktorija123.viktorija@gmaiiiiil.com"  # ako se ne poklapa, izadje none

a = patern.search(email)
print(a)

# Pasword

# ^ pocetak, slova, brojevi i $ % # @
# da ih bude najmanje 8 {8,}
# \d digit, da se zavrsi brojem ili [0-9]
patern1 = re.compile(r"(^[a-zA-Z0-9$%#@]{8,}\d$)")
password = "ffjnf3jn#2"
a = patern1.search(password)
b = patern1.fullmatch(password)
print(b)
print(a)
