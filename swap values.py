#Write  a  program  to  swap  values  of  two   objects   using  3rd  object
a = int(input("enter a first number:"))
b = int(input("enter a second number:"))
print("before swap:","a=",a,"b=",b)
c = a
a = b
b = c
print("after swap:","a=",a,"b=",b)


#Write  a  program  to  swap  values  of  two  objects  without  using  3rd  reference
a = int(input("enter a first num:"))
b = int(input("enter a second num:"))
print("before swap:","a=",a,"b=",b)
a = a+b
b = a-b
a = a-b
print("before swap:","a=",a,"b=",b)


#swap two numbers without using third object(one multiplication,two dvision)
a = float(input("enter 1st input:"))
b = float(input("enter 2nd input:"))
print("before swap:","a=",a ,"b=",b)
a = a*b
b = a/b
a = a/b
print("after swap:","a=",a,"b=",b)


#swap two numbers without using third reference(using truncate)
a = int(input("enter a first number:"))
b = int(input("enter a second number:"))
print("before swaping:","a=",a,"b=",b)
a,b = b,a
print("after swaping:","a=",a,"b=",b)
