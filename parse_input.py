import sys
import numpy as np



class Warehouse(object):
    """docstring for Warehouse"""
    def __init__(self, r, c, items):
        super(Warehouse, self).__init__()
        self.r = r
        self.c = c
        self.items = items

class Order(object):
    """docstring for Order"""
    def __init__(self, r,c,n_items,items):
        super(Order, self).__init__()
        self.r = r
        self.c = c
        self.n_items = n_items
        self.items = items
        

def str2int(string_list):
    return map(lambda x: int(x), string_list)


f = open('mother_of_all_warehouses.in', 'r')




n_rows, n_columns, n_drones, turns, max_payload = str2int(f.readline().split())
n_product_types = int(f.readline())
weights = f.readline().split()
weights = str2int(weights) # map(lambda x: int(x), weights)
n_warehouses = int(f.readline())

warehouses = []
for i in xrange(n_warehouses):
    r, c = str2int( f.readline().split() )
    items = str2int( f.readline().split() )
    warehouses.append(Warehouse(r,c,items))


n_orders = int(f.readline())

orders = []
for i in range(n_orders):
    r,c = str2int( f.readline().split() )
    n_items = int( f.readline() )
    items = np.zeros(n_product_types, dtype=int)
    items_list = str2int( f.readline().split() )
    for e in items_list:
        items[e] += 1

    orders.append(Order(r,c,n_items,items))



print 'n_rows',n_rows, 'n_columns',n_columns, 'n_drones',n_drones, 'turns',turns, 'max_payload',turns
print 'n_product_types',n_product_types

print 'n_warehouses',n_warehouses
print 'warehouses[0].r',warehouses[0].r

print 'n_orders',n_orders
print 'orders[0].c',orders[0].c 
print 'orders[0].items[785]',orders[0].items[785]

f.close()

