#practice1214
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
path='./smoothedco2.dat'
with open(path,'r')as f:
  data1=f.read().split()  #讀之後的全部資料，並用空白鍵把每個資料做分割

year=[]
co2=[]
for i in range(0,178):
  year.append(int(data1[i*2]))
for i in range(1,179):
  co2.append(float(data1[i*2-1]))


n=178  #x的長度
for no in range(2,6):
#no=3  #階數-1
    a=np.zeros((n,no), dtype=np.float)
    at=np.zeros((no,n), dtype=np.float)
    y=np.zeros((n,1), dtype=np.float)


    for i in range(0,n):
        a[i,0]=1
        a[i,1]=year[i]
        if (no>2):
            for j in range(0,n):
                for k in range(2,no):
                    a[j,k]=year[j]**(k)
        
        #print(a)
        for l in range(0,n): #L的轉置矩陣=U矩陣
            y[l,0]=co2[l]
            for j in range(0,no):
                at[j,l]=a[l,j]
    
    z=at.dot(a)
    b=at.dot(y)
    x0=(np.linalg.inv(z)).dot(b)
    yr=a.dot(x0)
    plt.plot(year,yr,label=str(no-1))
plt.scatter(year,co2,s=2,label="true",color="r") #畫原本的點
plt.legend() #顯示圖例
plt.show
