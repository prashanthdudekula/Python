str=input("Enter a string : ")
word=input("Enter a word which on you want to delete: ")
for i in str:
    if i==word:
        continue
    else:
        print(i,end="")
