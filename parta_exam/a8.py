from functools import reduce
import operator
list1=[int(x) for x in input().split() ]
print(list1)
list2=[3*x for x in list1]
print(list2)
sum1=reduce(lambda x,y:x+y,list1)
print("Sum of original list:",sum1)
sum2=reduce(lambda x,y:x+y,list2)
print("Sum of multiplied list",sum2)

