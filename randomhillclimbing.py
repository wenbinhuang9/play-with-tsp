import  random
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

def getRandomSequence(city_num):
  chromosome = range(1, city_num)
  ## randomize chromosome
  seq = random.shuffle(chromosome)

  ans = [0]
  ans.extend(chromosome)

  return ans

def init(cityNum):
  return getRandomSequence(cityNum)

## accept a bad result when we can't go forward???
def climb(seq, randomSelectionTimes, cityNum, graph):
  while randomSelectionTimes > 0:
    nextSeq = getRandomSequence(cityNum)
    if cost(nextSeq, graph) < cost(seq, graph):
      return nextSeq
    randomSelectionTimes -= 1

  return None

def hillClimbing(graph, iteration, randomSelectionTimes):
  row, col = len(graph), len(graph[0])
  cityNum = row
  assert row == col

  seq = init(cityNum)

  while iteration > 0:
    nextSeq = climb(seq, randomSelectionTimes, cityNum, graph)
    if nextSeq == None:
      ## termination, because can't find better solution after limited selections.
      return seq
    iteration -= 1

  return nextSeq


