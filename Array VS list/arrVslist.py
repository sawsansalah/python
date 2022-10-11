# Arrays Vs lists
import numpy as np
# you can operate Arithmetic Operations via array not by list
myarray = np.array([1,2,3,4,5])
myList = [1,2,3,4,5]
print(myarray /2 )
# print(myList /2 ) can not opraete division on  list

# Data type in list can be different in list
myarray = np.array([1,2,3,4,5,'a'])
myList = [1,2,3,4,5,'a']
print(myarray)
print(myList)
