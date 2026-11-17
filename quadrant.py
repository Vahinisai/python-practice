#Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
 4th  quadrant , x - axis , y - axis   or  origin

tpl = eval(input("enter a tuple of (x-coordinate,y-coordinate)"))
x,y = tpl
if x>0 and y>0:
  print("1st-quadrant")
elif x<0 and y>0:
  print("2nd-quadrant")
elif x<0 and y<0:
  print("3rd-quadrant")
elif x>0 and y<0:
  print("4th-quadrant")
elif x!=0 and y==0:
  print("x-axis")
elif x==0 and y!=0:
  print(y-axis)
else:
  print("origin")  
    
                

