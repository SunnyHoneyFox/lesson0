grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
students.sort()
#print(students)
a = (grades[0])
a = sum([5, 3, 3, 5, 4]) / len([5, 3, 3, 5, 4])
#print(a)
b = (grades[1])
b = sum([2, 2, 2, 3]) / len([2, 2, 2, 3])
#print(b)
c = (grades[2])
c = sum([4, 5, 5, 2]) / len([4, 5, 5, 2])
#print(c)
d = (grades[3])
d = sum([4, 4, 3]) / len([4, 4, 3])
#print(d)
e = (grades[4])
e = sum([5, 5, 5, 4, 5]) / len([5, 5, 5, 4, 5])
#print(e)
marks = [a, b, c, d, e]
#print(marks)
marks_students = dict(zip(students, marks))
print(marks_students)




