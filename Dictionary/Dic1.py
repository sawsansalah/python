# dictionary is unordered , changeable , indexe
# how to create a dictionary
# 1 ) you can define dictionary by using dict() Function

mydict = dict()
print(mydict)
# 2
secondDict = {}
print(secondDict)
# 3
enToSp = {"one":"uno","two":"dos","three":"tres"}
print(enToSp)
print(enToSp['one']) # access by key and time complexity is O(1)

# 4 update /add an elements to the Dic
myDict = {'name':'sawsan','age':26} # time complexity is O(1) and space complexity o(1)
myDict['age'] = 27
print(myDict)
myDict['name'] = "Dina"
print(myDict) # adding
myDict['address'] = "Giza" # time complexity is O(1) and space complexity o(1)
print(myDict)
print("*"*80)
#Traverse through Dic
def traverse(dict):
    for key in dict:  ### o(n) time complixity
        print(key,dict[key]) #o(1) so all time complexity o(n) and space complexity 0(1)

# Searching for value
d1 = {'name': 'Dina', 'age': 27, 'address': 'Giza'}
def SearchDic(dict,value):# time complexity o(n) and spacecompiexity o(1)
    for key in dict:#.....o(n)
        if dict[key] == value : #.........o(1)
            return key,value # .......o(1)
    return 'The value does not exit '





print("*"*80)

# Delete an elements from Dic
print(d1)
d1.pop('name')
print(d1)
d1['Education'] = 'Engineering'
d1['name'] = 'sawsan'
d1['age'] = '26'
print(d1)
# using pop item () method , pop item select random value and delete it
print(d1.popitem())
print(d1)
# clear your Dic
d1.clear()
print(d1)

# use del

d2 = {'age': '26', 'address': 'Giza', 'Education': 'Engineering', 'name': 'sawsan'}
del d2['age']
print(d2)
# can use delete to delete entire dict
del d1
# print(d1) will provide NameError: name 'd1' is not defined becuse it is delete
