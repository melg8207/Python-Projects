student1={"name":"Ali","age":20,"course":"BCA"}
print("Student Details: ",student1)

student2={"name":"Sara","age":21,"course":"MCA"}
print("Name: ",student2["name"])
print("Age: ",student2["age"])

student3={"name":"John","age":22}
student3["course"]="BCA"
print(student3)

d={"a":10,"b":20,"c":30}
for key in d.keys():
    print(key)
for value in d.values():
    print(value)

f={"a":10,"b":20,"c":30}
for k,v in f.items():
    print(k,":",v)

e={"a":10,"b":20,"c":30}
key=input("Enter the key to search: ")
if key in e:
    print("Key found. Value: ",e[key])
else:
    print("Key not found.")

s={10,20,30,40}
print("Set elements: ",s)

g={10,20,30,40}
g.remove(20)
print("Set after removing: ",g)

a={1,2,3}
b={3,4,5}
print("Union: ",a.union(b))
print("Intersection: ",a.intersection(b))
x={1,2}
y={3,4}
print(x.difference(y))
a1={1,2,3}
a2={3,4,5}
print("Symmetric Difference: ",a1.symmetric_difference(a2))

a3={1,2,3,4}
b4={3,4,5,6}
result=a3^b4
print("After removing common elements: ",result)

x1={1,2,3,4}
x2={2,3,5}
x3={2,3,6}
common=x1&x2&x3
print("Common elements: ",common)