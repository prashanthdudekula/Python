li=list(map(int,input().split()))
max=li[0]
for n in li:
    if n>max:
        max=n
print(max)
