a,b,c=map(int,input("Enter Three Numbers : ").split(","))
max_val=a if a > b and a > c else b if b > c else c
print(max_val)
