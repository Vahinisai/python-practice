#Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

a = int(input("enter a number:"))
result = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
try:
 if a>=0 and a<=10:
   print(result[a])
 else:
   print("not a digit") 
except:
   print("input should be an integer")    
