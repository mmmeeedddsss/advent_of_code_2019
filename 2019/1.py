

summ = 0
i = int(input())
while not i == -1 :
	f = i//3-2
	while f > 0:
		summ += f
		f = f//3 - 2
	
	i = int(input())

print(summ)