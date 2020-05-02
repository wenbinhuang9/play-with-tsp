
## A heuristic with probability graph
from randomhillclimbing import cost, climb

from  random import  uniform
import  bisect
def nearestProbabilityHeuristic(proTable):
    pro = uniform(0, 1)


    cityNum = len(proGraph)
    seq = [0]
    start = 0

    ## select the next point by probability!!!
