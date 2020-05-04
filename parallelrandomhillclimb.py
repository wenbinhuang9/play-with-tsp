import sys
import  random
# A hill climbing algorithm with random selection.
def cost(chromosome, city_distance_data):
  distance = 0
  previous_city_no = 0
  for cur_city_no in chromosome:
    distance += city_distance_data[previous_city_no][cur_city_no]
    previous_city_no = cur_city_no

  distance += city_distance_data[previous_city_no][0]

  return distance

def getRandomSequence(city_num):
  chromosome = range(1, city_num)
  ## randomize chromosome
  seq = random.shuffle(chromosome)

  ans = [0]
  ans.extend(chromosome)

  return ans

def init(cityNum):
  return getRandomSequence(cityNum)


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



def hillClimbing(graph, parallel):
  row, col = len(graph), len(graph[0])
  cityNum = row
  assert row == col

  curSeq = init(cityNum)
  globalMax = sys.maxint
  globalSeq = None
  while parallel > 0 :
    while True:
      nextSeq = climb( curSeq , graph)
      if nextSeq == None:
        ## termination, because can't find better solution after limited selections.
        return curSeq
      curSeq = nextSeq

    if cost(curSeq, graph) > globalMax:
      globalSeq =curSeq
  return globalSeq


