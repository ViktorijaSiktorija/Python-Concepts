# users
# koji si su wizards,archers itd al svi moraju da budu signed in
# children klases se nekada zovu sub klases ili derived klase

# base object class u objektu je "object", od njega sve nastaje tj built in metode
# on je kao parent class svima


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('loged in')


class Wizard(User):
    def __init__(self, name, power, email):
        # super keyword - odnosi se na klasu iznad tj User
        # ne moramo da prosledjujemo self, samo email is User
        # super().__init__(email)
        self.name = name
        self.power = power
        self.email = email

    def attack(self):
        print("attackign with power of " + self.name)


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print("attackign with power of arrows " + self.name)


class HybridBorg(Wizard, Archer):  # visestruko nasledjivanje
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        # Wizard.__init__(self, name, power) ne radi


hb1 = HybridBorg('borgi', 50, 100)
print(hb1.sign_in())

wizard1 = Wizard('Merlin', 50, 'merlin@gmail')
archer1 = Archer('Robin', 100)

print(wizard1.email)


def player_attack(char):  # polimorfizam
    # over riduje default attack metodu iz usera
    char.attack()


for char in [wizard1, archer1]:
    char.attack()

player_attack(wizard1)
# metode:
wizard1.attack()
archer1.attack()
# nasledjivanje:
print(wizard1.sign_in())

# isinstance - da proverimo dal je instanca
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True
print(isinstance(wizard1, object))  # True

# Object introspekcija - sposobnost da odredimo tip objekta at runtime
# Runtime - kada je kod pokrenut
print(dir(wizard1))  # attack, email, name,power, sign in

# MRO - Metod Resolution Order
# komplikovano je i retko se koristi


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
# print(D.mro())
# u vs cod izadje 10 i da ne postoji mro atribut
# u repl izadje 1 i radi mro
