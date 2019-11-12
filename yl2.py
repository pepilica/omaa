def creating(di):
    out = [[] for _ in range(len(a))]
    for i in di.keys():
        for j in range(len(di.keys())):
            if j != di[i][j][0] - 1:
                out[j].append(0)
            else:
                out[j].append(di[i][1])
    return out


def way():
    pass


a = []
graph = dict()
inp = [int(i) for i in input().strip().split()]
while len(inp) == 3:
    to, out, length = inp
    if to not in graph.keys():
        graph[to] = [(out, length)]
    else:
        graph[to].append((out, length))
    if out not in graph.keys():
        graph[out] = [(to, length)]
    else:
        graph[out].append((to, length))
    inp = [int(i) for i in input().split()]
matrix = creating(graph)
print(matrix)