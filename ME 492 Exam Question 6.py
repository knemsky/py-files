#Kurtis Nemsky

mylist_course = []
mylist_grade = []

for n in range(50):
    x = str(input("Please type the name of your course (type 0 to exit): "))
    if x == '0':
        break
    y = int(input("Please type the course grade: "))
    mylist_course.append(x)
    mylist_grade.append(y)

GPA = sum(mylist_grade)/len(mylist_grade)

print("REPORT CARD:")
print("\n")
N = len(mylist_course)

for z in range(N):
    print(str(mylist_course[z]) + " - " + str(mylist_grade[z]))
    print("\n")
print("Overall GPA - " +str(GPA))