# def - definisemo funkciju
# Funkcija ili menja nesto (kao print) u programu
# ili vraca nesto
def reci_cao():
    print('cao cao')


reci_cao()

# Positional!
# parametri - idu u zagrade
# to su promenljive koje sami pravimo, i koje koristimo unutar funkcije


def reci_cao2(name, emoji):
    print('cao ' + name + " " + emoji)


reci_cao2('Vika', ':)')

# argumenti - koriste se kao vrednosti koje prosledimo funkciji
# Vika i :) su argumenti

# keyword args - da ne brinemo o poziciji
reci_cao2(emoji=':))', name='Bibi')

# default parametri


def reci_cao3(name='vika', emoji=':D'):
    print('cao ' + name + " " + emoji)


reci_cao3()

# return - funkcije moraju da vrate nesto, u suprtonom None


def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))

# Metodu mora neko da poseduje . notacija,
# to su built in objekti koje liste, tuplovi itd preko . imaju pristup metodi

# Cist kod - fja koja vraca true ili false dal je broj ceo


def is_even(num):
    return num % 2 == 0


print(is_even(50))

# *args **kwargs


def funckccija(*args, **kwargs):
    total = 0
    for items in kwargs.values():  # argumenti se vracaju kao dict
        total += items

    # return sum(args) + total # u replit radi, u vs cod ne
print(funckccija(1, 2, 3, 4, 5))
# num1=5, num2=10)) ovo ne radi
# params, *args, default params, **kwargs

# max - vraca najveci br


def paran_broj(li):
    parni = []
    for num in li:
        if num % 2 == 0:
            parni.append(num)
    return max(parni)


print(paran_broj([3, 5, 2, 4, 8]))
