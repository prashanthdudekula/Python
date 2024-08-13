n=int(input())
arr=list(map(int,input().split()))
even_sum=0
odd_sum=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even_sum+=arr[i]
    else:
        odd_sum+=arr[i]
print(even_sum,"",odd_sum)
