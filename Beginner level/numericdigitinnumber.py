def count(x):
	c=0
	while(x!=0):
		x//=10
		c+=1
	print(c)
def main():
	try:
		x=int(input())
		count(x)
	except:
		print('invalid')
main()
