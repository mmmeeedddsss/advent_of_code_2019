import os
from tqdm import tqdm
import itertools
import copy
import subprocess

class OpcodeComp:
	def __init__(self, code):
		self.pc = 0
		self.mem = [int(x) for x in code.split(',')]
		self.inp_index = 0
		self.halted = False
		self.inp = []

	def parse_opcode(self, op):
			ops = str(op)
			while len(ops) < 5:
				ops = "0" + ops
			return tuple(ops[:-2]) + (int(ops[-2:]),)

	def append_input(self, new_inp):
		self.inp.append(int(new_inp))

	def run_once(self):
		while True:
			mode3, mode2, mode1, op = self.parse_opcode(self.mem[self.pc])
			if op == 99:
				self.halted = True
				return self.halted
			try:
				if self.pc+1 < len(self.mem):
					opr1 = self.mem[self.pc+1]
					param1 = self.mem[opr1] if mode1 == '0' else opr1
				if self.pc+2 < len(self.mem):
					opr2 = self.mem[self.pc+2]
					param2 = self.mem[opr2] if mode2 == '0' else opr2
				if self.pc+3 < len(self.mem):
					opr3 = self.mem[self.pc+3]
					param3 = self.mem[opr3] if mode3 == '0' else opr3
			except:
				pass

			if op == 1:
				self.mem[opr3] = param1 + param2
				inc = 4
			elif op == 2:
				self.mem[opr3] = param1 * param2
				inc = 4
			elif op == 3:
				self.mem[opr1] = self.inp[self.inp_index]# 5 for part 5
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
				self.mem[opr3] = 0
				if param1 < param2:
					self.mem[opr3] = 1
				inc = 4
			elif op == 8:
				self.mem[opr3] = 0
				if param1 == param2:
					self.mem[opr3] = 1
				inc = 4
			else:
				print('woops?', op)
			self.pc += inc



instructions = input()

best = 0
best_seq = None

for it in tqdm(itertools.permutations('56789')):
	last_e = 0
	last_o = 0
	i = 0

	comps = []
	for _ in range(5):
		comps.append(OpcodeComp(instructions))
	for ind, comp in enumerate(comps):
		comp.append_input(it[ind])
	while True:
		comps[i].append_input(str(last_o))
		last_o = comps[i].run_once()
		if comps[i].halted:
			if int(last_e) > best:
				best = int(last_e)
				best_seq = it
			break
		i += 1
		i %= 5
		if i == 0:
			last_e = last_o


print(best, best_seq)

