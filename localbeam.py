import random
from  util import fillgraph, drawHist
from data import graph1
def localBeamSearch(graph, beamNum):
  row, col = len(graph), len(graph[0])
  cityNum = row

  beam = initBeam(beamNum, cityNum)

  while True:
    nextSuc = []
    for curState in beam:
      nextbeam = climbToNextBeam(curState, graph, beamNum)

      nextSuc.extend(nextbeam)

    if len(nextbeam) == 1:
      return best(nextbeam, graph)
    if len(nextbeam) == 0 :
      return best(beam, graph)

    beam = selectNextBeam(nextSuc, beamNum, graph)

  return best(beam, graph)



def initBeam(beamNum, cityNum):
  return [getRandomSequence(cityNum) for i in range(beamNum)]


def climbToNextBeam(curState, graph, beamNum):
  row = len(graph)
  curCost = cost(curState, graph)
  beam = []
  for i in range(row):
    for j in range(i + 1, row):
      nextState = curState[:]
      nextState[i], nextState[j] = nextState[j], nextState[i]
      nextCost = cost(nextState, graph)
      if nextCost < curCost:
        beam.append(nextState)
        if len(beam) >= beamNum:
          return beam

  return beam


def selectNextBeam(nextSucs, beamNum, graph):
  tup = [(cost(state, graph), state) for state in nextSucs]
  sortedStates = sorted(tup, key=lambda x: x[0])

  kth= sortedStates[:beamNum]

  return [t[1] for t in kth]

def best(beam, graph):
  return max([cost(state, graph) for state in beam])

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
  random.shuffle(chromosome)

  ans = [0]
  ans.extend(chromosome)

  return ans

if __name__ == "__main__":

  iteration = 50

  print ("begin running local beam search for {0} times".format(iteration))
  fillgraph(graph1)

  scores = []
  for i in range(iteration):
    maxcost = localBeamSearch(graph1, 100)
    print (maxcost)
    scores.append(maxcost)

  print ("final result, tsp min cost = {0}; tsp max cost = {1};tsp average cost = {2}".format(min(scores), max(scores), sum(scores) / (len(scores) + 0.0)))
  drawHist(scores)
