
## probabilistic mst
import random

def mst(graph):
    num = len(graph)
    visited = [False for _ in range(num)]

    iteration = num

    visited[0] = True
    tree = [[-1 for __ in range(num)] for _ in range(num)]

    minedgetotree = set([(0, i, graph[0][i]) for i in range(num)])

    while iteration > 0:
        left, right, weight = getMinUnvisitedNode(minedgetotree)

        tree[left][right] = weight
        tree[right][left] = weight
        update(graph, right, visited,minedgetotree )
        iteration -= 1

    return tree

def update(graph, newaddednode, visited, minedge):
    visited[newaddednode] = True

    for e in minedge:
        left, right, weight = e
        if graph[newaddednode][right] < weight:
            minedge.remove(e)
            minedge.add((newaddednode, right,graph[newaddednode][right]))

def getMinUnvisitedNode(minedgetotree):
    if len(minedgetotree) == 1:
        return minedgetotree.pop()

    p = random.uniform(0, 1)
    if p < 0.7:
        firstMin = min(minedgetotree, key= lambda x: x[2])
        minedgetotree.remove(firstMin)
        return firstMin

    elif 0.7 <= p < 0.9 :
        firstMin = min(minedgetotree, key= lambda x: x[2])
        minedgetotree.remove(firstMin)

        secondMin = min(minedgetotree, key=lambda x: x[2])
        minedgetotree.remove(secondMin)

        minedgetotree.add(firstMin)
        return secondMin
    else:
        thirdMinList = random.sample(minedgetotree, 1)
        thirdMin = thirdMinList[0]
        minedgetotree.remove(thirdMin)
        return thirdMin


