a=[]
sum=0
n=int(input("Enter the number of elements: "))
for i in range(n):
    no=int(input("Enter a number: "))
    a.append(no)
    sum+=no
print("Sum of the elements in the list is: ",sum)
