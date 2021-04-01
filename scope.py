# Scope - koje promenljive imam pristup
# Function scope

# Prvo gledal local scope, local u funkciji
# Ako nema u local scope, dal ima parent local scope, ako nema to onda
# Global, sta god ima fajl to je global
# Built in Pajton funkcije (sum npr)

a = 1
def fja():
    a = 5
    return a
print(a)
print(fja())

# Parametri imaju local scope

# Global keyword - ako ima global
total = 0
def count():
    global total 
    total += 1
    return total

print(count())
# nije bas dobro, bolje dependency injection, umesto pristupa
# promenljivim koje su van fje, stavimo kao parametar
total = 0
def countt(total):
    total += 1
    return total
print(countt(countt(countt(total))))

# nonlocal keyword, novi feature
# odnosi se na parent local
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
