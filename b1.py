from collections import Counter
#a
def rever_list(x):
    return x[::-1]

def remov_dup(y):
    return list(dict.fromkeys(y))

print("Enter the list")
list1=[x for x in input().split()]
list4=remov_dup(list1)
print(list4)


n=int(input("Enter the no till which you want the even no list\n"))
list2=[x for x in range(n) if (x%2==0)]
list3=remov_dup(list2)
print(list2)
print(list3)


#b
f=open("myfile.txt","r")

def word_counter(fname):
    with open(fname) as f:
        return Counter(f.read().split())

print("NO of words in the file are:",word_counter("myfile.txt"))
#c
print("Enter the no list")
list5=[int(x) for x in input().split()]
def findMax(a):
    if len(a)==1:
        return a[0]
    else:
        return max(a[0],findMax(a[1:]))

print(findMax(list5))
