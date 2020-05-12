import  random
from  util import fillgraph, drawHist, median, mean
from data import graph1
from mst import mst
def hillClimbing(graph, tree):
  row, col = len(graph), len(graph[0])
  cityNum = row

  ## heuristic by generating sequence from MST
  curState= genMstRandomly(tree, cityNum)

  iteration = 10000
  while iteration > 0:
    nextState = climb(curState, graph)

    if nextState == None:
      ## termination, because can't find better solution after limited selections.
      return curState

    iteration -= 1
    curState = nextState

  return curState

##generate next states by swapping any two cities
##Get the new sequence with lower cost
def climb(curState, graph):
  row = len(graph)
  curCost = cost(curState, graph)
  for i in range(row):
    for j in range(i + 1, row):
      nextState = curState[:]
      nextState[i], nextState[j] = nextState[j], nextState[i]
      nextCost = cost(nextState, graph)
      if nextCost < curCost:
        return nextState

  return None

def genMstRandomly(mstTree, city_num):
  node = random.randrange(0, city_num)

  seq = genMstRecursive(node, mstTree, city_num, set([]))

  return seq


def genMstRecursive(node, tree, city_num, visited):
  visited.add(node)

  ans = [node]
  for i in range(city_num):
    if i not in visited and tree[node][i] > 0 :
      subans =  genMstRecursive(i, tree, city_num, visited)
      ans.extend(subans)

  return ans


def cost(state, city_distance_data):
  distance = 0
  previous_city_no = 0
  for cur_city_no in state:
    distance += city_distance_data[previous_city_no][cur_city_no]
    previous_city_no = cur_city_no

  distance += city_distance_data[previous_city_no][0]

  return distance


if __name__ == "__main__":
  runTimes = 200

  ans = []
  fillgraph(graph1)
  print ("begin running mst heuristic hill climbing for {0} times".format(runTimes))
  for i in range(runTimes):
    tree = mst(graph1)

    seq = hillClimbing(graph1, tree)

    seq_cost = cost(seq, graph1)
    print (seq_cost)

    ans.append((seq, seq_cost))

  cost_list = [float(ans[i][1]) for i in range(len(ans))]

  print ("final result, tsp min cost = {0}; tsp max cost = {1};tsp average cost = {2}".format(min(cost_list), max(cost_list), sum(cost_list) / (len(cost_list) + 0.0)))

  drawHist(cost_list)