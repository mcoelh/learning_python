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

lowest_score = my_list[0][1]
for student in my_list:
    if lowest_score > student[1]:
        lowest_score = student[1]

for student in my_list:
    if student[1] != lowest_score:
        new_list.append(student)

second_lowest = new_list[0][1]
for student in new_list:
    if second_lowest > student[1]:
        second_lowest = student[1]

my_list = []
for student in new_list:
    if student[1] == second_lowest:
        my_list.append(student)

flag = True
while (flag):
    flag = False
    for i in range(len(my_list) - 1):
        if (my_list[i][0] > my_list[i + 1][0]):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            flag = True

for num in my_list:
    print(num[0])

"""
More simplified version by chatGPT:

my_list = []
for _ in range(int(input("How many students? "))):
    name = input("{} student name: ".format(_ + 1))
    score = float(input("{} student grade: ".format(_ + 1)))
    my_list.append([name, score])

lowest_score = min(student[1] for student in my_list)
new_list = [student for student in my_list if student[1] != lowest_score]

second_lowest = min(student[1] for student in new_list)
my_list = [student for student in new_list if student[1] == second_lowest]

my_list.sort()

for student in my_list:
    print(student[0])


"""