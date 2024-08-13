n=int(input())
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print(n,"Not a Prime number")
            break
        else:
            print(n,"is a Prime number")
    else:
        print("Enter a Positive number")
        
