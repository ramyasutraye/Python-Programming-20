import sys
def gcd():
	(a,b)=map(int,sys.stdin.readline().split())
	while(b!=0):
		t=b
		b=a%b
		a=t
	print(a)
try:
	gcd()
except:
	print('invalid')
