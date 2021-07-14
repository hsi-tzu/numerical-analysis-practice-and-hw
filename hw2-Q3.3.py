#Q3.3 Compose your own program based on Fig. 3.11 and use it to determine your computer’s machine epsilon.
# Machine epsilon 代表甚麼意義?
# 答:machine epsilon 是計算機中最小的浮點數，滿足1+machine epsilon=1.可以說是浮點運算中的精度.
epsilon=1 

while epsilon+1>1: 
  epsilon=epsilon/2 

epsilon=2*epsilon
print(epsilon)