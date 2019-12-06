import copy

mem = [int(x) for x in input().split(',')]


def parse_opcode(op):
	ops = str(op)
	while len(ops) < 5:
		ops = "0" + ops
	return tuple(ops[:-2]) + (int(ops[-2:]),)


pc = 0

input_v = 5

while True:
	mode3, mode2, mode1, op = parse_opcode(mem[pc])
	if op == 99:
		break
	try:
		if pc+1 < len(mem):
			opr1 = mem[pc+1]
			param1 = mem[opr1] if mode1 == '0' else opr1
		if pc+2 < len(mem):
			opr2 = mem[pc+2]
			param2 = mem[opr2] if mode2 == '0' else opr2
		if pc+3 < len(mem):
			opr3 = mem[pc+3]
			param3 = mem[opr3] if mode3 == '0' else opr3
	except:
		pass

	if op == 1:
		mem[opr3] = param1 + param2
		inc = 4
	elif op == 2:
		mem[opr3] = param1 * param2
		inc = 4
	elif op == 3:
		mem[opr1] = input_v
		inc = 2
	elif op == 4:
		print(param1)
		inc = 2
	elif op == 5:
		if not param1 == 0:
			pc = param2 - 3
		inc = 3
	elif op == 6:
		if param1 == 0:
			pc = param2 - 3
		inc = 3
	elif op == 7:
		mem[opr3] = 0
		if param1 < param2:
			mem[opr3] = 1
		inc = 4
	elif op == 8:
		mem[opr3] = 0
		if param1 == param2:
			mem[opr3] = 1
		inc = 4
	else:
		print('woops?', op)
	pc += inc



