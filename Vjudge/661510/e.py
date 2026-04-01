connections = {1: [-1]}

depts, lines = map(int, input().split())
all_depts = list(range(1, depts+1))
all_depts.remove(1)
all_depts.remove(depts)

for i in range(lines):
	a, b = map(int, input().split())
	if a not in connections:
		connections[a] = []
	connections[a].append(b)

	if b not in connections:
		connections[b] = []
	connections[b].append(a)

network = []

start = 1

def line(pos, c_line):
	# print('pos', pos, 'c_line', c_line)
	if all(x in c_line for x in all_depts):
		return

	if pos == depts:
		new_line = c_line.copy()
		new_line.append(depts)
		network.append(new_line)
		return

	for wire in connections.get(pos, []):
		if wire in c_line:
			continue
		new_line = c_line.copy()
		new_line.append(wire)
		if wire == depts:
			network.append(new_line)
			continue
		line(wire, new_line)


for wire in connections[start]:
	line(wire, [start, wire])

if len(network) == 0:
	print("IMPOSSIBLE")


else:
	mini = min(network, key=lambda x: len(x))
	print(' '.join(map(str, mini)))
# print('network', network)