#Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
a = eval(input("enter a number:"))
b = eval(input("enter a number:"))
c = eval(input("enter a number:"))
largest = a if (a>b and a>c) else b if b>c else c
print("largest:",largest)  

#largest of two numbers (use ternary operator)
a = eval(input("enter 1st input:"))
b = eval(input("enter 2nd input:"))
max = a if a>b else b 
print("maximum num:",max)
  
