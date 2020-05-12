import matplotlib.pyplot as plt


def mean( l):
    return sum(l) / (len(l) + 0.0)


def median( l):
    mid = len(l) / 2
    return l[mid]


def fillgraph(graph):
    row = col = len(graph)

    for i in range(row):
        for j in range(col):
            if i > j:
                graph[i][j] = graph[j][i]

def drawHist(data):
    plt.hist(data, bins=int(100))
    plt.show()
