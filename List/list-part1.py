intgers = [1,2,3,4]
print(intgers)
StrinList = ["sawsan","Ahmed", "Dina"]
print(StrinList)
MixList = ["a",1,5,7,5.00]
print(MixList)
nestedList = [1,4,"spam",[1.8,1.8],['Test']]
print(nestedList)
empty =[]
print(empty)
print("*"*100)
# Accessing /Traversing the list
shoppingList = ["Milk","Cheese","Butter"]
print(shoppingList[0]) #access First Element
print(shoppingList[1])
print('Milk' in shoppingList)
print('Tom' in shoppingList)
print(shoppingList[-1])
print(shoppingList[-2])
print("*"*100)
for index in shoppingList:
    print(index)
print("*"*100)
count = 0
for i in range(len(shoppingList)):
    count = count + i
print(count)
print("*"*100)
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
print(shoppingList)
print("*"*100)
empty = []
for i in empty: # we have nothing in empty to loop on it
    print("i am empty")
print("*"*100)

# update/Insert - list note update element is O(1) and space compilcity = o(1)
myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
myList[4] = 55
print(myList)
print("*"*100)
myList = [1,2,3,4,5,6,7] # time complexity 0(N) by using insert
myList.insert(0,11)
print(myList)
myList.insert(4,99)

print(myList)

myList.append(100) # in append time comp O(1)
print(myList)
print("*"*100)
list2 = [200,300,400]
myList.extend(list2) # Time complecity o(n) and space complicity 0(n)
print(myList)

print("*"*100)
myList = ['a','b','c','d','e','f']
print(myList[1:])
print(myList[:2])
print(myList[:])
#update more than elements in list
myList[0:2] = ['x','y']
print(myList)
#delete method by pop method timecomplicity 0(n) and delete last elements o(1) ,space complecity 0(1)
myList.pop(1)
print(myList)
# we use pop to keep the item deleted
temp = myList.pop()
print(temp)
print(myList)
print("*"*100)
# delete by using delete() method and Time complexity o(n) space complixity 0(1)
myList = ['a','b','c','d','e','f']
del myList[0]
print(myList)
del myList[1:3]
print(myList)
print("*"*100)
# delete by using Remove() method >> method and Time complexity o(n) space complixity 0(1)
myList = ['a','b','c','d','e','f']
myList.remove('e')
print(myList)
print("*"*100)

#Searching for an elements in the list

myList = [10,20,30,40,50,60,70,80,90]
#1-by using IN opeartor
if 20 in myList:  ### time complicity is o(n)
    print(myList.index(20))
else:
    print("the value not found ")

# 2 - linear Search
def Searchele(list,value):
    for i in  list:
        if i == value:
           return "the value found in index " + str(list.index(i))

    return "The value not found"

print(Searchele(myList,5))
print("*"*100)

# list operations /Functions

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
# by using * operator
a = [0,1]
print(a * 4)
print("*"*100)
# to get number of elements
list = [0,1,2,3,4,5,6]
print(len(list))
# to find Max() to get max. number
print(max(list))
print(min(list)) ## to get min numbers in your list
print(sum(list))   ## to get sum of list instead of looping on list
print(sum(list)/len(list)) ## get the average of list

# Example
total = 0
count = 0
# while(True):
#
#     inp = input("please Enter Value :")
#     if inp == 'Done':
#         break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     avg = total / count
# print("the average is ",avg)

# conver the average code to list

leng = int(input("Enter leng of list : "))
 list = []
 for i in range(leng):
     number = int(input("Enter Value: "))
     list.append(number)
 print(sum(list)/len(list))

# strings and lists
a = "sawsan"
b = list(a)
print(b)
# using split() by default it splits by space
a = 'spam spam spam'
b = a.split()
print(b)
a = "sawsan salah eldin"
b = a.split()
print(b)
print("*"*70)
a = "sawsan-salah-eldin"
b = a.split("-")
print(b)
# to revert to string again by using join()
c = "-".join(b)
print(c)

# Pitfalls and ways to avoid them
# this is wrong output with none
print("*"*100)
mylist = [2,4,3,1,5,7]
# mylist = mylist.sort() by adding this value  led to none function
print(mylist)
mylist.sort()
print(mylist)
print("*"*100)
# mylist append
mylist.append(10)
print(mylist)
# you need to take copy of original list
mylist = [2,4,3,1,5,7]
origin = mylist[:]
mylist.append(77)
print(mylist)
print(origin)
