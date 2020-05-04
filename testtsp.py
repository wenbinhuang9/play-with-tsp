import unittest

from randomhillclimbing import hillClimbing, getRandomSequence, cost
from  data import  graph1
import matplotlib.pyplot as plt
import  random
from mstheuristic import mstseq
from naivemst import mst
import probabilitymst
import mstheuristic

from  graph import Graph

class MyTestCase(unittest.TestCase):
    def testGetRandomSequence(self):

        seq = getRandomSequence(10)
        print seq

        print random.randrange(0, 10)


    def runProbabilityMstHillClimbing(self):
        self.fillgraph(graph1)
        tree = probabilitymst.mst(graph1)

        ans_seq = mstheuristic.hillClimbing(graph1, tree)

        return ans_seq


    def runMstHillClimbing(self):
        self.fillgraph(graph1)
        tree = mst(graph1)

        ans_seq = mstheuristic.hillClimbing(graph1, tree)

        return ans_seq


    def runhillClimbing(self):

        ans_seq = hillClimbing(graph1)

        return ans_seq

    def mean(self, l):
        return sum(l)/(len(l) + 0.0)
    def median(self, l):
        mid = len(l) /2
        return l[mid]

    ## todo how to verify a good initial point can get a better result???
    def testHillClimbing(self):
        restartTime = 200
        self.fillgraph(graph1)
        ans = []
        for i in range(restartTime):
            seq = self.runhillClimbing()
            seq_cost = cost(seq, graph1)

            ans.append((seq, seq_cost))
            print i
        cost_list = [float(ans[i][1]) for i in range(len(ans))]

        print self.mean(cost_list), max(cost_list), min(cost_list)

        self.drawHist(cost_list)

    def testMstHillClimbing(self):
        restartTime = 200

        ans = []
        for i in range(restartTime):
            seq = self.runMstHillClimbing()
            seq_cost = cost(seq, graph1)

            ans.append((seq, seq_cost))

        cost_list = [float(ans[i][1]) for i in range(len(ans))]

        print self.mean(cost_list), max(cost_list), min(cost_list)

        self.drawHist(cost_list)


    def testProbabilityMstHillClimbing(self):
        restartTime = 1000

        ans = []
        for i in range(restartTime):
            seq = self.runProbabilityMstHillClimbing()
            seq_cost = cost(seq, graph1)

            ans.append((seq, seq_cost))

        cost_list = [float(ans[i][1]) for i in range(len(ans))]

        print self.mean(cost_list), max(cost_list), min(cost_list)

        self.drawHist(cost_list)


    def fillgraph(self, graph):
        row = col = len(graph)

        for i in range(row):
            for j in range(col):
                if i > j:
                    graph[i][j] = graph[j][i]

    def testmst(self):
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

    def testmstseq(self):
        self.fillgraph(graph1)

        tree = mst(graph1)
        city_num = len(tree)

        seq = mstseq(tree, city_num)

        print  seq

    def drawHist(self, data):
        plt.hist(data, bins=int(100))
        plt.show()

if __name__ == '__main__':
    unittest.main()
