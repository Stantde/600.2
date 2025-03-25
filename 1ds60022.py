"""

As a burgler robs a house, she finds the following items:

Dirt - Weight: 4, Value: 0
Computer - Weight: 10, Value: 30
Fork - Weight: 5, Value: 1
Problem Set - Weight: 0, Value: -10
This time, she can only carry a weight of 14, and wishes to maximize the value to weight ratio of the things she carries. She employs three different metrics in an attempt to do this, and writes an algorithm in Python to determine which loot to take.

The algorithm works as follows:

Evaluate the metric of each item. Each metric returns a numerical value for each item.
For each item, from highest metric value to lowest, add the item if there is room in the bag.
Describe the heuristic that each of the following 3 metrics uses, and choose the result of running the algorithm with each metric.

def metric1(item):
    return item.getValue() / item.getWeight()

def metric2(item):
    return  -item.getWeight()

def metric3(item):
    return item.getValue()
   
"""
MAX_WEIGHT = 14
NAMES = ['Dirt', 'Computer', 'Fork', 'Problem Set']
WEIGHTS = [4,10,5,0]
VALUES = [0,30, 1, -10]

class Lootable(object):
    def __init__(self, n, w, v):
        self.name = n
        self.value = v
        self.weight = w

    def __str__(self):
        return f"{self.name} :< {self.value}, {self.weight} >"

    def getValue(self):
        return self.value
   
    def getWeight(self):
        return self.weight
   
def print_list(list):
    for i in list:
        print(i)
    ranking(list)
    return
   
def metric1(item):
    try:
        item.getValue() / item.getWeight()
    except ZeroDivisionError:
        return 1000
    return item.getValue() / item.getWeight()

def metric2(item):
    return -item.getWeight()

def metric3(item):
    return

def apply_metric(list, sort_key):
    carry_weight = 0
    metric_list = []    
    for loot in sorted(list, reverse=True, key=sort_key):
        if carry_weight + loot.getWeight() <= MAX_WEIGHT:
            carry_weight += loot.getWeight()
            metric_list.append(loot)
    return metric_list

def ranking(list):
    total = 0
    for item in list:
        total += item.getValue()
    print(total)
    return total
   
   
def main():
    loot_table = []
    for i in range(len(NAMES)):
        loot = Lootable(NAMES[i], WEIGHTS[i], VALUES[i])
        loot_table.append(loot)
    metric_1_result = apply_metric(loot_table, metric1)
    metric_2_result = apply_metric(loot_table, metric2)
    #metric_3_result = apply_metric(loot_table, metric3)
   
    #print(metric_1_result)
    print("Results of metric 1: ")
    print_list(metric_1_result)
    print("Results of metric 2: ")
    print_list(metric_2_result)
    print("Results of metric 3: ")
    #print_list(metric_3_result)
    return

if __name__ == "__main__":
    main()

'''
# Code to print items in loot_table
for stuff in loot_table:
    print(stuff) # '''
