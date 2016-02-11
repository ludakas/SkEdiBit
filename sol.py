#! /usr/env/bin/python
from splitOrders import *
from parse_input import *

TURNS = 0
def distributeTasks(orders, drones, warehouses):
  tasks = splitOrders(orders, max_payload, weights)
  while len(tasks) > 0:
    (task, drone, warehouse) = getBest(tasks, drones, warehouses)
    drone.assign(task, warehouse)

  # Now we are finished
  writeOutput(drones)

def getBest(tasks, drones, warehouses):
  bestCost, bestPair = None, None
  for drone in drones:
    for taskId, task in enumerate(tasks):
      cost = costOfPair(drone, task, warehouses)
      cost, warehouse = costOfPair(drone, task, warehouses)
      if bestCost == None or cost < bestCost:
        bestCost = cost
        bestPair = (taskId, task, drone, warehouse)
  del tasks[taskId]
  return bestPair[1:]

def costOfPair(drone, task, warehouses):
  warehouse = getWarehouse(drone, task, warehouses)
  print type(warehouse), type(drone), type(task)
  toHouse = distance(drone.location, warehouse.location)
  toCustomer = distance(warehouse.location, task.location)
  timeToFinish = toHouse + toCustomer + drone.available
  if timeToFinish > TURNS:
    return sys.maxint, warehouse
  return toHouse + toCustomer + drone.available, warehouse

def getWarehouse(drone, task, warehouses):
  item_type = task.item_type
  n_items = task.n_items
  for warehouse in warehouses:
    if warehouse.items[item_type] >= n_items:
      return warehouse
  print item_type, n_items
  raise ValueError("WTF - should not happen")

def distance(x, y):
  return np.sqrt((x[0]-y[0])**2 + (x[1]-y[0])**2)

def writeOutput(drones):
  with open('output.txt', 'w') as f:
    n = 0
    for drone in drones:
      n += 2*len(drone.history)
    f.write(str(n)+'\n')

    for drone in drones:
      f.write(drone.getOutput())

class Drone(object):
  def __init__(self, id):
    self.id = id
    self.location = (0, 0)
    self.history = []
    self.available = 0

  def assign(self, task, warehouse):
    assert warehouse.items[task.item_type]>=task.n_items, "not enough items in the warehouse"

    warehouse.items[task.item_type] -= task.n_items
    self.history.append((task,warehouse))
    self.available += np.ceil( distance(self.location, task.location) ) + 1
    self.location = task.location


  def getOutput(self):
    output = ''

    for (wh, task) in self.history:
        output += self.id+' L '+wh.id+' '+task.item_type+' '+task.n_items+'\n'
        output += self.id+' D '+task.id+' '+task.item_type+' '+task.n_items+'\n'

if __name__ == "__main__":
  n_rows, n_columns, n_drones, turns, max_payload, n_product_types, weights, n_warehouses, warehouses, n_orders, orders = parseStuff()
  TURNS = turns
  drones = []
  for i in range(n_drones):
    drones.append(Drone(i))
  print n_rows
  distributeTasks(orders, drones, warehouses)


