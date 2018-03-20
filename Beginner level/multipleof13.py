def multiple13():
	m=int(input())
	if m%13==0:
		print('yes')
	else :
		print('no')
try:
	multiple13()
except:
	print('invalid')
