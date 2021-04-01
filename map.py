def mnozenje_sa2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

# sa map ne treba stvaranje liste, pa append
# mora sa list, jer map samo pokaze gde je vrednost u memoriji
# automatski lupuje map objekat, koji pretvorimo u listu
my_list = [1,2,3]
# map nece uticati na my_list
# jer je mnozenje_sa22 "cista funkcija",ne utice na spoljasnji svet
# i uvek ima isti autput
def mnozenje_sa22(item):
    return item*2
print(list(map(mnozenje_sa22,[1,2,3])))
print(my_list)


