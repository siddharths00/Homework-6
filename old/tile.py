from collections import defaultdict

def DFS(g, s, t, parent):
    visited = [False] * (len(g) + 1)
    stack = [s]
    while(len(stack)):
        node_popped = stack.pop()
        # print(f"popped: {node_popped}")
        visited[node_popped] = True
        # print(visited)
        # stop if we are at the target
        for neighbour in g[node_popped]:
            # print(neighbour)
            if(visited[neighbour[0]] == False and neighbour[1] == 1):
                # set the node_popped as parent for this vertex
                parent[neighbour[0]] = node_popped
                # push this node for DFS
                stack.append(neighbour[0])
                if(neighbour[0] == t):
                    return True
                # print(parent)
    return False

def fordFulkerson(g, source, sink):
    parent = [-1] * (len(g) + 1)
    max_flow = 0
    while(DFS(g, source, sink, parent)):
        # find minimum capacity
        min_cap = float("Inf")
        node = sink
        while(node != source):
            # update
            for neighbour in g[parent[node]]:
                if(neighbour[0] == node):
                    min_cap = min(neighbour[1], min_cap)
            node = parent[node]
        max_flow += min_cap
        node = sink
        while(node != source):
            for neighbour in g[parent[node]]:
                if(neighbour[0] == node):
                    neighbour[1] -= min_cap
            for neighbour in g[node]:
                if(neighbour[0] == parent[node]):
                    neighbour[1] += min_cap
            node = parent[node]
    # print(g)
    return max_flow




class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self. ROW = len(graph)
        # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        # We didn't reach sink in BFS starting
        # from source, so return false
        return False

    # Returns the maximum flow from s to t in the given graph

    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def is_adjacent(a, b):
    # exactly one parameter should change
    if (abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 0):
        return True
    elif(abs(a[1] - b[1]) == 1 and abs(a[0] - b[0]) == 0):
        return True
    return False


infile = open("input.txt", "r")

n = int(infile.readlines()[0])
adj_mat = [[0] * (n+1) for i in range(n+1)]

lines = []
with open("input.txt") as fp:
    for line in fp:
        lines.append(line.strip())

# print(lines)

lines.pop(0)

# populate adjacency matrix
for i in range(len(lines)):
    for j in range(len(lines[i])):
        adj_mat[i+1][j+1] = int(lines[i][j])

# L - set of nodes created for empty cells
L = []
for i in range(len(adj_mat)):
    for j in range(len(adj_mat[i])):
        if (adj_mat[i][j] == 1):
            L.append([i, j])


# map indices to integers
map1 = dict()
ctr = 2
for item in L:
    map1[ctr] = item
    ctr += 1

R = L.copy()


map2 = dict()
for item in R:
    map2[ctr] = item
    ctr += 1

# print(map1)
# print(map2)
map3 = dict()

for k1, v1 in map1.items():
    for k2, v2 in map2.items():
        if(v1 == v2):
            map3[k1] = k2

for k1, v1 in map2.items():
    for k2, v2 in map1.items():
        if(v1 == v2):
            map3[k1] = k2

# print(map3)

lre_list = dict()
erl_lsit = dict()

# make lre_list
# s - L
nodes = []
for i in range(2, len(L)+2):
    nodes.append([i, 1])
lre_list[1] = nodes

# L - R and L - s
for i in range(2, len(L) + 2):
    temp = [[1,0]]
    for j in range(len(L) + 2, 2*len(L) + 2):
        idx1 = map1[i]
        idx2 = map2[j]
        if(is_adjacent(idx1, idx2)):
            temp.append([j,1])
    lre_list[i] = temp

# R - t
# for i in range(len(L) + 2, 2*len(L) + 2):
#     lre_list[i][([2*len(L) + 2, 1]]

# R - L back mapping
for i in range(len(L) + 2, 2*len(L) + 2):
    temp = []
    for j in range(2, len(L) + 2):
        idx1 = map1[j]
        idx2 = map2[i]
        if(is_adjacent(idx1, idx2)):
            temp.append([j,0])
    temp.append([2*len(L) + 2, 1])
    lre_list[i] = temp

# t - R
temp = []
for i in range(len(L) + 2, 2*len(L) + 2):
    temp.append([i, 0])
lre_list[2*len(L) + 2] = temp

# print(lre_list)

# make erl_list
# map t nodes to R
# erl_list = dict()
# nodes = []
# for i in range(len(L)+2, 2*len(L) + 2):
#     nodes.append([i, 0])
# erl_list[2*len(L) + 2] = nodes
#
# # add edges of R
# for i in range(len(L) + 2, 2*len(L) + 2):
#     temp = []
#     for j in range(2, len(L) + 2):
#         idx1 = map1[j]
#         idx2 = map2[i]
#         if(is_adjacent(idx1, idx2)):
#             temp.append([j,0])
#     erl_list[i] = temp
#
# # add edges of L
# for i in range(2, len(L) + 2):
#     erl_list[i] = [1, 0]
# print(erl_list)
#


# check if perfect matching exists

# create graph to pass to ford fulkerson
# g_mat = [[0] * (2*len(L)+3) for i in range(2*len(L) + 3)]
#
# # populate g_mat using lre_list
# for key, value in lre_list.items():
#     for node in value:
#         g_mat[key][node] = 1


# specify source and sink and call Ford-Fulkerson
# src = 1
# sink = len(g_mat) - 1
# g = Graph(g_mat)
# ans = g.FordFulkerson(src, sink)
#
# # write ans to file
# outfile = open("output.txt", "w+")
# outfile.write("1\n") if ans == len(L) else outfile.write("0\n")
# outfile.close()
#
# # write the specific pairs into the output file
# g_copy = g.graph
#
# pairs = []
# for i in range(len(L) + 2, 2*len(L) + 2):
#     for j in range(2, len(L) + 2):
#         if(g_copy[i][j] == 1):
#             g_copy[map3[j]][map3[i]] = 0
#             pairs.append([map1[j], map2[i]])
#
# if(ans == len(L)):

# print(DFS(lre_list, 1, 2*len(L) + 2, [-1 for i in range(2*len(L) + 3)]))

ans = fordFulkerson(lre_list, 1, 2*len(L) + 2)
outfile = open("output.txt", "w")
outfile.write("1\n") if ans == len(L) else outfile.write("0\n")
outfile.close()

pairs = []
if(ans == len(L)):
    seen = set()
    for i in range(2, len(L) + 2):
        for item in lre_list[i]:
            if(item[1] == 0 and map3[i] not in seen and map3[item[0]] not in seen):
                # i, item[0] is our pair
                pairs.append([map1[i], map2[item[0]]])
                seen.add(i)
                seen.add(item[0])

    # write pairs to output file
    outfile = open("output.txt", "a")
    for pair in pairs:
        outfile.write("({},{})({},{})\n".format(pair[0][0],pair[0][1],pair[1][0],pair[1][1]))
    outfile.truncate(outfile.tell()-1)
    outfile.close()
