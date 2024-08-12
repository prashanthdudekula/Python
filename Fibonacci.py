n=int(input("Enter a number for Fibonacci Series : "))
n1,n2=0,1
print("{}\n{}".format(n1,n2))
for i in range(2,n):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
