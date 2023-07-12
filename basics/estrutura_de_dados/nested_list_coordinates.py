"""
Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions
of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k)
on a 3D grid where the sum of i, j, k is not equal to n!
"""

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
z = int(input("Digite outro número: "))
n = int(input("Digite o último número: "))

my_list = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if ((i + j + k) != n):
                my_list.append([i, j, k])

print(my_list)