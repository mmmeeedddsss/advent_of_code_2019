import copy
import math

a = []
INF = 99999999999

def is_valid(x, y):
	b = len(a)
	r = len(a[0])
	if x >= 0 and x < r and y >= 0 and y < b:
		return True
	return False

def neighbors(pos):
	n = []
	x = pos[0]
	y = pos[1]
	if is_valid(x-1, y):
		n.append((x-1, y))
	if is_valid(x+1, y):
		n.append((x+1, y))
	if is_valid(x, y-1):
		n.append((x, y-1))
	if is_valid(x, y+1):
		n.append((x, y+1))
	return n


def bfs( start, mp, debug = False ):
	q = neighbors(start)
	mp[start[1]][start[0]] = 's'
	counter = 0
	while len(q):
		e = q[0]
		q = q[1:]

		x = e[0]
		y = e[1]
		if mp[y][x] == '-':
			continue
		elif mp[y][x] == '.':
			mp[y][x] = '-'
		elif mp[y][x] == '#':
			counter += 1
			dx = x - start[0]
			dy = y - start[1]
			gcd = math.gcd(dx, dy)
			dx //= gcd
			dy //= gcd
			if debug: print("for x,y",x,y)
			while is_valid(x, y):
				mp[y][x] = '.'
				x += dx
				y += dy
			if debug:
				for r in mp:
					for k in r:
						print(k, end='')
					print()
				print("counter=",counter)
				print()

		q += neighbors(e)
	return counter


while True:
	row = input()
	if row == '-1':
		break
	a.append(list(row))

astreoids = []
orig = None

best = 0
scores = copy.deepcopy(a)
for i in range(len(a)):
	for j in range(len(a[0])):
		# Calc for i,j
		if a[i][j] == '#':
			astreoids.append((j,i))
			c = bfs( (j, i), copy.deepcopy(a) )
			scores[i][j] = c
			if c > best:
				best = c
				orig = (j,i)

print(best)
for r in scores:
	for e in r:
		print(e, end='')
	print()
print('-------')
for r in a:
	for e in r:
		print(e, end='')
	print()

astreoids.remove(orig)

print(orig)


print('--------------------- PART 2 ----------------------')


astreoids = [ (a[0]-orig[0], a[1]-orig[1]) for a in astreoids ]
astreoids = [ (a[1]/a[0] if not a[0] == 0 else -INF,(a[0], a[1])) for a in astreoids ] #  (m,(x,y))
r = list(filter(lambda a: a[1][0] > 0 or a[1][0] == 0 and a[1][1] < 0, astreoids))
l = list(filter(lambda a: a[1][0] < 0, astreoids))


r.sort(key=lambda x: +100000*x[0]-abs(x[1][0]) - abs(x[1][1]) )
l.sort(key=lambda x: +100000*x[0]-abs(x[1][0]) - abs(x[1][1]) )


print(r)
print("---")
print(l)

del_num = 0
deleted_elems = []
while del_num < 200:
	ind = 0
	last_elem = (-99999999,-999999999)
	while del_num < 200 and ind < len(r):
		if not r[ind][0] == last_elem[0]:
			last_elem = r.pop(ind)
			deleted_elems.append(last_elem)
			del_num += 1
			ind -= 1
		ind += 1
	ind = 0
	while del_num < 200 and ind < len(l):
		if not l[ind][0] == last_elem[0]:
			last_elem = l.pop(ind)
			deleted_elems.append(last_elem)
			del_num += 1
			ind -= 1
		ind += 1

deleted_elems = [( e[1][0] + orig[0], e[1][1] + orig[1] ) for e in deleted_elems ]

print(deleted_elems)


print(deleted_elems[-2][0]*100 + deleted_elems[-2][1])







