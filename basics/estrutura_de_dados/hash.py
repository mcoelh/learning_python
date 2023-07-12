""" Given an integer, n, and n space-separated integers as input, create a tuple,
 t, of those n integers. Then compute and print the result of hash()."""

n = int(input())
integer_list = map(int, input().split())
t = (*integer_list,)
ret = hash(t)
print(ret)