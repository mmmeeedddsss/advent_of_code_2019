
import threading
import keyboard
import time 

class OpcodeComp:
	literal_opcodes = [(1,3), (2,3), (3,1), (7,3), (8,3)]
	def __init__(self, code, brain):
		self.pc = 0
		self.mem = [int(x) for x in code.split(',')]
		self.mem = {k: v for k, v in enumerate(self.mem)}
		self.inp_index = 0
		self.halted = False
		self.inp = []
		self.relative_base = 0

		self.brain = brain

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
				self.brain.decide()
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
	def __init__(self):
		with open('13.in', 'r') as f:
			self.comp = OpcodeComp(f.read(), self)  # :(
		self.comp.mem_set(0, 2)
		self.c = 0

		self.map = [None] * 30
		for i in range(len(self.map)):
			self.map[i] = [0] * 50

		t = threading.Thread(target=self.draw)
		t.start()

		self.ball_pos = (0, 0)
		self.tile_pos = (0, 0)
		self.last_score = 0

		self.game_started = False

	def operate(self):
		sleep_time = 0.5
		while not self.comp.halted:
			#self.comp.append_input(self.get_paint(self.pos))
			x = int(self.comp.run_once())
			y = int(self.comp.run_once())
			tile_id = int(self.comp.run_once())
			if x == -1 and y == 0:
				self.last_score = max(tile_id, self.last_score )
				self.game_started = True
			else:
				self.map[y][x] = tile_id
				if tile_id == 4:
					self.ball_pos = (x, y)
				if tile_id == 3:
					self.tile_pos = (x, y)
			

	def decide(self):
		if self.tile_pos[0] < self.ball_pos[0]:
			inp = 1
		elif self.tile_pos[0] > self.ball_pos[0]:
			inp = -1
		else:
			inp = 0
		#print(self.tile_pos, self.ball_pos, inp)
		time.sleep(0.2)
		self.comp.append_input(inp)


	def draw(self):
		while True:
			for i in range(19):
				print()
			time.sleep(0.15)
			print(self.last_score)
			for i in range(30):
				for j in range(50):
					c = ' '
					v = self.map[i][j]
					if v == 1:
						c = 'X'
					elif v == 2:
						c = 'B'
					elif v == 3:
						c = 'P'
					elif v == 4:
						c = 'O'
					print(c, end='')
				print()



if __name__ == "__main__":
	r = Robot()
	r.operate()
	print(r.c)







