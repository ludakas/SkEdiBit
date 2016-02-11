# Splits orders into tasks.
# Assumes items in each order are sorted !!!!
def splitOrders(orders):
    tasks = []
    
    for o in orders:
        
        lastItem = -1
        count = 0
        for item in o.items:
            
            if item == lastItem:
                count += 1
            else:
                # Save previous
                if (lastItem != -1):
                    newTask = Object()
                    newTask.r = o.r
                    newTask.c = o.c
                    newTask.type = lastItem
                    newTask.count = count
                    tasks.append(newTask)
                
                # Set up next
                count = 1
                lastItem = item
         
         
        # Save last item
        newTask = Object()
        newTask.r = o.r
        newTask.c = o.c
        newTask.type = lastItem
        newTask.count = count
        tasks.append(newTask)
     
    return tasks
    
    
    
class Object(object):
    pass
    
dummy1 = Object()
dummy1.r = 5
dummy1.c = 5
dummy1.noItems = 3
dummy1.items = [0, 0, 1]
dummyOrders = [dummy1]

dummy2 = Object()
dummy2.r = 4
dummy2.c = 4
dummy2.noItems = 6
dummy2.items = [0, 0, 1, 3, 3, 3]
dummyOrders.append(dummy2)

tasks = splitOrders(dummyOrders)

for t in tasks:
    print str(t.r) + ' ' + str(t.c) + ' ' + str(t.type) + ' ' + str(t.count)
    
    