def composite():
	a=int(input())
	l=[]
	f=0
	for i in range(1,a//2+1):
		if a%i==0:
			l.append(i)
	l.append(a)
	for i in l:
		print(i)
try:
	composite()
except:
	print('invalid')
