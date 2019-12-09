
all_layers = input()

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

all_layers = list(chunks(all_layers, 25*6))

best, best_ind = 99999999999999,0
for i,layer in enumerate(all_layers):
	c = 0
	for elem in layer:
		if elem == '0':
			c += 1
	if c < best:
		best = c
		best_ind = i

ones = 0
twos = 0
for elem in all_layers[best_ind]:
	if elem == '1':
		ones += 1
	elif elem == '2':
		twos += 1

print(ones*twos)


image = [None]*6
for i in range(len(image)):
	image[i] = [0] * 25

for i,c in enumerate(image):
	for j in range(len(c)):
		layer = 0
		while all_layers[layer][i*25 + j] == '2':
			layer += 1
		c[j] = all_layers[layer][i*25 + j]


'▓', '░'
for row in image:
	for elem in row:
		print('░' if elem == '1' else '▓',end = '')
	print()

