'''
Tuples 
A tuple is an immutable sequence of python objects
Tuples are also comparable and hashable 
'''
# 1 - create table
t = 'a','b','c','d'
print(type(t))
newTuple = ('a','b','c','d')
print(newTuple)
print(type(newTuple))
# to create Tuple with one element
t3 = ("d",)
print(type(t3))
t4 =("d")
print(type(t4))
# you can use tuble function to create empty
new = tuple()
print(new)
new = tuple('abcderr')
print(new)
'''
Time complexity of creating Tuple 0(1)
space complexity o(n)
the main difference between Tuple and list and Dictionary that are immutable , Once you declare them you can not change them
'''
print("*"*70)
# Access elements
newTuple = ('a','b','c','d')
print(newTuple[1])
print(newTuple[-1])
print(newTuple[-2])
# you can use slice to access tuple
print(newTuple[1:3])
print(newTuple[1:])
print("*"*70)
#Traversing in Tuple by Two Mehod o(n) time complexity and o(1) for space comp.
for i in newTuple:
    print(i)
for i in range(len(newTuple)):
    print(newTuple[i])
# Search for Tuple
def SearchTup(tup,value):
    for i in range(len(tup)):
        if tup[i] == value:
            return "the value at index ",i
    return "The value not found "
print(SearchTup(newTuple,'f'))
print("#"*70)
# 2 - another searching method by using in opearter and it is o(n) 
print('a'in newTuple)
print(newTuple.index('a'))
