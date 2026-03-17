a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    no=int(input("Enter a number: "))
    a.append(no)
print(a)
n=int(input("Enter an element to remove: "))
a.remove(n)
print(a)