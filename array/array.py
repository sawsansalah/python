from array import *
# 1- create an array and Traverse it
arr1 = array("i",[1,2,3,4,5,6])
def TraverseArray(array):
    for index in array:
        print(index)

#2- Access indivdual elements in arrays
print("Step 2")
print(arr1[0])
print(arr1[5])
#3- append any value for array using append method note timecomplexity O(1)
print("Step 3")
arr1.append(7)
print(arr1)
#4-insert the value using Insert Method timecompexity 0(n) and if you add at end of array o(1)
print("Step 4")
arr1.insert(2,44)
print(arr1)

#5- Extend array using extend function ....you can extend more than one value ...time complixty = O(n) space = o(array a + array b)
print("Step 5")
arr2 = array('i',[8,9,10,11])
arr1.extend(arr2)
print(arr1)
#6-add items from list to array by using fromlist
print("Step 6")
list1= [12,13,14]
arr1.fromlist(list1)
print(arr1)
#7-Remove element from array Timecoml=O(n) and if your remove last element O(1)
print("Step 7")
arr1.remove(11)
print(arr1)

#8-Remove last array element by using Pop() Time comlexity O(1)
print("Step 8")
arr1.pop()
print(arr1)
#9-Fetch any elements using index()
print("Step 9")
print(arr1.index(13))
#10-Reverse array by using Reverse method
print("Step 10")
arr1.reverse()
print(arr1)
#11-Get array informaton by Gutting buffer_info method >> provide you with start
print("Step 11")
print(arr1.buffer_info())
#12-check for number occuenese in this array by count method
print("Step 12")
arr1.append(44)
print(arr1.count(44))
#13-convert array to string using tolist method
print("Step 13")
# listTemp = arr1.tolist()
# print(listTemp)
# print(type(listTemp))
#14-convert array to string using tostring method
#16-slice ane elment of array
print("Step 16")
print(arr1[1:4])
print(arr1[:])
