# klase se pisu kamel kejsom
# u Pajtonu ne postoje direkt privatne i javne promenljive,
# doda se _ ispred imena metode/promenljive, to je samo konvencija
# da ne mogu da se menjaju

class BigObject:
    pass


obj1 = BigObject()  # instantiate
print(type(obj1))


class PlayerCharacter:
    # class object atribut - nije dinamican tj statican je
    membership = True
    # mogu i difolt parametri, age=0 itd

    def __init__(self, name, age):  # __init__ posebna metoda DUNDER/MAGICNA metoda,
        # constructor metoda, automatski se zove kada instanciramo
        # if age > 18:
        self._name = name  # self nacin da definisemo klasu
        self._age = age  # atributi/propertis koje objekti imaju, dinamicni su i
        # jedinsvetni za taj objekat

    def run(self):  # fja
        print('ja sam ' + self._name)
        # return 'done'

    # @classmethod - decorator, ne koriste se cesto
    @classmethod
    def add_things(cls, num1, num2):  # cls je class
        return num1+num2

    # @staticmethod - nemamo pristup klasi(cls), samo radimo neku metodu
    # koristimo kada nas ne zanimaju atributi
    @staticmethod
    def add_things2(num1, num2):
        return num2+num1

    def speak(self):
        print('ja se zovem ' + self._name)


player1 = PlayerCharacter('Vika', 44)  # instanciranje
player2 = PlayerCharacter('Koko', 2)
print(player2._age)
print(player1._age)
print(player1.run())
print(player2.membership)
print(player2.run())
print(player1.add_things(2, 3))
print(player1.speak())
# help
# help(player1)
