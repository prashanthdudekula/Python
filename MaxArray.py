arr=[12,5,18,30,74,3]
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print("Maximum Element in Array:",max)
