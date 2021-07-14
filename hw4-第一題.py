import numpy as np
import matplotlib.pyplot as plt

temp=[]  #建立temp的空矩陣
y=[]  #建立y的空矩陣
path='./inversion.txt'  #讀檔路徑
with open(path,'r')as f:  #讀檔
  data=f.readline()  #讀掉第一行的T(C)
  data1=f.read().split()  #讀之後的全部資料，並用空白鍵把每個資料做分割
  data2=[] #建立空矩陣
  for i in data1:  #data1的每個元素，從1開始
    try:
      data2.append(float(i))  #將data1的字串轉成浮點數依序加入data2矩陣
    except ValueError:  #將不是數字的部分跳過(Height(m))
      pass
temp=data2[0:48]  #temp矩陣=data2矩陣的0~47
height=data2[48:97] #height矩陣=data2矩陣的48~96

f2=[] #建立空矩陣
f1=[] #建立空矩陣
f11=((height[1]-height[0])/(temp[1]-temp[0])) #第0項使用前差法求其一階微分

f1.append(f11) #將f11的值加入矩陣f1
n=1
while n<47: #建立迴圈,使用中插法找1~46項的一階微分
  fa=((height[n+1]-height[n-1])/(temp[n+1]-temp[n-1])) #中差法公式，我就不多說了
  f1.append(fa)  #將fa的值加入矩陣f1

  n=n+1 #n=n+1繼續下一個迴圈

f12=((height[47]-height[46])/(temp[47]-temp[46])) #第47項使用後插法求一階微分
f1.append(f12) #加進矩陣
f21=(f1[1]-f1[0])/(temp[1]-temp[0])  #二階微分值，一樣利用前插
f2.append(f21) #加進矩陣
n=1
while n<47: #建立迴圈,使用中插法找1~46項的二階微分
  fb=(((height[n+1]-height[n])/(temp[n+1]-temp[n]))-((height[n]-height[n-1])/(temp[n]-temp[n-1])))/(((temp[n]+temp[n+1])/2)-((temp[n]+temp[n-1])/2)) #中差法公式，我就不多說了
  f2.append(fb) #將fb的值加入矩陣f2
  n=n+1 #n=n+1繼續下一個迴圈

f22=((f1[47]-f1[46])/(temp[47]-temp[46])) #第47項使用後插法求二階微分
f2.append(f22) #加進矩陣
i=0
print('{:<3}'.format('n'),'{:<10}'.format('溫度℃'),'{:<20}'.format('一階微分值'),'{:<20}'.format('二階微分值')) #印出標題
for i in range(48):
  print('{:<3}'.format(i),'{:<11}'.format(temp[i]),'{:<20}'.format(f1[i]),'{:<20}'.format(f2[i])) #印出每個值
print('\n逆溫範圍=\n') #印出標題
for i in range(48): #如果一階微分>0就印出，用來判斷逆溫層
  if f1[i]>0:
    print(i,f1[i])
x=temp  #令x=temp畫圖會用到
y=height #令y=height畫圖會用到
x1=temp[0:8]  #逆溫範圍
y1=height[0:8] #逆溫範圍
plt.plot(x,y,label='temperature') #畫出溫剖圖
plt.plot(x1,y1,color='r',label='inversion') #畫出逆溫範圍
plt.axhline(height[8],color= 'y',alpha=0.5,label='inversion height') #畫出逆溫層高度

a=str(height[8]) #將逆溫高度轉成字串
plt.text(-20,height[8],a) #畫出標示逆溫的數字在-20,height[8]的位置(才不會擋到圖)
plt.ylabel('Height (m)') #y軸標題
plt.xlabel('T(℃)') #x軸標題
plt.legend() #圖例
plt.show #顯示圖