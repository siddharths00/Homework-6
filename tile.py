from collections import defaultdict


def is_adjacent(a, b):
    # exactly one parameter should change
    if (abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 0) or (abs(a[1] - b[1]) == 1 and abs(a[0] - b[0]) == 1):
        return True
    return False


infile = open("input.txt", "r")

n = int(infile.readlines()[0])
adj_mat = [[0] * n for i in range(n)]

lines = []
with open("input.txt") as fp:
    for line in fp:
        lines.append(line.strip())

# remove first charatcer
lines.pop(0)

# populate adjacency matrix
for i in range(len(lines)):
    for j in range(len(lines[i])):
        adj_mat[i][j] = int(lines[i][j])

# L - set of nodes created for empty cells
L = []
for i in range(len(adj_mat)):
    for j in range(len(adj_mat[i])):
        if (adj_mat[i][j] == 1):
            L.append([i, j])

# map indices to integers
mapping = dict()
ctr = 0
for item in L:
    mapping[ctr] = item
    ctr += 1

R = L.copy()

lre_graph = [[0] * len(L) for i in range(len(L))]

# populate the LRE graph
# add vertices if they are adjacent empty nodes
for litem in L:
    for ritem in R:
        if (is_adjacent(litem, ritem) and litem != ritem):
            # find integer for litem, ritem
            u = -1
            v = -1
            for key, value in mapping.items():
                if (litem == value):
                    u = key
                    break
            for key, value in mapping.items():
                if (ritem == value):
                    v = key
                    break
            lre_graph[u][v] = 1
            lre_graph[v][u] = 1
            print(litem, ritem)
# print(mapping)
print(lre_graph)
