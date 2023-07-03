'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
runner-up score refers to the second-highest score in a list of scores.

'''
import sys

n = int(input("Inform how many elements do you want to put in the list: "))
arr = list(map(int, input("Insert the numbers separated by empty spaces: ").split()))
my_list = []
if len(arr) != n:
    print("The list should have {} elements. The program will be terminated.\nTry again later.".format(n))
    sys.exit()
for num in arr:
    if num not in my_list:
        my_list.append(num)
temp = my_list[0]
for first in my_list:
    if first > temp:
        temp = first
my_list.remove(temp)
temp = my_list[0]
for runner_up in my_list:
    if runner_up > temp:
        temp = runner_up
print(temp)
