# generalno ne treba da se over rajtuju, ali mogu ako treba

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.dictt = {
            'name': 'vika',
            'ima_psa': True
        }

    def __str__(self):
        return(self.color)

    def __len__(self):
        return 5

    def __call__(self):
        return('yesss')

    def __getitem__(self, i):
        return self.dictt[i]


figura = Toy('red', 0)
print(figura.__str__())
print(str(figura))
print(len(figura))
print(figura())
print(figura['name'])
# delete keyword brise neke promenljive


# list postaje parent class, da mozemo da iskoristimo metode liste:
class SuperList(list):
    def __len__(self):
        return 1000


s_l1 = SuperList()

print(len(s_l1))
s_l1.append(5)
print(s_l1[0])
# dal je superlista podklasa liste
print(issubclass(SuperList, list))
