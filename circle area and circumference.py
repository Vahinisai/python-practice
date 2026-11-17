import math
try:
  r = float(input("enter radius of circle:"))
  area = math.pi*r**2
  cir = 2*math.pi*r
  print(F'Area:{area:.2f}')
  print(F'Circumference:{cir:.2f}')
except:
  print("input should be an float(or)input")
