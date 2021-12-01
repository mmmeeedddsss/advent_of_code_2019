c = 0
l = []

with open("in/1.txt", "r") as f:
    for line in f:
        now = int(line)
        l.append(now)

print(l)

for i in range(len(l)-3):
    if l[i] < l[i+3]:
        c+= 1
print(c)