Inventory={}
n=int(input("Enter no. of products: "))
for i in range(n):
    code=input("Enter product code: ")
    name=input("Enter product name: ")
    price=float(input("Enter product price: "))
    qty=int(input("Enter product quantity: "))
    Inventory[code]=(name,price,qty)
try:
    file=open("inventory.txt","w")
    for code,data in Inventory.items():
        name,price,qty=data
        file.write(code+" "+name+" "+str(price)+" "+str(qty)+"\n")
    file.close()
    print("Inventory saved to file")
except:
    print("Error saving inventory to file")