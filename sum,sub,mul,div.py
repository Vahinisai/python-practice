try:
  a = complex(input("enter the first complex:"))
  b = complex(input("enter the second complex:"))
  print("sum:",a+b)
  print("sub:",a-b)
  print("mul:",a*b)
  print("div:",a/b)
except:
  print("input should be an complex number")
