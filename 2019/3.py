def get_step(x):
	if x == 'R':
		return (1,0)
	if x == 'L':
		return (-1,0)
	if x == 'U':
		return (0,1)
	if x == 'D':
		return (0,-1)


p1 = [(x[0],int(x[1:])) for x in input().split(',')]
p2 = [(x[0],int(x[1:])) for x in input().split(',')]

p1_marked = {}


current = (0, 0)
p1_marked[current] = 0
move_num = 0
for p in p1:
	step = get_step(p[0])
	for s in range(p[1]):
		current = ( current[0] + step[0], current[1] + step[1] )
		move_num += 1
		p1_marked[current] = move_num 


intersections = []
least_step_intersections = []
move_num = 0
current = (0, 0)
for p in p2:
	step = get_step(p[0])
	for s in range(p[1]):
		current = ( current[0] + step[0], current[1] + step[1] )
		move_num += 1
		if current in p1_marked:
			intersections.append(current)
			least_step_intersections.append(p1_marked[current] + move_num)

intersections = [abs(i[0])+abs(i[1]) for i in intersections]
intersections.sort()

least_step_intersections.sort()

print(intersections) #  part 1
print(least_step_intersections) #  part 2


