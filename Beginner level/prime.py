m=int(input(""))
n=int(input(""))
for i in range(m,n):
    for j in range(2, i):
        if i%j == 0:
            break
        else:
            print(i)
            
