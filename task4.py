l = []
def IsPolindrom(x):
	l = list(str(x))
	rev = list(reversed(l))
	return True if l==rev else False

for i in range(100, 1000):
	for j in range(100, 1000):
		if IsPolindrom(i*j): # if str(i*j)==str(i*j)[::-1]:
			l.append(i*j)

print(max(l))