n=int(input("enter number:"))
r=0
while(n!=0):
    rem= n%10
    r=r*10+rem
    n=n//10
print("reversed number is :",r)
    


