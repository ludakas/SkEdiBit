#! /usr/env/bin/python

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
    for taskId, tasks in enumerate(tasks):
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

def distanceSquared(x, y):
  return (x[0]-y[0])**2 + (x[1]-y[0])**2

def writeOutput(drones):
  with open('output.txt') as f:
  for drone in drones:
    f.write(drone.getOutput())

if __name__ == "__main__":
  distributeTasks(orders, drones, warehouses)



