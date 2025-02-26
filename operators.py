def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=input("enter your operation:")
if(c=='add'or c=='+'):
    ad=add(a,b)
    print("add a and b is:",ad)
elif(c=='sub' or c=='-'):
    dif=sub(a,b)
    print("sub a and b is:",dif)
elif(c=='mul' or c=='x'):
    mult=mul(a,b)
    print("mul a and b is:",mult)
elif(c=='div' or c=='/'):
    divi=div(a,b)
    print("div a and b is:",divi)
      
      

