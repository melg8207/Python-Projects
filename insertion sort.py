size=int(input("Enter size of the array: "))
arr1=[]
for i in range(size):
    print("Enter elements: ")
    n=int(input())
    arr1.append(n)
print("Enter position to insert element: ")
pos=int(input())
print("Enter element to insert: ")
e=int(input())
arrcopy=arr1.copy()
arr1.insert(pos,e)
print("Array before insertion: ",arrcopy)
print("Array after insertion: ",arr1)