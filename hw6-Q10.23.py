#Q10.23
import numpy as np
#  a*0+b=c*2+d=1  >>b=1,c*2+d=1
#  a*1+b=c*1+d   >>a+b-c-d=0
#  a+b=4

a=np.array([[0.0,1.0,0.0,0.0],[0.0,0.0,2.0,1.0],[1.0,1.0,-1.0,-1.0],[1.0,1.0,0.0,0.0]])
a0=np.array([[0.0,1.0,0.0,0.0],[0.0,0.0,2.0,1.0],[1.0,1.0,-1.0,-1.0],[1.0,1.0,0.0,0.0]])
x=np.array([[1.0],[1.0],[1.0],[1.0]])
b=np.array([[1.0],[1.0],[0.0],[4.0]])
n=4
er=0
o=[]
s=[]
tol=0.05
#分解
for i in range(0,n):
  o.append(i)  #將i加入o矩陣
  s.append(abs(a[i,1])) #將a[i,0]加入s矩陣
  for j in range(1,n):
    if abs(a[i,j])>s[i]: #如果同一列有數大於s[i](同一列第一個被加進去的數)，較大的就取代之，直到s矩陣是每一列最大的數
      s[i]=abs(a[i,j])
for k in range(0,n-1):
  p=k
  big=abs(a[k,k]/s[k]) #pivot=對角線數/最大值
  for l in range(k+1,n): #從下一列開始比較(k+1列)，找pivot最大的列
    dummy=abs(a[l,k]/s[l]) #假設dum=某列的值/某列最大值
    if dummy>big:  #如果dum>big，即某列值/最大值>原列值/最大值
      big=dummy #pivot值改成dum
      p=l #p由k列改成l
  if p!=k:  #如果p不等於k:
    for m in range(k,n):#把第一列和下面的列數比較，若p不等於k則每一列元素和原本的互換，
       d=a[p,m] #a矩陣的互換
       a[p,m]=a[k,m]
       a[k,m]=d
    c=b[p,0]  #b矩陣互換
    b[p,0]=b[k,0]
    b[k,0]=c
    
    e=s[p]  #s矩陣互換
    s[p]=s[k]
    s[k]=e

    c=o[p]  #o矩陣互換
    o[p]=o[k]
    o[k]=c
#print(a,b,o)
for k in range(0,n-1):
  for i in range(k+1,n): #LU矩陣
    f=(a[i,k])/(a[k,k]) #pivot要的乘a21/a11
    a[i,k]=f #L矩陣
    for j in range(k+1,n):
      a[i,j]=a[i,j]-((a[k,j])*f) #U矩陣

if abs(a[k,k]/s[k])<tol:  #確定每一列pivot係數不為0，若為0則停止
  er=-1
  print([k,k]/s[k])
#print(a)
for k in range(1,n): #求d1,d2,d3的值
    sum=b[k,0]  #從第二式開始算d2
    for j in range(0,k):
     sum=sum-(a[k,j]*b[j,0]) #依序算出d2.d3 
    b[k,0]=sum #將d存入b
x[3,0]=(b[3,0]/a[3,3])
#print("x2=",x[3,0])
for k in range(2,-1,-1): #用上三角矩陣算出x的值
     s=0
     for j in range(k+1,n):
       s+=(a[k,j]*x[j,0])
    
     x[k]=(b[k,0]-s)/a[k,k]
print("a,b,c,d=\n",x)