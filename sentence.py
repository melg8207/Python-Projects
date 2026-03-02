vowels=0
words=0
sentence=str(input("Enter a string: "))
for i in range(len(sentence)):
    if sentence[i]=="a" or sentence[i]=="e" or sentence[i]=="i" or sentence[i]=="o" or sentence[i]=="u":
        vowels+=1
for i in range(len(sentence)):
    if sentence[i]==" " or sentence[i]=="." or sentence[i]=="?" or sentence[i]=="!" or sentence[i]==",":
        words+=1
print("Number of vowels:", vowels)
print("Number of words:", words+1)