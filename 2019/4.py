

s,e = input().split('-')
s = int(s)
e = int(e)

def is_adj(x):
	sx = str(x)
	combo = 1
	has_adj = False
	for i in range(len(sx)-1):
		if sx[i] == sx[i+1]:
			combo += 1
		else:
			has_adj = True
			if combo == 2:
				return 2
			combo = 1
	if combo > 1:
		has_adj = True
		if combo == 2:
			return 2
		combo = 1
	return 3 if has_adj else 0
			


def is_non_dec(x):
	sx = str(x)
	for i in range(len(sx)-1):
		if sx[i] > sx[i+1]:
			return False
	return True


counter1 = 0
counter2 = 0
for cand in range(s,e):
	if is_non_dec(cand):
		adj = is_adj(cand)
		if adj > 0:
			counter1 += 1
			if adj == 2:
				counter2 += 1


print(counter1)
print(counter2)