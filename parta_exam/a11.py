mystrings=['hey i am akshay','hey i am vivek','hey i am shashwat','hey hows your life going on 9']
print(mystrings)
a=len(mystrings)

for i in range(a):
	if i%2==0:
		print(mystrings[i])

for i in range(a):
        if i!=0:
            if i%2==0:
                mystrings[i]=mystrings[i].upper()
                
print(mystrings)

for i in range(a):
	mystrings[i]=" ".join(reversed(mystrings[i].split()))
print("On reversal",mystrings)

num=[]
for i in range(a):
	for s in mystrings[i].split():
		 if s.isdigit():
		 	num.append(s)
		 	
print(num)