# koristimo kada nismo sigurni kolko puta treba da lupujemo

# break (radi i u for loop)
i = 0
while i < 50: #infinite loop
    print(i)
    break # da se zaustavi

i = 0
while i < 50:
    print(i)
    i += 1 # ili da uslov bude false
else: # radi ako nema break
    print("gotov")

my_list = [1,2,3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input('cao: ') 
    if (response == 'bye'): # ukuca se 'bye' u konzoli
        break

# continue
my_list = [1,2,3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue # ne moze print posle toga, jer continue nastavlja radnju

# pass (nije bas korisno, nista ne radi), ide na novi red
# sluzi vise kao komentar samo da ubacimo nesto kada ne znamo sta
# da radimo, da ne izlazi eror
    