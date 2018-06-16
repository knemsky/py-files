x = int(input("Please enter an integer for x: "))
y = int(input("Please enter an integer for y: "))
z = int(input("Please enter an integer for z: "))

check_var1 = True
check_var2 = True
check_var3 = True

if x%2 == 0:
    check_var1 = False
if y%2 == 0:
    check_var2 = False
if z%2 == 0:
    check_var3 = False

highest = [0,0,0]


if check_var1 == True:
    highest[0] = x
if check_var2 == True:
    highest[1] = y
if check_var3 == True:
    highest[2] = z

highest = max(highest)

if highest == 0:
    print("None of the values are odd")
else:
    print("The largest odd number is: "+str(highest))