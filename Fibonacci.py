n=int(input())
a=0
b=1
print("Fibonacci Sequence")
i=0
print("{}\n{}".format(a,b))
while(i<n-2):
    sum=a+b
    print(sum)
    a=b
    b=sum
    i+=1
    
