import unittest

from simplehillclimbing import hillClimbing, cost
from data import graph1
import matplotlib.pyplot as plt
from mst import mst
import probabilisticmst
from localbeam import localBeamSearch
from graph import Graph
import msthillclimbing

class MyTestCase(unittest.TestCase):
    def testSimpleHillClimbing(self):
        runTimes = 200
        self.fillgraph(graph1)
        ans = []
        for i in range(runTimes):
            seq = hillClimbing(graph1)
            seq_cost = cost(seq, graph1)

            ans.append((seq, seq_cost))
            print i
        cost_list = [float(ans[i][1]) for i in range(len(ans))]

        print self.mean(cost_list), max(cost_list), min(cost_list)

        self.drawHist(cost_list)


    def testMstHillClimbing(self):
        runTimes = 200

        ans = []
        self.fillgraph(graph1)

        for i in range(runTimes):
            tree = mst(graph1)

            seq = msthillclimbing.hillClimbing(graph1, tree)

            seq_cost = cost(seq, graph1)

            ans.append((seq, seq_cost))

        cost_list = [float(ans[i][1]) for i in range(len(ans))]

        print self.mean(cost_list), max(cost_list), min(cost_list)

        self.drawHist(cost_list)

    def testProbabilityMstHillClimbing(self):
        runTimes = 200
        self.fillgraph(graph1)

        ans = []
        for i in range(runTimes):
            tree = probabilisticmst.probabilisticmst(graph1)

            seq = msthillclimbing.hillClimbing(graph1, tree)

            seq_cost = cost(seq, graph1)

            ans.append((seq, seq_cost))

        cost_list = [float(ans[i][1]) for i in range(len(ans))]

        print self.mean(cost_list), max(cost_list), min(cost_list)

        self.drawHist(cost_list)

    def testLocalBeamSearch(self):
        iteration = 50

        self.fillgraph(graph1)

        scores = []
        for i in range(iteration):
            maxcost = localBeamSearch(graph1, 100)
            print i
            scores.append(maxcost)


        print min(scores), max(scores), sum(scores)/(len(scores) + 0.0)
        self.drawHist(scores)

    def mean(self, l):
        return sum(l)/(len(l) + 0.0)

    def median(self, l):
        mid = len(l) / 2
        return l[mid]

    def fillgraph(self, graph):
        row = col = len(graph)

        for i in range(row):
            for j in range(col):
                if i > j:
                    graph[i][j] = graph[j][i]

    def testMst(self):
        self.fillgraph(graph1)
        tree = mst(graph1)

        print tree
        num = len(tree)
        g = Graph()
        min_bound = 0
        for i in range(num):
            for j in range(i, num):
                if tree[i][j] > 0:
                    g.edge(str(i), str(j),symbol=str(tree[i][j]))
                    min_bound += tree[i][j]

        print min_bound
        g.render("./mst")



    def drawHist(self, data):
        plt.hist(data, bins=int(100))
        plt.show()

if __name__ == '__main__':
    unittest.main()
