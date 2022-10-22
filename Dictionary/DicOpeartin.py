myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}
# use in operator to
print('eooooa'in myDict) # you can use in opearter for keys only
print(2 in myDict.values()) # to check values found in Dic. use function dic.values() , time complexity 0(n)
print("*"*70)
# use for loop to access key
for key in myDict:
    print(key)
print("*"*70)
# use for loop to access value time complexity o(n)
for key in myDict:
    print(myDict[key])
# use for loop to access key and value time complexity o(n)
for key in myDict:
    print(key,myDict[key])
print("*"*70)
# all() method return true if all itmes are true
print(all(myDict))
myDict1 = {1:True,2:True}
print(all(myDict1))
myDict1 = {0:False , 2:False}
print(all(myDict1))
d = {0: "Hello", 1: "Hi"} # add 0 convert To true
print(all(d))
d = {}
print(all(d))
print("*"*70)
#any () any elements will return true
l = [False, False, True, False, False]
print(any(l))

d = {}
print(any(d))
print("*"*70)
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}
print(len(myDict))
print("*"*70)
#to sort keys you can use sorted()
myDic = {4:"e",5:"c",88:"z",1:"f"}
print(sorted(myDic,))
print(sorted(myDic, reverse=True))
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}
print(sorted(myDict,key=len))
