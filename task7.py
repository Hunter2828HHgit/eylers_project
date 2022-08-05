def IsPrime(x):
	count = 0
	for i in range(1, x+1):
		if x%i==0:
			count+=1
	if count==2:
		return True
	else:
		return False

status = True
n = 0
l = []
while status:
	if len(l)==10001:
		print(l[-1])
		status=False
	elif IsPrime(n):
		l.append(n)
	n+=1