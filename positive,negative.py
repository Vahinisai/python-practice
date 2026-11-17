#Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
a = float(input("enter a number:"))
result  = 1 if a>0 else -1 if a<0 else 0
print("result:",result) 
