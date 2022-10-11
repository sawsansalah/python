'''To install NumPy on PyCharm, click on File and go to the Settings. Under Settings, 
choose your Python project and select Python Interpreter. Then, search for the NumPy package and click Install Package '''

import numpy as np
#Day1 =======  1,10,11
#Day2 =======  5,4,10
#Day3 =======  24,50,12

TwoDArr= np.array([[1,10,11],[5,4,10],[24,50,12]])
print(TwoDArr)
print("*"*70)
# adding columns [77,66,33] at beginging of array
NewArray = np.insert(TwoDArr,0,[[77,66,33]],axis=1)
print(NewArray)
print("*"*70)
NewArray = np.insert(TwoDArr,1,[[0,0,0]],axis=0)
print(NewArray)
print("*"*70)
# you can use Function append at End of array axis =0 as raw and 1 for coulmns
NewArray = np.append(TwoDArr,[[8,8,8]],axis=0)
print(NewArray)

print("#"*70)
print(len(NewArray[0]))
# Access an elements of Two Dimension Array
def accessElement(array,rowIndex,colmIndex):
    if rowIndex >= len(array) and colmIndex >= len(array[0]):
        print("Element not found")
    else:
        print(array[rowIndex][colmIndex])


#Traversing Two Dimension
def TraversArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
TArr = np.array([[1,10,11],[5,4,10],[24,50,12]])
TraversArray(TArr)

#searing in Two Dimensianal Array
def SearchArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "The value found in index" +str(i)+""+str(j)

    return "The Value not Found"

#delete Function
TwoDArr= np.array([[1,10,11],[5,4,10],[24,50,12]])
newArray = np.delete(TwoDArr,0,axis=1)
print(newArray)
