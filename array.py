a=int(input("Enter size of the array: "))
arr=[]
for i in range(a):
    n=int(input("Enter element: "))
    arr.append(n)
print("Enter element to insert: ")
e=int(input())
pos=int(input("Enter position to insert element: "))
arrcopy=arr.copy()
arr.insert(pos,e)
print("Array before insertion: ",arrcopy)
print("Array after insertion: ",arr)