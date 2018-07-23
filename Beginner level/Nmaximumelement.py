def largest(arr,n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
a=input(" ")
print(a)    
arr = input(" ")
print(arr)
n = len(arr)
Ans = largest(arr,n)
print(Ans)
