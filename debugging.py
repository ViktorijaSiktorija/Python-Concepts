# pdb - Pajton debager, built in modul
import pdb


def add(num1, num2):
    pdb.set_trace()  # help, list ili help list
    t = 4+5
    return num1+num2  # step, ide na sledecu liniju


# a, w, next, continue, unutar mogu da se menjaju promenljive
add(4, 5)
