
def f(x):
  return (x**2-1)
from scipy import optimize

root = optimize.brentq(f,-2,0)
print(root)
root2=optimize.brentq(f, 0, 2)
print(root2)
#root=optimize.brentq(f,0,2)