import unittest

from graph import Graph

from  data import graph1, fillgraph
from probabilisticmst import mst
class MyTestCase(unittest.TestCase):
    def test_propabilisitc_mst(self):
        graph = fillgraph(graph1)
        num = len(graph)
        tree = mst(graph)

        g = Graph()
        min_bound = 0
        tree_len = 0
        for i in range(num):
            for j in range(i, num):
                if tree[i][j] > 0:
                    g.edge(str(i), str(j),symbol=str(tree[i][j]))
                    min_bound += tree[i][j]
                    tree_len += 1
        print min_bound
        print tree_len
        g.render("./propability_mst")


if __name__ == '__main__':
    unittest.main()
