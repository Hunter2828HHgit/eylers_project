def IsPrime(x):
	count = 0
	for i in range(1, x+1):
		if x%i==0:
			count+=1
	if count==2:
		return True
	else:
		return False
n = 600851475143
l = []
for i in range(1, n):
	if n%i==0 and IsPrime(i):
		l.append(i)
print(l[-1])