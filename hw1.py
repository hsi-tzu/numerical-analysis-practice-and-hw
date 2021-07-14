a= int(input("輸入a(a要大於b)="))
b= int(input("輸入b="))
c= int

def lcm(a,b):
    if a>b:
        g,l=a,b
    else:
        g,l=b,a
        
    while (l!=0):
        t=g%l
        g=l
        l=t
    return a*b/g
print('s=',lcm(a,b))