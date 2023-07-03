'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

If there are multiple students with the second lowest grade, order their names alphabetically and print 
each name on a new line.

The first line contains an integer, N , the number of students.
The 2nd subsequent lines describe each student over  2 lines.
- The first line contains a student's name.
- The second line contains their grade.
'''


my_list = []
new_list = []
for _ in range(int(input("How many students? "))):
    name = input("{} student name: ".format(_ + 1))
    score = float(input("{} student grade: ".format(_ + 1)))
    my_list.append([name, score])

temp = my_list[0]
i = 0
while (i < len(my_list)):
    if temp[1] > my_list[i][1]:
        temp = my_list[i]
    i += 1

i = 0
while (i < len(my_list)):
    if (temp[1] != my_list[i][1]):
        new_list.append(my_list[i])
    i += 1

my_list = []
temp = new_list[0]
i = 0
while (i < len(new_list)):
    if (temp[1] > new_list[i][1]):
        temp = new_list[i]
    i += 1

i = 0
while( i < len(new_list)):
    if (temp[1] == new_list[i][1]):
        my_list.append(new_list[i])
    i += 1

flag = True
i = 0
while (flag):
    flag = False
    for i in range(len(my_list) - 1):
        if (my_list[i][0] > my_list[i + 1][0]):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            flag = True

for student in my_list:
    print(student[0])