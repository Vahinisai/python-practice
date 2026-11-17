#Write  a  program  to  test  year  is  leap  year  or  not
a = int(input("enter a number:"))
if a%4==0 or (a%400==0 and a%100!=0):
  print("leap year")
else:
  print("not a leap year")  
