import graphviz as gv

class Graph():
    def __init__(self, rankdir = ""):
        self.node = set([])
        self.graph = self.__createSvg(rankdir)

    def __createSvg(self, rankdir = ""):
        graph = gv.Digraph(format='svg')
        if rankdir != "":
            graph.attr(rankdir=rankdir)
        return graph

    def doubleEdge(self, a, b):
        self.edge(a, b)
        self.edge(b, a)
    def edge(self, a, b, symbol = "", style="", shape = ""):
        if a not in self.node:
            self.node.add(a)
            self.graph.node(a , shape = shape)


        if b not in self.node:
            self.node.add(b)
            self.graph.node(b, shape = shape)

        self.graph.edge(a, b, label = symbol, style=style, shape= "box", arrowhead = "none")

    def render(self, file):
        self.graph.render(file)
