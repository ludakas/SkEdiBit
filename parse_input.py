import sys
import numpy as np



class Warehouse(object):
    """docstring for Warehouse"""
    def __init__(self, id, r, c, items):
        super(Warehouse, self).__init__()
        self.id = id
        self.r = r
        self.c = c
        self.items = items
        self.location = (r, c)

class Order(object):
    """docstring for Order"""
    def __init__(self,id,r,c,n_items,items):
        super(Order, self).__init__()
        self.id = id
        self.r = r
        self.c = c
        self.n_items = n_items
        self.items = items
        self.location = (r, c)


class Task(object):
    """docstring for Order"""
    def __init__(self,id,r,c,item_type,n_items):
        super(Task, self).__init__()
        self.id = id
        self.r = r
        self.c = c
        self.item_type = item_type
        self.n_items = n_items
        self.location = (r,c)


def str2int(string_list):
    return map(lambda x: int(x), string_list)

def parseStuff():
  f = open('input/demo.in', 'r')
  n_rows, n_columns, n_drones, turns, max_payload = str2int(f.readline().split())
  n_product_types = int(f.readline())
  weights = f.readline().split()
  weights = str2int(weights) # map(lambda x: int(x), weights)
  n_warehouses = int(f.readline())

  warehouses = []
  for i in xrange(n_warehouses):
      r, c = str2int( f.readline().split() )
      items = str2int( f.readline().split() )
      warehouses.append(Warehouse(i,r,c,items))


  n_orders = int(f.readline())

  orders = []
  for i in range(n_orders):
      r,c = str2int( f.readline().split() )
      n_items = int( f.readline() )
      items = np.zeros(n_product_types, dtype=int)
      items_list = str2int( f.readline().split() )
      for e in items_list:
          items[e] += 1

      orders.append(Order(i,r,c,n_items,items))

 #print 'n_rows',n_rows, 'n_columns',n_columns, 'n_drones',n_drones, 'turns',turns, 'max_payload',turns
 #print 'n_product_types',n_product_types

 #print 'n_warehouses',n_warehouses
 #print 'warehouses[0].r',warehouses[0].r

 #print 'n_orders',n_orders
 #print 'orders[0].c',orders[0].c
 #print 'orders[0].items[785]',orders[0].items[785]

  f.close()

  return n_rows, n_columns, n_drones, turns, max_payload, n_product_types, weights, n_warehouses, warehouses, n_orders, orders


