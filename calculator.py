# bhavesh-multi,divide
#addition subtraction -himanshu
#harsh -power
def multi() :
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    return print(f"Multiplication = {a*b}")

def divide() : 
    a = float(input("enter nominator : "))
    b = float(input("enter denominator : "))

    while b==0:
        print("Denominator cannot be zero")
        b = float(input("enter denominator : "))
        return print(f"Division = {a/b}")


def power():
    a=float(input("enter number for base : "))
    b=float(input("enter number for power : "))
    if (b==0):
        print(1)
    elif(b>0):
        c=1
        for i in range(0,int(b)):
            c=c*a
        print(c)
    else:
        b=-(b)
        c=1
        for i in range(0,int(b)):
            c=c*a
        print(a)
num=int(input("enter 1 if you want to ADDITION OR SUBTRACTION :: \nenter 2 if you want to MULTIPLICATION OR DIVISION ::\nenter 3 if you want to find POWER ::  \n"))
if(num==5):
    power()
elif(num==2):
    sub(1)
elif(num==3):
    multi()
elif(num ==4):
    divide()
    

