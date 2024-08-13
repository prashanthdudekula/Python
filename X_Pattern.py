n=int(input())
for i in range(n):
    for j in range(n):
        if(i-j==0)or (i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
