# Setovi dozvoljavaju brojeve koji nisu duplikati tj samo jedinstvene

my_list = {num*2 for num in range(0,100)}
power = {num**2 for num in range(0,100)}
#print(power)
# da se zadrza samo celi, mora if uslov, ide na kraju
even = {num**2 for num in range(0,100) if num % 2 ==0}
print(even)