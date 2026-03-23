try: 
    a=10
    b=0
    result = a/b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid value.")

try:
    lst=[10,20,30]
    index=int(input("Enter the index to access: "))
    print("Element: ", lst[index])
except IndexError:
    print("Error: Index out of bounds.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")

try:
    a="10"
    b=5
    print(a+b)
except TypeError:
    print("Error: Cannot add a string and an integer.")

try:
    d={"name":"Raja","age":25}
    print(d["address"])
except KeyError:
    print("Error: Key not found in the dictionary.")

try:
    lst={1,2,3,4}
    index=int(input("Enter index: "))
    print("Element: ", lst[index])
except IndexError:
    print("Error: Index out of bounds.")

try:
    lst=[10,20,30]
    value=int(input("Enter a value to remove: "))
    lst.remove(value)
    print("Updated list: ", lst)
except ValueError:
    print("Error: Value not found in the list.")

try:
    s="Python"
    index=int(input("Enter index: "))
    print("Character: ", s[index])
except IndexError:
    print("Error: Index out of bounds.")

try:
    t=(1,2,3)
    t[1]=10
except TypeError:
    print("Error: Tuples are immutable and cannot be modified.")