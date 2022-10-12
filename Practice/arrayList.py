# Temperature Days take from user and provide with Average and return how many Days above average 

NumberOfDays = int(input("How Many Day's Temperature ? "))
Mylist = []
for temp in range(NumberOfDays):
    Day = int(input("Day"+str(temp + 1)+"'s temp : "))
    Mylist.append(Day)
AVG = sum(Mylist)/len(Mylist)
print("Average = ",round(AVG))
count = 0
for i in Mylist:
    if i > AVG:
      count = count + 1
print(count,"day's above average ")
