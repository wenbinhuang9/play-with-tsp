
## a naive implementation, don't use any priority queue
import  sys
def mst(graph):
    num = len(graph)
    visited = [False for _ in range(num)]

    iteration = num - 1

    visited[0] = True
    tree = [[-1 for __ in range(num)] for _ in range(num)]

    minedgetotree = [(0, graph[0][i]) for i in range(num)]

    while iteration > 0:
        left, right, weight = getMinUnvisitedNode(visited, minedgetotree)

        tree[left][right] = weight
        tree[right][left] = weight
        update(graph, right, visited,minedgetotree )
        iteration -= 1

    return tree

def update(graph, newaddednode, visited, minedge):
    visited[newaddednode] = True

    for i in range(len(graph)):
        if visited[i] == False and graph[newaddednode][i] < minedge[i][1]:
            minedge[i]= (newaddednode, graph[newaddednode][i])

    return


def getMinUnvisitedNode(visited, minedgetotree):
    minnode = -1
    left = -1
    weight = sys.maxint

    for i in range(len(visited)):
        if visited[i] == False and minedgetotree[i][1] < weight:
            minnode = i
            left, weight = minedgetotree[i]

    return (left, minnode, weight)

