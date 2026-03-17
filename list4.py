a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    no=int(input("Enter a number: "))
    a.append(no)
print(a)
pos=int(input("Enter the position to insert an element: "))
n=int(input("Enter an element to insert at position "+str(pos)+": "))
a.insert(pos,n)
print(a)