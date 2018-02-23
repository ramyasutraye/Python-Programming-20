x=int(input("enter no. of terms"))
a=0
b=1
count=0
if(x==0):
        print(a)
elif(x<0):
        print("enter  valid number")
else:
        while(count<x):
            print(a)
            term= a+b
            a=b
            b=term
            count+=1
