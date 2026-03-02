vowels=0
sentence=str(input("Enter a string: "))
for i in range(len(sentence)):
    if sentence[i].lower()=="a" or sentence[i].lower()=="e" or sentence[i].lower()=="i" or sentence[i].lower()=="o" or sentence[i].lower()=="u":
        vowels+=1
words=len(sentence.split())
print("Number of vowels:",vowels)
print("Number of words:",words)