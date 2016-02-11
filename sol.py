#! /usr/env/bin/python
from splitOrders import *
from parse_input import *

def distributeTasks(orders, drones, warehouses):
  tasks = splitOrders(orders)
  while len(tasks) > 0:
    (task, drone) = getBest(tasks, drones, warehouses)
    drone.assign(task)

  # Now we are finished
  writeOutput(drones)

def getBest(tasks, drones, warehouses):
  bestCost, bestPair = None, None
  for drone in drones:
    for taskId, task in enumerate(tasks):
      cost = costOfPair(drone, task, warehouses)
      if bestCost == None or cost < bestCost:
        bestCost = cost
        bestPair = (taskId, task, drone)
  del tasks[taskId]
  return bestPair[1:]

def costOfPair(drone, task, warehouses):
  warehouse = getWarehouse(drone, task, warehouses)
  toHouse = distanceSquared(drone.location, warehouse.location)
  toCustomer = distanceSquared(warehouse.location, task.location)
  return toHouse + toCustomer

def getWarehouse(drone, task, warehouses):
  #TODO
  return warehouses[0]

def distanceSquared(x, y):
  return (x[0]-y[0])**2 + (x[1]-y[0])**2

def writeOutput(drones):
  with open('output.txt', 'w') as f:
    for drone in drones:
      f.write(drone.getOutput())

class Drone(object):
  def __init__(self):
    self.location = (0, 0)
    self.history = []

  def assign(self, task):
    # TODO
    pass

  def getOutput(self):
    #TODO
    pass

if __name__ == "__main__":
  n_rows, n_columns, n_drones, turns, max_payload, n_product_types, weights, n_warehouses, warehouses, n_orders, orders = parseStuff()
  drones = []
  for _ in range(n_drones):
    drones.append(Drone())
  print n_rows
  distributeTasks(orders, drones, warehouses)


