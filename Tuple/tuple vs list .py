# Tuple vs Lists
list1 = [0,1,2,3,4,5,6,7]
list1[3] = 7
print(list1)
list1 = [100,200,70,88]
print(list1)
del list1[-1]
print(list1)
###################
tuple1 = (0,1,2,3,4,5,6,7)
# tuple1[1] = 7 TypeError: 'tuple' object does not support item assignment
print(tuple1)
tuple1 = (100,200,70,88) # you can reassign all tuples
print(tuple1)
# del tuple1[0] #TypeError: 'tuple' object doesn't support item deletion
print(tuple1)
# del(tuple1)
###########
# Tuple can be store in list
# list can be stores in tuples
list1 = [(1,2),(3,4),(5,6)]
print(list1)
tuple1 = ([4,5],[6,7])
