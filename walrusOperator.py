# :=
# u izrazu kada se nesto procenjuje

a = 'Kokili'
if ((n := len(a)) > 10):
    print("too long " + n + "elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
print(a)