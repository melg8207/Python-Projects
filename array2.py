a=int(input("Enter size of the array: "))
arr=[]
for i in range(a):
    n=int(input("Enter element: "))
    arr.append(n)
print("Enter element to delete: ")
e=int(input())
arrcopy=arr.copy()
arr.__delitem__(arr.index(e))
print("Array before deletion: ",arrcopy)
print("Array after deletion: ",arr)