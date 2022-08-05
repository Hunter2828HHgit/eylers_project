n = [1, 2]
while  n[-1] <4000000:
	n.append(n[-2]+n[-1])
# for i in n:
# 	if i%2==0:
# 		sum+=i
res = filter(lambda x:x%2==0, n)
print(sum(res))
# new 