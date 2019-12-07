import copy

edges = {}
path_you = None
path_santa = None

def calc( r, cpath ):
	if r == 'YOU':
		global path_you
		path_you = cpath
	if r == 'SAN':
		global path_santa
		path_santa = cpath
	if r not in edges:
		return 0, 1
	cs = edges[r]
	rs, b = 0, 0
	for c in cs:
		_rs, _b = calc(c, cpath + [r])
		rs += _rs
		b += _b
	return rs + b, b + 1



inp = input()
while not inp == '-1':
	f, t = inp.split(')')
	if f in edges:
		edges[f].append(t)
	else:
		edges[f] = [t]
	inp = input()

print(calc('COM', []))
print(path_you)
print(path_santa)

ind = 0
while True:
	if ind < len(path_santa) and ind < len(path_you) and path_santa[ind] == path_you[ind]:
		ind += 1
	else:
		print(len(path_santa) - ind + len(path_you) - ind)
		break


"""
COM)B
B)G
G)H
B)C
C)D
D)I
D)E
E)F
E)J
J)K
K)L
"""













