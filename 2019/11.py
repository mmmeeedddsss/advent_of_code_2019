

class OpcodeComp:
	literal_opcodes = [(1,3), (2,3), (3,1), (7,3), (8,3)]
	def __init__(self, code):
		self.pc = 0
		self.mem = [int(x) for x in code.split(',')]
		self.mem = {k: v for k, v in enumerate(self.mem)}
		self.inp_index = 0
		self.halted = False
		self.inp = []
		self.relative_base = 0

	def parse_opcode(self, op):
			ops = str(op)
			while len(ops) < 5:
				ops = "0" + ops
			return tuple(ops[:-2]) + (int(ops[-2:]),)

	def parse_param(self, p, mode, opcode, param_order):
		if mode == '0' or mode == '1':
			param = p
		elif mode == '2':
			param = p + self.relative_base
		else:
			print('woops2?', p, mode)

		if (opcode, param_order) not in OpcodeComp.literal_opcodes and not mode == '1':
			return self.mem_get(param)
		return param

	def append_input(self, new_inp):
		self.inp.append(int(new_inp))

	def mem_get(self, ind):
		if ind not in self.mem:
			self.mem[ind] = 0
		return self.mem[ind]

	def mem_set(self, ind, val):
		self.mem[ind] = val

	def run_once(self):
		while True:
			mode3, mode2, mode1, op = self.parse_opcode(self.mem_get(self.pc))
			if op == 99:
				self.halted = True
				return self.halted

			# parse parameters of operation
			opr1 = self.mem_get(self.pc+1)
			param1 = self.parse_param(opr1, mode1, op, 1)
			opr2 = self.mem_get(self.pc+2)
			param2 = self.parse_param(opr2, mode2, op, 2)
			opr3 = self.mem_get(self.pc+3)
			param3 = self.parse_param(opr3, mode3, op, 3)

			if op == 1:
				self.mem_set(param3, param1 + param2)
				inc = 4
			elif op == 2:
				self.mem_set(param3, param1 * param2)
				inc = 4
			elif op == 3:
				self.mem_set(param1, self.inp[self.inp_index])# 5 for part 5
				self.inp_index += 1
				inc = 2
			elif op == 4:
				self.pc += 2
				return param1
			elif op == 5:
				if not param1 == 0:
					self.pc = param2 - 3
				inc = 3
			elif op == 6:
				if param1 == 0:
					self.pc = param2 - 3
				inc = 3
			elif op == 7:
				self.mem_set(param3, 0)
				if param1 < param2:
					self.mem_set(param3, 1)
				inc = 4
			elif op == 8:
				self.mem_set(param3, 0)
				if param1 == param2:
					self.mem_set(param3, 1)
				inc = 4
			elif op == 9:
				self.relative_base += param1
				inc = 2
			else:
				print('woops?', op)
			self.pc += inc


class Robot:
	orientation_list = ['u','r','d','l']
	moves = { 'u': (0,-1), 'r': (1, 0), 'd': (0, 1), 'l': (-1, 0) }

	def __init__(self):
		self.orientation = 'u'
		self.pos = (0, 0)
		self.comp = OpcodeComp(input())
		self.area = { (0,0): 1 }
	
	def get_paint(self, pos):
		if pos in self.area:
			return self.area[pos]
		return 0

	def set_paint(self, pos, color):
		self.area[self.pos] = color

	def make_turn(self, turn):
		ind = Robot.orientation_list.index(self.orientation)
		if turn == 0:
			ind -= 1
		else:
			ind += 1
		ind += 4
		ind %= 4
		self.orientation = Robot.orientation_list[ind]

	def move(self):
		dirr = Robot.moves[self.orientation]
		self.pos = ( self.pos[0] + dirr[0], self.pos[1] + dirr[1] )

	def operate(self):
		while not self.comp.halted:
			self.comp.append_input(self.get_paint(self.pos))
			color = int(self.comp.run_once())
			turn = int(self.comp.run_once())
			print(color, turn)

			self.set_paint(self.pos, color)
			self.make_turn(turn)
			self.move()


if __name__ == "__main__":
	r = Robot()
	r.operate()
	print("->", len(r.area))
	for i in range(-30,30):
		for j in range(-40,150):
			if (j,i) in r.area and r.area[(j,i)] == 1:
				print('█', end='')
			else:
				print(' ', end='')
		print()








