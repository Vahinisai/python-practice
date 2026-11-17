#Write  a  program  to  determine  simple  interest  and  compound  interest
p = float(input("enter the principle:"))
t = float(input("enter the time:"))
r = float(input("enter a rate of interest:"))
simple_interest = p*t*r/100
compound_interest = p*(1+r/100)**t-p
print("simple interest:",simple_interest)
print("compund interest:",compound_interest)
