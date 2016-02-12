from parse_input import *
import math

# Splits orders into tasks.
# Assumes items in each order are sorted !!!!
def splitOrders(orders, max_payload, weights):
    print 'starting splitOrders'
    maxItemsInOrder = 40 # Rough estimate
    tasks = []
    tasksByOrderSize = []
    for i in range(maxItemsInOrder):
        tasksByOrderSize.append([])

    for o in orders:
    
        index = 0
        for i in range(len(o.items)):

            if o.items[i] > 0:

                n_items = o.items[i]
                while (n_items*weights[i] > max_payload):
                    max_items = int(math.floor((0.0+max_payload)/weights[i]))
                    index += 1
                    n_items = n_items - max_items
                    
                index += 1

        #index = o.n_items
        for i in range(len(o.items)):

            if o.items[i] > 0:

                while (o.items[i]*weights[i] > max_payload):
                    max_items = int(math.floor((0.0+max_payload)/weights[i]))
                    newTask = Task(o.id, o.r, o.c, i, max_items)
                    tasksByOrderSize[index].append(newTask)

                    o.items[i] = o.items[i] - max_items
                newTask = Task(o.id, o.r, o.c, i, o.items[i])
                tasksByOrderSize[index].append(newTask)

    for i in range(maxItemsInOrder):
        print str(i) + ' ' + str(len(tasksByOrderSize[i]))
        tasks += tasksByOrderSize[i]
                
                
                
    print 'ending splitorders'
    return tasks



# class Object(object):
    # pass

# dummy1 = Object()
# dummy1.r = 5
# dummy1.c = 5
# dummy1.noItems = 3
# dummy1.items = [0, 0, 1]
# dummyOrders = [dummy1]

# dummy2 = Object()
# dummy2.r = 4
# dummy2.c = 4
# dummy2.noItems = 6
# dummy2.items = [0, 0, 1, 3, 3, 3]
# dummyOrders.append(dummy2)

# tasks = splitOrders(dummyOrders)

# for t in tasks:
   # print str(t.r) + ' ' + str(t.c) + ' ' + str(t.type) + ' ' + str(t.count)


