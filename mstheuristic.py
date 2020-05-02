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
def climb(seq, randomSelectionTimes, cityNum, graph, tree ):
  while randomSelectionTimes > 0:
    nextSeq = getRandomSequence(cityNum,tree)
    if cost(nextSeq, graph) < cost(seq, graph):
      return nextSeq
    randomSelectionTimes -= 1

  return None

def hillClimbing(graph, iteration, randomSelectionTimes, tree ):
  row, col = len(graph), len(graph[0])
  cityNum = row
  assert row == col

  seq = init(cityNum, tree)

  while iteration > 0:
    nextSeq = climb(seq, randomSelectionTimes, cityNum, graph, tree )
    if nextSeq == None:
      ## termination, because can't find better solution after limited selections.
      return seq
    iteration -= 1

  return nextSeq


