import math
from copy import deepcopy

class Moon:
	def __init__(self, x, y, z):
		self.pos = [x,y,z]
		self.vel = [0, 0, 0]

	def apply_gravity_caused_by(self, moon2):
		def _update_vel_on_axis(moon2, axis):
			if moon2.pos[axis] > self.pos[axis]:
				self.vel[axis] += 1
			elif moon2.pos[axis] < self.pos[axis]:
				self.vel[axis] -= 1
			else:
				pass

		_update_vel_on_axis(moon2, 0)
		_update_vel_on_axis(moon2, 1)
		_update_vel_on_axis(moon2, 2)

	def iterate_time(self):
		def _iterate_on_axis(axis):
			self.pos[axis] += self.vel[axis]

		_iterate_on_axis(0)
		_iterate_on_axis(1)
		_iterate_on_axis(2)

	def kinetic_energy(self):
		print(self.vel)
		return abs(self.vel[0]) + abs(self.vel[1]) + abs(self.vel[2])

	def potantial_energy(self):
		print(self.pos)
		return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])

	def total_energy(self):
		return self.kinetic_energy() * self.potantial_energy()

orig_moons = [Moon(-17,9,-5), Moon(-1,7,13), Moon(-19,12,5), Moon(-6,-6,-4)]
moons = [Moon(-17,9,-5), Moon(-1,7,13), Moon(-19,12,5), Moon(-6,-6,-4)]

#orig_moons = [moon(-8,-10,0), moon(5,5,10), moon(2,-7,3), moon(9,-8,-3)]
#moons = [moon(-8,-10,0), moon(5,5,10), moon(2,-7,3), moon(9,-8,-3)]

#orig_moons = [Moon(-1,-0,2), Moon(2,-10,-7), Moon(4,-8,8), Moon(3,5,-1)]
#moons = [Moon(-1,-0,2), Moon(2,-10,-7), Moon(4,-8,8), Moon(3,5,-1)]

lim = 16 # given
for iter in range(lim):
	for i in range(len(moons)):
		for j in range(i+1, len(moons)):
			moons[i].apply_gravity_caused_by(moons[j])
			moons[j].apply_gravity_caused_by(moons[i])

	for moon in moons:
		moon.iterate_time()

s = 0
for moon in moons:
	s += moon.total_energy()

print(s)

#orig_moons = [Moon(-1,-0,2), Moon(2,-10,-7), Moon(4,-8,8), Moon(3,5,-1)]
#moons = [Moon(-1,-0,2), Moon(2,-10,-7), Moon(4,-8,8), Moon(3,5,-1)]


def _find_repeat_on_axis(axis):
	iter = 0
	moons = deepcopy(orig_moons)
	while True:
		for i in range(len(moons)):
			for j in range(i+1, len(moons)):
				moons[i].apply_gravity_caused_by(moons[j])
				moons[j].apply_gravity_caused_by(moons[i])
		
		for moon in moons:
			moon.iterate_time()
		iter += 1

		flag = True
		for i in range(len(moons)):
			if not moons[i].pos[axis] == orig_moons[i].pos[axis]:
				flag = False
				break
			if not moons[i].vel[axis] == 0:
				flag = False
				break
		if flag == True:
			print(iter)
			for i in range(len(moons)):
				print(moons[i].pos, moons[i].vel)
			return iter


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

a = _find_repeat_on_axis(0)
b = _find_repeat_on_axis(1)
c = _find_repeat_on_axis(2)

i = lcm( lcm( a,b), c)

print(i)








