# trebaju nam 2 liste/iteratora, koje "zipujemo" zejdno

my_list = [1,2,3]
your_list = [10,20,30]

print(list(zip(my_list, your_list)))
# [(1, 10), (2, 20), (3, 30)] -> uzme 2 iteratora, od svakog uzme 1. item i spoji ih
# 1 i 10 se dodaju zajedno u tuple, pa 2 i 20 itd
# nebitno je dal je lista ili tuple, samo da je iterator

their_list = (5,3,5)
print(list(zip(my_list, your_list, their_list)))
# [(1, 10, 5), (2, 20, 3), (3, 30, 5)]

