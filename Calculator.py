import math
a=1
while a>0:
    print("Enter first number.")
    b=int(input())
    print("Enter Operator")
    c=input()
    if c=="sqrt":
        print("The square root of",b,"is",math.sqrt(b),"\n")
    else:
        print("Enter second number.")
        d=int(input())
    if c=="/2":
        print("The average is",(b+d)/2,"\n")
    elif c=="+":
        print("The sum is",b+d,"\n")
    elif c=="**":
        print("The answer of",b,"raised to the power of",d,"is",b**d,"\n")
    elif c=="-":
        print("The difference is",b-d,"\n")
    elif c=="/%":
        print("The qoutient is",int(b/d),"and the remainder is",b%d,"\n")
    elif c=="*":
        print("The product is",b*d,"\n") 
    elif c=="/":
        print("The quotient is",b/d,"\n")
else:
    print("Invaid Input!!\n")   
  
