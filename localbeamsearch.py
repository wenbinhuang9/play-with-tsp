import  random

def localBeamSearch(graph, beamNum):
  row, col = len(graph), len(graph[0])
  cityNum = row

  beam = initBeam(beamNum, cityNum)

  while True:
    nextSuc = []
    for curState in beam:
      successors = climbToNextKSuccessors(curState, graph, beamNum)

      nextSuc.extend(successors)

    if len(successors) == 1:
      return best(successors, graph)
    if len(successors) == 0 :
      return best(beam, graph)

    beam = selectNextKSuccessors(nextSuc, beamNum, graph)

  return best(beam, graph)


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

def initBeam(beamNum, cityNum):
  return [getRandomSequence(cityNum) for i in range(beamNum)]


def climbToNextKSuccessors(curState, graph, beamNum):
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


def selectNextKSuccessors(nextSucs, beamNum, graph):
  tup = [(cost(state, graph), state) for state in nextSucs]
  sortedStates = sorted(tup, key=lambda x: x[0])

  kth= sortedStates[:beamNum]

  return [t[1] for t in kth]

def best(beam, graph):
  return max([cost(state, graph) for state in beam])



