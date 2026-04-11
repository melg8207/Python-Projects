library={}
n=int(input("Enter the number of books: "))
for i in range(n):
    isbn=input("Enter the ISBN number: ")
    title=input("Enter the title of the book: ")
    author=input("Enter the author of the book: ")
    avail=input("Is the book available? (yes/no): ")
    library[isbn]=(title, author, avail)
try:
    f=open("library.txt", "w")
    for isbn,data in library.items():
        f.write(isbn+" "+data[0]+" "+data[1]+" "+data[2]+"\n")
    f.close()
except Exception as e:
    print("An error occurred while writing to the file:", e)
try:
    x=input("Enter the ISBN number to search: ")
    if x in library:
        if library[x][2].lower()=="yes":
            print("The book is available.",library[x][0])
        else:
            print("The book is not available.")
    else:
        print("The book with ISBN number", x, "is not found in the library.")
except Exception as e:
    print("An error occurred while searching for the book:", e)