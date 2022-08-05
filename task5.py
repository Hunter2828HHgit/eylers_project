n = 1
status = True
while status:
	l = [i for i in range(1, 21) if n%i==0]
	if len(l)==20:
		print(n)
		status = False
	n+=1