"""Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of  country stamps.
Find the total number of distinct country stamps."""

N = int(input("Number of stamps: "))
stamp_set = set({})
for i in range(N):
    stamp = input("Which country is the stamp from? ")
    stamp_set.add(stamp)
print(len(stamp_set))