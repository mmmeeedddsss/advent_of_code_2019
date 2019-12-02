import copy

mem_orj = [int(x) for x in input().split(',')]

for n in range(100):
	for v in range(100):
		mem = copy.deepcopy(mem_orj)

		mem[1] = n
		mem[2] = v

		pc = 0

		while True:
			op = mem[pc]
			if op == 99:
				break
			opr1 = mem[pc+1]
			opr2 = mem[pc+2]
			opr3 = mem[pc+3]
			if op == 1:
				mem[opr3] = mem[opr1] + mem[opr2]
			elif op == 2:
				mem[opr3] = mem[opr1] * mem[opr2]
			else:
				print('woops?')
			pc += 4


		if mem[0] == 19690720:
			print(n, v, 100*n+v)