# wap find the biggest number
a = input("enter a : ")
b = input("enter b : ")
c = input("enter c : ")
if ( a < b ):
    big  = b
    if(big < c):
        big = c
else:
    big = a
    if(big < c):
        big = c
print "big : ",big

# wap find the given year is leap year  or not
# 2000 ---> leap
# 1900 ---> Not leap
# 2008 ---> Leap leap
# 2003 -->> not leap 
