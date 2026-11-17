#Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
'<'  if  1st  input  <  2nd  input  and '='  if  inputs  are  same

a = eval(input("enter the first input:"))
b = eval(input("enter the second input:"))
result = ">" if a>b else "<" if a<b else "="
print("result:",result)
