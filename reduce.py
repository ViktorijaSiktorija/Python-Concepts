# reduce nije built in funkcija
# mora da se importuje
# functools je kao drzac za alate
# prosledjuje joj se funkcija, sequence, initial
from functools import reduce

my_list = [1,2,3]
def acumulator (acc,item):
    print(acc,item)
    return acc + item

# ne mora u listu da se pretvara
# map i filter koriste reduce u pozadini
print(reduce(acumulator, my_list, 20))