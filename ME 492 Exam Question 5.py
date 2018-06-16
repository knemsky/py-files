#Kurtis Nemsky

mylist = [5,4,3,2,1,0]
x = int(input("Please type a value for x: "))
result2 = 0

for n in mylist:
    result1 = n*(x**n)
    result2 = result1 + result2

print(result2)