# How to find the missing  numbers in an intger array of 1 to 100 ?
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
def missNo(list,n):
   sum1 = 100 * 101 /2
   sum2 = sum(list2)
   print(sum1 - sum2)
missNo(list2,100)

To Define it in function 
myList = [1,2,3,4,5,6,7,9,10]
def missingNumer(list,totalcount):
    expectedSum = (( totalcount + 1 ) * totalcount ) /2
    sum = 0
    for i in list:
        sum = sum + i
    return (expectedSum - sum)
print(missingNumer(myList,10))


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def TwoSum(nums,target):

   for i in range(len(nums)):
        for j in range(i+1,len(nums)):
           if nums[i] == nums[j]:
              continue
           if nums[i]+nums[j] == target:
              print(i,j)

# How to check if an array contains anumber in python
import numpy as np
myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25])
def SearchArray(array,value):
   for i in range(len(array)):
      if array[i] == value :
         return "value found at ",str(i)
   return "The value of not found"

# how to calculate max product of Array :
def MaxProudct(array):
   maxproudect = 0
   for i in range(len(array)):
      for j in range(i+1,len(array)):
         if array[i] * array[j] > maxproudect:
            maxproudect = array[i] * array[j]
            pairs = str(array[i]) + " "+str(array[j])
   print(maxproudect)
   print(f"pairs at {pairs}")
MaxProudct(myArray)


# define if list containe unique or dublicate numbers

mylist = [1,2,3,4,3,1,5,6]
# to difine if list unique or nor
def isUnique(list):
  if len(list) == len(set(list)):
      return True
  else:
      return False
def isun(list):
    a = []
    for i in list:
        if i in a :
            return True
        else:
            a.append(i)
            return False
print("*$"*80)

print(isun(mylist))
# define program to remove repeated items in list
def removeDup(list):
    unique = []
    for items in list:
        if items not in unique:
           unique.append(items)
           print(unique)
print(removeDup(mylist))
print("*"*80)
# to print all duplicate in list
def dupl(list):
    dup = []
    for i in range(len(list)):
        for j in range(i+1,len(list)):

            if list[i] == list[j]:
                dup.append(list[i])
    return dup
# Define program to check if list 1 equal to list 2

list1 = ["c","a","t"]
list2 = ["a","t","c","d"]
def permutation(list1,list2):
    if len(list1) != len(list2):
       return False
    else:
         list1.sort()
         list2.sort()
         if list1 == list2 :
             return True
print(dupl(mylist))






