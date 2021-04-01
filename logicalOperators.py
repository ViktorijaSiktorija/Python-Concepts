# and, or, not,>, <, ==, !=

print('a' > 'A')  # true
print('a' > 'b')  # false
print(1 <= 2 < 3 < 4)
print(0 != 0)
print(not(True))  # not je keyword i funkcija
print(not(1 == 1))  # false, jer not radi suprotno, 1 jednako 1,not ispred->false

is_magician = True
is_expert = False

if is_expert and is_magician:
    print("bravo")
elif is_magician and not is_expert:
    print("pokusavas")
elif not is_magician:
    print("treba ti magija")

# is je bukvalno vrednost, true is true, 1 is 1
print(1 is 1)  # broj je u memoriji na jednoj lokaciji
print(True is 1)
print([] is [])  # false, jer su 2 liste, nisu bukv iste
# isto false, jer su liste data structure, nalaze se na
print([1, 2, 3] is [1, 2, 3])
# drugacijim lokacijama
