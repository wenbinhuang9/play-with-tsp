from  util import fillgraph, drawHist, median, mean
from data import graph1
import  probabilisticmst
import  msthillclimbing
def cost(chromosome, city_distance_data):
  distance = 0
  previous_city_no = 0
  for cur_city_no in chromosome:
    distance += city_distance_data[previous_city_no][cur_city_no]
    previous_city_no = cur_city_no

  distance += city_distance_data[previous_city_no][0]

  return distance

if __name__ == "__main__":
    runTimes = 200
    fillgraph(graph1)
    print ("begin running probabilistic mst heuristic hill climbing for {0} times".format(runTimes))

    ans = []
    for i in range(runTimes):
        tree = probabilisticmst.probabilisticmst(graph1)

        seq = msthillclimbing.hillClimbing(graph1, tree)

        seq_cost = cost(seq, graph1)
        print (seq_cost)
        ans.append((seq, seq_cost))

    cost_list = [float(ans[i][1]) for i in range(len(ans))]

    print ("final result, tsp min cost = {0}; tsp max cost = {1};tsp average cost = {2}".format(min(cost_list),
                                                                                                max(cost_list),
                                                                                                sum(cost_list) / (len(
                                                                                                    cost_list) + 0.0)))
    drawHist(cost_list)