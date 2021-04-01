# exception - eror koji kresuje program
# Eror handling - da pazimo na erore
# typeEror - data tajps koji nisu kompatibilni, built in exceptions
# sintaks eror npr zaboravimo :
# name eror kada nije defined
# indeks eror za list , i dict key eror

# while True:
# try:
#age = int(input('kolko imas god'))
# print(age)
# 10/age

# raise ValueError('prestani plz') # ili raise Exception()

# except ValueError:  # ovo ne radi
#print('unesi broj')

# except ZeroDivisionError:

#print('mora vece od 0')
# else:  # ovo ne radi, radi u repl, ne izadje iz loopa u terminalu
# print('fala')

# finally: # obavlja se bez obzira na sve

# print('ok')
# break


def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum(1, 0))
print(sum(1, '2'))
