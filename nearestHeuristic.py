import  random

from naivemst import mst
# A hill climbing algorithm with random selection.
## todo can I remember sth. here
def cost(chromosome, city_distance_data):
  distance = 0
  previous_city_no = 0
  for cur_city_no in chromosome:
    distance += city_distance_data[previous_city_no][cur_city_no]
    previous_city_no = cur_city_no

  distance += city_distance_data[previous_city_no][0]

  return distance


def getRandomSequence(city_num, tree ):

    return mstseq(tree, city_num)

#   start_city = random.randrange(0, city_num)

def mstseq(tree, city_num):
  node = random.randrange(0, city_num)

  seq = dfsrecursive(node, tree, city_num, set([]))

  return seq
def dfsrecursive(node, tree, city_num, visited):
  visited.add(node)

  ans = [node]
  for i in range(city_num):
    if i not in visited and tree[node][i] > 0 :
      subans =  dfsrecursive(i, tree, city_num, visited)
      ans.extend(subans)

  return ans


def init(cityNum, tree):
  return getRandomSequence(cityNum, tree )

## accept a bad result when we can't go forward???

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

## the key is to implement from here!
def nearest(cityNum, graph):
  pass

def hillClimbing(graph, tree ):
  row, col = len(graph), len(graph[0])
  cityNum = row
  assert row == col

  curSeq = nearest(cityNum, graph)

  iteration = 10000
  while iteration > 0:
    nextSeq = climb(curSeq, graph )
    if nextSeq == None:
      ## termination, because can't find better solution after limited selections.
      return curSeq
    iteration -= 1
    curSeq = nextSeq

  return curSeq


