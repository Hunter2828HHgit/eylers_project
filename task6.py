SumOfSquares = 0
SquareOfSum = 0
for i in range(1, 101):
	SumOfSquares+=i**2
for i in range(1, 101):
	SquareOfSum+=i
SquareOfSum **=2
print(SquareOfSum-SumOfSquares)