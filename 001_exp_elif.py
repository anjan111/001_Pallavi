# wap print salaries based on exp
exp = input("enter exp in years : ")
if( exp >= 0 and exp < 2):
    print "salary 5L PA"
elif( exp >= 0 and exp < 4):
    print "salary 10L PA"
elif(exp >= 0 and  exp < 8):
    print "salary 15L PA"
elif( exp >= 0 and exp < 15):
    print "salary 25L PA"
elif(exp >= 0 and  exp < 20):
    print "salary 45L PA"
elif(exp >= 0 and exp >= 20):
    print " salary 1 cr PA"
else:
    print "Please provide the proper exp"

