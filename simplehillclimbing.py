import random

def hillClimbing(graph):
  cityNum, row, col = len(graph), len(graph), len(graph[0])

  curState = getRandomSequence(cityNum)

  while True:
    nextState = climb( curState , graph)

    if nextState == None:
      ## we have got to a optimality point
      return curState

    curState = nextState

  return curState


## climb to next states with lower cost
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


def getRandomSequence(city_num):
  chromosome = range(1, city_num)
  random.shuffle(chromosome)

  state = [0]
  state.extend(chromosome)
  return state

def cost(chromosome, city_distance_data):
  distance = 0
  previous_city_no = 0
  for cur_city_no in chromosome:
    distance += city_distance_data[previous_city_no][cur_city_no]
    previous_city_no = cur_city_no

  distance += city_distance_data[previous_city_no][0]

  return distance




