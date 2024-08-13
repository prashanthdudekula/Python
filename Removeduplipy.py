li1=list(map(int,input("Enter data : ").split(" ")))
li2=[]
for i in li1:
    if i not in li2:
        li2.append(i)
print(li1)
print(li2)
