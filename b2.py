from operator import itemgetter
loop_end_value=1
conversions=[]
def c2k():
    cel=int(input("Enter the celsius value:"))
    kel=cel+273
    conversions.append(('C',cel,'K',kel))
    print("Kelvin value is:",kel)
def k2c():
    kel=int(input("Enter the kelvin value:"))
    cel=kel-273
    conversions.append(('K',kel,'C',cel))
    print("Celsius value is:",cel)
def c2f():
    cel=int(input("Enter the celsius value:"))
    fah=(1.8*cel)+32
    conversions.append(('C',cel,'F',fah))
    print("Fahrenite value is:",fah)
def f2c():
    fah=int(input("Enter the fahrenite value:"))
    cel=(fah-32)*0.5556
    conversions.append(('F',fah,'C',cel))
    print("Celsius value is:",cel)
def k2f():
    kel=int(input("Enter the kelvin value:"))
    fah=1.8*(kel-273)+32
    conversions.append(('K',kel,'F',fah))
    print("Fahrenite value is:",fah)
def f2k():
    fah=int(input("Enter the fahrenite value:"))
    kel=((fah-32)*0.5556)+273
    conversions.append(('F',fah,'K',kel))
    print("Kelvin value is:",kel)

while loop_end_value==1:
    n=int(input("Enter 1 to convert celsius to kelvin\nEnter 2 to convert kelvin to celsius\nEnter 3 to convert celsius to fahernite\nEnter 4 to convert fahernite to celsius\nEnter 5 to convert kelvin to fahrenite\nEnter 6 to convert fahernite to kelvin\nEnter 7 to view conversions\nEnter 8 to exit\n"))
    if n==1:
        c2k()
    elif n==2:
        k2c()
    elif n==3:
        c2f()
    elif n==4:
        f2c()
    elif n==5:
        k2f()
    elif n==6:
        f2k()
    elif n==7:
        print("***Display Menu***")
        print("Enter 1 for ascending order of from values")
        print("Enter 2 for descending order of from values")
        print("Enter 3 for ascending order of to values")
        print("Enter 4 for descending order of to value")
        ch=int(input("Enter your choice:"))
        if len(conversions)==0:
            print("No conversions are found")
        elif ch==1:
            c=sorted(conversions,key=itemgetter(1))
            for i in c:
                print(i)
        elif ch==2:
            c=sorted(conversions,key=itemgetter(1),reverse=True)
            for i in c:
                print(i)
        elif ch==3:
            c=sorted(conversions,key=itemgetter(3))
            for i in c:
                print(i)
        elif ch==4:
            c=sorted(conversions,key=itemgetter(3),reverse=True)
            for i in c:
                print(i)
        else:
            print("Invalid choice")
    elif n==8:
        loop_end_value=0
