"""
Consider a list (list = []). You can perform the following commands:

1 insert i e: Insert integer e at position i.
2 print: Print the list.
3 remove e: Delete the first occurrence of integer e .
4 append e: Insert integer e at the end of the list.
5 sort: Sort the list.
6 pop: Pop the last element from the list.
7 reverse: Reverse the list.
Initialize your list and read in the value of n followed by n 
lines of commands where each command will be of the  7 types 
listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""

N = int(input())
commands = []
for i in range(N):
    name, *line = input("Insert a command and its argument: ").split()
    arguments = list(map(int, line))
    commands.append([name] + arguments)

ret_list = []
for cmd in commands:
    if(cmd[0] == "insert"):
        if (len(cmd) == 3):
            ret_list.insert(cmd[1], cmd[2])
        else:
            print("Error!\nInsert method requires 2 arguments.")
    elif(cmd[0] == "print"):
        print(ret_list)
    elif(cmd[0] == "remove"):
        ret_list.remove(cmd[1])
    elif(cmd[0] == "append"):
        ret_list.append(cmd[1])
    elif(cmd[0] == "sort"):
        ret_list.sort()
    elif(cmd[0] == "pop"):
        ret_list.pop()
    elif(cmd[0] == "reverse"):
        ret_list.reverse()
