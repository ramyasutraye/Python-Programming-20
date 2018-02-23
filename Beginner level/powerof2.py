def main():
	try:
		n=0
		a=int(input())
		while(a!=0):
			a=a/2
			if a==1:
				n=1
				break
		if n!=1:
			print('no')
		else :
			print('yes')
	except:
		print('invalid')
main()
