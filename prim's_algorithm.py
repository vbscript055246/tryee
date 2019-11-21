import random
random.seed()

edge_table = [
 	#  A  B  C  D  E  F  G
    	[ 0, 1, 0, 1,12, 0, 0],	# A
	[ 1, 0, 6, 2, 0, 0, 0],	# B
	[ 0, 6, 0, 5, 0, 0, 8], # C
	[ 1, 2, 5, 0, 2, 3, 3], # D
	[12, 0, 0, 2, 0, 3, 0], # E
	[ 0, 0, 0, 3, 3, 0, 5], # F
	[ 0, 0, 8, 3, 0, 5, 0]  # G
]

# 1.
TV0 = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] # [chr(i) for i in range(65,72)]
TV = []
T = []

# 2.
index = random.randint(0, len(TV0)-1)
TV.append(TV0[index])
TV0.remove(TV0[index])

# 5.
while len(TV0):
	# 3.
	min = 999
	vtx_from_to = []
	for vertex in TV:
		for vtx in TV0:
			if min > edge_table[ord(vertex)-65][ord(vtx)-65] and edge_table[ord(vertex) - 65][ord(vtx)-65]:
				min = edge_table[ord(vertex)-65][ord(vtx)-65]
				vtx_from_to = [ord(vertex)-65, ord(vtx)-65]
	if min == 999:
		print("no spanning tree")
		exit(87)
	# 4.
	TV.append(chr(vtx_from_to[1]+65))
	TV0.remove(chr(vtx_from_to[1]+65))
	T.append((chr(vtx_from_to[0]+65), chr(vtx_from_to[1]+65)))

# result
print(TV)
print(T)
